#Automated template-match code (ATMC) - version 1.0

'''
Code that implements template matching procedure
to systematically detect ground-coupled airwaves.

The code implements functions from Obspy, Scipy,
Numpy and Multiprocessing libraries. Also detect_peaks 
function (Duarte and Watanabe, 2019) is used for detection
of events.

Input files: 

- Database files: Files of seismic records. The code
manages one-hour files of database. txt format 
or seismic format (MSEED, SAC, SEISAN, etc.) can be used.

- Template file: File of the master signal. txt format
or seismic format (MSEED, SAC, SEISAN, etc.) can be used.

'''

import numpy as np
import matplotlib.pyplot as pt
import multiprocessing as mp
from obspy import read
import scipy.signal
from scipy import fftpack
import obspy.signal.cross_correlation as ost
import obspy
import os
from detect_peaks import detect_peaks
import obspy.signal.filter as filt


#############Function that creates non-existing files#####################

def create_file(channel,month,day,hour):

	'''
	Function that creates non-existing files in the database in order to
	avoid a sudden stop in the execution of the code.

	Creates a sac file that contains an array of zeros.

	Arguments of the function are:

	- Channel: HHE, HHN, HHZ, BHE, BHN, BHZ
	- Month: Month of the year
	- Day: Day of the month
	- Hour: Time of the day

	Returns:

	- Sac file of 1-hour length of zeros. THe time corresponds to 
	the month, day and hour entered in the arguments of the function.


	'''

	prev_data = channel+'.'+month+'.1.0_DISP.sac'
	a = read(prev_data,debug_headers=True)
	index = a[0].data.shape[0]
	
	#Changes values inside SAC file by zeros
	for i in range(0,index,1):
		a[0].data[i]=1
	
	new_name=channel+'.'+month+'.'+str(day)+'.'+str(hour)+'_DISP.sac'
	new_file=a.write(new_name)
	print('Accomplished')
	return new_file

######Function that extract time windows and do cross correlation#########

def cut_and_correlate(template,time_series,windows,nt,nts):

	'''

	Function that cuts an array into several windows and calculates
	the absolute correlation coefficient.

	Input data:

	- template: variable that contains the template
	- time_series: variable that contains the one-hour data file
	- windows: number of windows 
	- nt: number of samples of template
	- nts: number of samples of time_series

	'''
	l_l = 0
	u_l = nt
	coeff = []
	for l in range(0,windows,1):
		array = time_series[l_l:u_l]
		correl = ost.correlate(array,template,2)
		correl = abs(correl); shift,value = ost.xcorr_max(correl)
		coeff.append(value)
		l_l = l_l + 1
		u_l = u_l + 1
	return coeff

#######################RMS calculation#####################################

def RMS(array):

	'''
	Computes the root mean square of a sequence of data

	Input: 

	- array: array of elements

	Output:

	- rms: value of rms of array.

	'''
	suma = 0
	N = array.shape[0]
	for i in range(0,N,1):
		square_comp = array[i]**2
		suma = suma + square_comp
	
	value = suma/N
	rms = np.sqrt(value)
	return rms

###########################################################################

print('Automated Template-Matching Code (ATMC) - Version 1.0')

#Threshold value
thres = 0.5

#Insert component of seismic records
comp = "HHZ"

#Section related to the template
template_file_name = 'template1.txt'

#Here the template is loaded as an ASCII file
new_template = np.loadtxt(template_file_name)
print('Loaded template: ',template_file_name)

#Obspy read function to load template if in a seismic data format 
#new_template = read("template5.sac")

#Removal of RMS
rms = RMS(new_template)
#print('RMS Template: '+str(rms))
new_template = new_template - rms

switch = False
switch2 = False

#Decimation of the template using scipy function decimate
#Applies to both the template and database records

while(switch == False):
	dec = input('Decimate signals? (y)es/(n)o: ')
	if(dec == 'y'):

		while(switch2 == False):
			try:
				dec_fac = int(input('Decimation factor?: '))
				switch2 = True
			except ValueError:
				print('Type an integer')
				switch2 = False

		new_template = scipy.signal.decimate(new_template,dec_fac)
		switch = True
	elif(dec =='n'):
		print('No decimation')
		switch==True
	else:
		print('Enter y/n')
		switch == False
		pass

#Open directory path using os library
os.chdir('/home/gerardomendo/Documentos/Datos_PPIG/Dec_18_waveforms/'+ comp)

#Entry of months of the year. 01 - January, 02 - February, ... , 12 - December
#Months must be inserted as a list of elements
month = ['12']

#Entry of the hour. Hours must be as elements of a list
hour = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]

# Cross correlation matrix for the year(entered first as a list). Rows: correlation values month arrays, Columns:number of windows
list_values = []

for i in month:

	#List of correlation values of the month - Later converted as matrix
	list_corr = []

	#List with correlation values of the month - Later converted into array
	values_corr_mes = []

	if i == '02':
		last_day = 24

	elif i == '04' or i == '06' or i == '09' or i == '11':
		last_day = 31

	elif i == '03':
		last_day = 27

	else:
		last_day = 32

	directory = comp+ i
	os.chdir(directory)

	#last_day = 2	

	for j in range(1,last_day,1):

		for k in hour:
			
			#Time series for cross correlation
			#Automatically generates name file. Name: Component_month_day_hour.extension
			#For example : name_file = "HHZ.02.1.1.sac"
			#Year is not included

			name_file = comp+'.'+str(i)+'.'+str(j)+'.'+str(k)+'_DISP.sac'
			#Uncomment if .txt file
			#name_file = comp+'.'+str(i)+'.'+str(j)+'.'+str(k)+'_DISP.txt'
			print('File: ',name_file)

			#Section of the code that looks for missing files in the database.
			#If missing files, create_files is called in order to avoid stopping.

			try:
				timeseries = read(name_file)
				#Uncomment if using .txt files
				#timeseries = np.loadtxt(name_file)

			except FileNotFoundError:
				print('No archive found - Creating zeros file')
				create_file(comp,i,j,k)
				timeseries = read(name_file)

			#Detrending using a linear function from obspy library
			timeseries.detrend('linear')

			#RMS removal
			timeseries_data = timeseries[0].data
			rms = RMS(timeseries_data)
			timeseries_data = timeseries_data - rms

			if(dec == 'y'):
				#Decimation of the window. If not needed, comment the line.
				timeseries_data = scipy.signal.decimate(timeseries_data,dec_fac)
			else:
				timeseries_data = timeseries_data

			#Number of samples of the time series
			nt = new_template.shape[0]
			nts = timeseries_data.shape[0]

			#s is the overlap factor
			#the movement of the time window

			s = 1
			#Here n_windows (Eq. 3 in Mendo-Pérez et al., 2021) must be added 1 value
			n_windows = int((nts - nt)/s) + 1
			print('Number of windows: ',n_windows)

			#Time series parameters
			fs = 100
			dt = 1/fs
			t = np.arange(0,nts*dt,dt)

			#Uncomment if not Pool functions is not needed (if uncomment, comment lines 245 - 247)
			#coef=cut_and_correlate(new_template,timeseries_data,n_windows,nt,nts)

			#Calculation of correlation values applying Pool function
			pool = mp.Pool(4)
			coef = [pool.apply(cut_and_correlate,args=[new_template,timeseries_data,n_windows,nt,nts])]
			pool.close()

			#Creation of coef array - Correlation values per window
			coef = np.asarray(coef); coeff = coef[0,:]
			
			#Appending coef elements into list_corr list and creating list_corr array - Correlation values per hour
			list_corr.append(coeff)

	#Conversion of list into array using Numpy function asarray
	list_corr = np.asarray(list_corr)
	print(list_corr.shape)
	print(list_corr.shape[0])


	#Appending and generating valores_corr_mes array - Correlation values per month
	#In this section, we re-order the correlation coefficients in an array
	for iii in range(0,list_corr.shape[0],1):
			for jjj in range(0,list_corr.shape[1],1):
				values_corr_mes.append(list_corr[iii][jjj])

	values_corr_mes = np.asarray(values_corr_mes)

	#Saving correlation values in ASCII file with name: Values_month_year_template.txt
	np.savetxt('R_values_'+ i +'_17_'+template_file_name+'.txt',values_corr_mes,delimiter='')
	
	#Applying detect_peaks function (Duarte & Watanabe, 2018) to correlation array to search for detections.
	detect = detect_peaks(values_corr_mes,mph=thres,mpd=30)
	print('Detections on '+i+': ')
	print(detect)
	
	#Peaks detected saved in an ASCII file with name: Peaks_year_month_component_template.txt
	name_detect = 'Peaks_17_'+ i + '_' + comp +'_'+ template_file_name+'.txt'
	np.savetxt(name_detect,detect,delimiter='')
	
	#Saving monthly detect values on a huge list
	list_values.append(values_corr_mes)

	#Returning to the main directory
	os.chdir('/home/gerardomendo/Documentos/Datos_PPIG/Dec_18_waveforms/'+ comp)


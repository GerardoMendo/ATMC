# Automated Template-Match Code (ATMC)

Code that applies a template matching procedure to systematically detect ground-coupled airwaves in seismic records.
The code implements Scipy, Numpy, Obspy and multiprocessing functions. 

Detection of airwaves is performed by implementation of detect_peaks function, created by Duarte & Watanabe, 2018
(https://github.com/BMClab/BMC).

Input data:

- Database of seismic records in ASCII format or seismic data format (MSEED, SAC, among others).
- File where template is saved in ASCII or seismic data format.
- Threshold value
- Overlapping factor between time windows s, in samples. 

To see more details about its application to a database, see Mendo-Pérez et al. (in prep). 

Template input file:

.txt files or seismic files (SAC,Seisan,MSEED) can be used. If .txt files is used, enable line 149;
if seismic file is used, enable line 149. The file template1.txt is an example of a template used for
this code.

Database input files:

The name of the input files has the following format

name_component.month.day.hour.format

name_component must be specified in line 139
month must be entered as a list of elements in line 189
day are automatically calculated using a for loop in line 222
hour is entered as a list in line 192
format is .sac by default. If other format is used, change lines
231, 240 - 242.
Year is not considered in the file names because database is separated
per year, and they have the same names. 

The format of the files of the database can be changed in line 231.

Decimation 

Decimation are applied to both database files and template files. Used in order to reduce
time of calculations. The decimation is performed using scipy.signal.decimate
function (see Scipy documentation for more information about this function). Prior to
the calculations, the program asks for decimation. Valid input are y (yes) and n (no) keys.
If y key is entered, a decimation factor must be entered. Only integer values can be used.

Remove of RMS and trend

RMS and detrend of the template and the database is performed before cross correlation
calculations. RMS is calculated by using an internal function. Detrending is perfomed by 
using obspy stream property detrend (see Obspy documentation for more info). Linear detrending 
is applied by default. Type of detrending can be changed in line 250.

Cross correlation 

Calculations of correlation values are performed by using obspy.signal.cross_correlation.correlate
and obspy.signal.cross_correlation.xcorrmax (for more information about this functions, see Obspy
documentation).

Multiprocessing

Multiprocessing calculation of R values is performed by applying pool function. For more information
about pool function, see multiprocessing documentation in Python standard library. By default, it is implemented
but it can be changed by commenting lines 284 - 286 and uncomment line 281.

Output data:

- .txt file of absolute correlation (|R|) values (R-file) per month. 
   Name of the file: R_values_component_year_templatefilename.txt
   
- .txt file that contains index of the elements in the |R| array above threshold.
  Name of the file: Peaks_year_component_templatefilename.txt












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

Output data:

- .txt file of absolute correlation (|R|) values (R-file) per month. 
   Name of the file: R_values_component_year_templatefilename.txt
   
- .txt file that contains index of the elements in the |R| array above threshold.
  Name of the file: Peaks_year_component_templatefilename.txt

To see more details about its application to a database, see Mendo-Pérez et al. (in prep). 

Template input file

.txt files or seismic files (SAC,Seisan,MSEED) can be used. If .txt files is used, enable line 149;
if seismic file is used, enable line 149. The file template1.txt is an example of a template used for
this code.

Database input files

The name of the input files has the following format

name_component.month.day.hour.format

name_component must be specified in line 139
month must be entered as a list of elements in line 189
day are automatically calculated using a for loop in line 222
hour is entered as a list in line 192

Year is not considered in the file names because database is separated
per year, and they have the same names. 

If the format of the name files want to be changed, change line 231.








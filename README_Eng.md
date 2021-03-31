# Automated Template-Match Code (ATMC)

ENGLISH

Code that applies a template matching procedure to systematically detect ground-coupled airwaves 
in seismic records. This code implements Scipy, Numpy, Obspy and Multiprocessing functions. Detection of 
airwaves is performed by implementation of detect_peaks function, created by Duarte & Watanabe, 2018 
(https://github.com/BMClab/BMC). 

Requirements to run:

To run the code please install Python 3.7, NumPy, ObsPy, SciPy and Multiprocessing libraries. To see how to download
and install them in different environments (Windows, MacOS and Linux), please refer to the official websites of each
package. Here we strongly recommend the use of Anaconda (https://www.anaconda.com/). 

How to run the code:

In a terminal window, type the following command:

      python ATMCV1.0.py 
      
If using IPython, type the following sentence:

      %run ATMCv1.0.py

Input data:

a) File of master signal/template in .txt or seismic data format (MSEED, SAC, SEISAN).
b) Files of seismic records in .txt format or seismic data format (MSEED, SAC, SEISAN).
c) Threshold value (float).
d) Overlapping factor between time windows s, in samples (integer). 

a) Master signal/template file:

Name of the file and format must be typed in line 141. If .txt files is used, 
enable line 144; if seismic file is used, enable line 148. The file template1.txt 
is an example of a template used for this code.

b) Files of database:

The names of the files have the following order:

name_component.month.day.hour.format

name_component must be specified in line 139;

month must be entered as a list of elements in line 189;

day are automatically calculated using a for loop in line 222;

hour is entered as a list in line 192;

format is .sac by default. 

If other format is used, change lines 231, 240 - 242.

Year is not considered in the file names because database is separated
per year, and they have the same names. 

If required, the elements of the file name can be changed in line 231.

c) Threshold value:

When running the code, threshold value is asked to enter. Threshold value
is float by default. If an integer is entered, automatically changes to float.

d) Overlapping factor s

When running the code, overlapping factor value (s) is asked to enter. s value
is integer by default. If a float value is entered, the program asks continuously
until an integer value is entered.

Implemented functions

- Decimation of signals

Decimation are applied to both database files and template file. It is used to reduce
the time of calculations. The decimation is performed using scipy.signal.decimate
function (see https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html
for more information about this function). 
Prior to the start of calculations, the program asks for decimation. Valid inputs are: y (yes) and n (no) 
keys. If y key is entered, a decimation factor must be entered; only integer values are allowed.

- Remove of RMS and trend

RMS and detrend of the database files and template file is performed before cross correlation
calculations. RMS is calculated by using an internal function. Detrending is perfomed by 
using obspy stream property detrend (see https://docs.obspy.org/packages/autogen/obspy.core.stream.Stream.decimate.html
for more info). Linear detrending is applied by default. Type of detrending can be changed in line 250.

- Cross correlation 

Calculations of correlation values are performed by using obspy.signal.cross_correlation.correlate
and obspy.signal.cross_correlation.xcorrmax (for more information about this functions, see
https://docs.obspy.org/packages/autogen/obspy.signal.cross_correlation.html). 

- Multiprocessing

Multiprocessing calculation of R values is performed by applying pool function. For more information
about pool function, see https://docs.python.org/3/library/multiprocessing.html. 
By default, it is implemented but it can be changed by commenting lines 284 - 286 and uncomment line 281.

- Detection of events

detect_peaks function of Duarte and Watanabe (2018) is implemented to search for peaks in R plots (for more information
about this function, see https://github.com/BMClab/BMC). 

Output data:

1. txt file of absolute correlation (|R|) values (R-file) per month. 
   Name of the file: R_values_component_year_templatefilename.txt
   
2) txt file that contains index of the elements in the |R| array above threshold.
  Name of the file: Peaks_year_component_templatefilename.txt

References

Numpy
Scipy
Obspy
Multiprocessing
Duarte and watanabe

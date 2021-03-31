# Automated Template-Match Code (ATMC) - Readme (English version)

Content

1. Description
2. Requirements to run
3. How to run the code
4. Input data
5. Implemented functions
6. Output data
7. References

1. Description

Code that applies a template matching procedure to systematically detect ground-coupled airwaves 
in displacement seismic records. This code implements Scipy (Virtanen et al., 2020), Numpy (Harris et al., 2020), 
Obspy (Beyreuther et al., 2010) and Multiprocessing (Python software foundation, 2001) functions. 
Detection of airwaves is performed by implementation of detect_peaks function (Duarte & Watanabe, 2018). 

2. Requirements to run:

ATMC code is written in Python programming language. To run the code Python 3.7, NumPy, ObsPy, SciPy and Multiprocessing 
libraries must be installed. Information related to Download and installation in different operative systems (Windows, MacOS and Linux)
is available in the official websites of each package. Here we strongly recommend the use of Anaconda (https://www.anaconda.com/). 
detect_peaks function must be downloaded from Duarte & Watanabe Github webpage: https://github.com/BMClab/BMC. 

3. How to run the code:

- Linux

In a terminal window, type the following command:

      python ATMC_1.0.py 
      
If using IPython, type the following sentence:

      %run ATMC_1.0.py

If using an IDE environment (e.g., Spyder) load the file and select the Run command to execute the code. 

- MacOS 

The instructions for Linux also apply to MacOS systems.

- Windows

Anaconda environment is strongly recommended for Windows users. If not, in a terminal window (e.g., Cygwin)
type the following command

      python ATMC_1.0.py

4. Input data:

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

- name_component must be specified in line 139;
- month must be entered as a list of elements in line 189;
- day are automatically calculated using a for loop in line 222;
- hour is entered as a list in line 192;
- format is .sac by default. If other format is used, change lines 231, 240 - 242.

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

5. Implemented functions

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

6. Output data:

- txt file of absolute correlation (|R|) values (R-file) per month. 
   Name of the file: R_values_month_year_templatefilename.txt
   
- txt file that contains index of the elements in the |R| array above threshold.
  Name of the file: Peaks_year_component_templatefilename.txt

7. References

Beyreuther, M., Barsch, R., Krischer, L., Megies, T., Behr, Y., & Wassermann, J. (2010). ObsPy: A Python Toolbox for Seismology. Seismological Research Letters, 81(3), 530 - 533.  https://doi.org/10.1785/gssrl.81.3.530

Duarte, M. & Watanabe, R. N. (2018). Notes on Scientific Computing for Biomechanics and Motor Control. GitHub repository, https://github.com/BMClab/BMC.

Harris, C. R., Millman, K. J., van der Walt, S. J., Gommers, R., Virtanen, P., Cournapeau, D., Wieser, E., Taylor, J., Berg, S., Smith, N. J., Kern, R., Picus, M., Hoyer, S., van Kerkwijk, M. H., Brett, M., Haldane, A., Fernández del Río, J., Wiebe, M., Peterson, P, … Oliphant, T. E. (2020). Array programming with NumPy. Nature, 585, 357–362. https://doi.org/10.1038/s41586-020-2649-2

Python software foundation.(2001). Python Documentation. https://docs.python.org/3/contents.html

Virtanen, P., Gommers, R., Oliphant, T. E., Haberland, M., Reddy, T. R., Cournapeau, D., Burovski, E., Peterson, P., Weckesser, W., Bright, J., van der Walt, S. J., Brett, M., Wilson, J., Millman, K. J., Mayorov, N., Nelson, A. R. J., Jones, E., Kern, R., Larson, E., … SciPy 1.0 Contributors (2020). SciPy 1.0: fundamental algorithms for scientific computing in Python. Nature Methods, 17(3), 261-272. https://doi.org/10.1038/s41592-019-0686-2


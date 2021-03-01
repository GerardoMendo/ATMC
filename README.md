# ATMC

Code that applies a template matching procedure to systematically detect ground-coupled airwaves in seismic records.
The code implements Scipy, Numpy and Obspy functions. Also, detection of peaks can be either using an internal function
or by using detect_peaks function, created by Duarte, 2019.

Input data:

- Database of seismic records in ASCII format or seismic data format (MSEED, SAC, among others).
- File where template is saved in ASCII or seismic data format.
- Threshold value
- Overlapping factor between time windows, in samples. 

Output data

- ASCII file of absolute correlation (|R|) values (R-file).
- ASCII file that contains index of the R file where window surpasses threshold value.




# Automated Template-Match Code (ATMC)

Code that applies a template matching procedure to systematically detect ground-coupled airwaves in seismic records.
The code implements Scipy, Numpy and Obspy functions. 

Detection of airwaves is performed by implementation of detect_peaks function, created by Duarte & Watanabe, 2018
(https://github.com/BMClab/BMC).

Input:

- Database of seismic records in ASCII format or seismic data format (MSEED, SAC, among others).
- File where template is saved in ASCII or seismic data format.
- Threshold value
- Overlapping factor between time windows s, in samples. 

Output:

- .txt file of absolute correlation (|R|) values (R-file) per month. 
   Name of the file: R_values_component_year_templatefilename.txt
   
- .txt file that contains index of the elements in the |R| array above threshold.
  Name of the file: Peaks_year_component_templatefilename.txt

To see more details about this work and its application to a database, see Mendo-Pérez et al. (in prep). 

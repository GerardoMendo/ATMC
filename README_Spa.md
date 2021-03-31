# Automated Template-Match Code (ATMC)

Este codigo usa template matching para detectar sistemáticamente ondas de aire acopladas al terreno
en los registros sísmicos de desplazamiento. Implementa funciones de las librerías NumPy, ObsPy, SciPy 
y Multiprocessing. La detección de las ondas de aire se realiza con la función detect_peaks, creada
por Duarte y Watanabe (2018) (https://github.com/BMClab/BMC).

Requerimientos:

Para ejecutar el código debe tener instalado Python 3.7, y las librerías NumPy, ObsPy, SciPy, Multiprocessing. Para ver
cómo descargar e instalar las diferentes librarías en los diferentes sistemas operativos (Windows, MacOS y Linux), por favor
refiérase a los sitios oficiales de cada paquetería. Recomendamos ampliamente el uso de Anaconda (https://www.anaconda.com/). 

Cómo correr el código

En una ventana de terminal, escriba la siguiente línea de comando:

      python ATMCV1.0.py 
      
Si se usa IPython, escriba la siguiente línea de comando:

      %run ATMCv1.0.py

Datos de entrada:

a) Archivo de señal maestra/template en formato txt o de dato sísmico (MSEED, SAC, SEISAN).
b) Archivos de registros sísmicos en format txt o de dato sísmico (MSEED, SAC, SEISAN).
c) Valor umbral (flotante).
d) Factor de trasplape entre ventanas s, en muestras (entero). 

a) Archivo de señal maestra/template:

El nombre del archivo y el formato se introducen en la línea 141. Si se usa un archivo txt 
habilite la línea 144; si se usa un archivo con formato de dato sísmico, habilite la línea 148.
El archivo template1.txt es un ejemplo de un template usado en este código.

b) Archivos de registros sísmicos:

Los nombres de los archivos deben seguir el siguiente orden:

componente.mes.día.hora_DISP.formato

componente debe introducirse en la línea 139;

mes debe entrar como una lista de elementos en la línea 189;

día es automáticamente calculado usando un ciclo for en la línea 222;

hora se introduce como una lista de elementos en la línea 192;

_DISP es de referencia para registros de desplazamiento;

formato es .sac por defecto. 

Si se usa otro formato, cambiar las líneas 231, 240-242.

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


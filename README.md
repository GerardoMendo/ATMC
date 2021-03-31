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

1. File of master signal/template in .txt or seismic data format (MSEED, SAC, SEISAN).
2. Files of seismic records in .txt format or seismic data format (MSEED, SAC, SEISAN).
3. Threshold value (float).
4. Overlapping factor between time windows s, in samples (integer). 

1. Master signal/template file:

Name of the file and format must be typed in line 141. If .txt files is used, 
enable line 144; if seismic file is used, enable line 148. The file template1.txt 
is an example of a template used for this code.

2. Files of database:

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

3. Threshold value:

When running the code, threshold value is asked to enter. Threshold value
is float by default. If an integer is entered, automatically changes to float.

4. Overlapping factor s

When running the code, overlapping factor value (s) is asked to enter. s value
is integer by default. If a float value is entered, the program asks continuously
until an integer value is entered.

Implemented functions

- Decimation 

Decimation are applied to both database files and template files. Used in order to reduce
time of calculations. The decimation is performed using scipy.signal.decimate
function (see Scipy documentation for more information about this function). Prior to
the calculations, the program asks for decimation. Valid input are y (yes) and n (no) keys.
If y key is entered, a decimation factor must be entered. Only integer values can be used.

- Remove of RMS and trend

RMS and detrend of the template and the database is performed before cross correlation
calculations. RMS is calculated by using an internal function. Detrending is perfomed by 
using obspy stream property detrend (see Obspy documentation for more info). Linear detrending 
is applied by default. Type of detrending can be changed in line 250.

- Cross correlation 

Calculations of correlation values are performed by using obspy.signal.cross_correlation.correlate
and obspy.signal.cross_correlation.xcorrmax (for more information about this functions, see Obspy
documentation).

- Multiprocessing

Multiprocessing calculation of R values is performed by applying pool function. For more information
about pool function, see multiprocessing documentation in Python standard library. By default, it is implemented
but it can be changed by commenting lines 284 - 286 and uncomment line 281.

- Detection of events

detect_peaks function of Duarte and Watanabe (2018) is implemented to search for peaks in R plots (for more information
about this function, see https://github.com/BMClab/BMC). 

Output data:

1. .txt file of absolute correlation (|R|) values (R-file) per month. 
   Name of the file: R_values_component_year_templatefilename.txt
   
2. .txt file that contains index of the elements in the |R| array above threshold.
  Name of the file: Peaks_year_component_templatefilename.txt

References

SPANISH

Código que aplica template matching para detección sistemática de ondas de aire acopladas al terreno
en los registros sísimicos. Este código implementa funciones de SciPy, NumPy, ObsPy y Multiprocessing. 
La detección de las ondas de aire se realiza a través de la función detect_peaks, creada por Duarte & Watanabe (2008).
(https://github.com/BMClab/BMC). 


Datos de entrada:

- Archivos de los registros sísmicos en formato .txt o formato de dato sísmico (MSEED, SAC, entre otros).
- Archivo del template guardado en formato .txt o formato de dato sísmico.
- Valor umbral (flotante)
- Factor de traslape entre ventanas de tiempo (en muestras, valor entero).

Archivo de template:

Archivos con extensión .txt o de dato sísmico (SAC,Seisan,MSEED) pueden ser usados. 
Si se usa la extensión.txt, habilite la línea 141; si se usa la extensión de dato 
sísmico, habilite la línea 148. El archivo template1.txt, adjunto al git, es un 
ejemplo de un archivo de entrada de template.

Archivos de la base de datos:

El nombre de los archivos de la base de datos deben tener el siguiente formato:

nombre_componente.mes.día.hora.formato

nombre_componente debe ser especificado en la línea 139 (BH*, HH*),
mes debe ingresarse como una lista de elementos en la línea 189,
día es automáticamente calculado usando un ciclo for en la línea 222,
hora es ingresado como una lista de elementos en la línea 192
formato está establecido como .sac por defecto. Si se usa otro formate, 
cambiar las líneas 231, 240 - 242.
El año no se considera dentro del nombre de los archivos debido a que la 
base de datos se separa por año.

The formato del nombre de los archivos de la base de datos puede cambiarse
en la línea 231.

Funciones implementadas

- Decimación 

La decimación se aplica al template y a los archivos de la base de datos. Se usa para
reducir el tiempo de cálculo. Se realiza a través de la función scipy.signal.decimate
(vea la documentación de SciPy para más información sobre esta función). Antes de realizar
los cálculos, el programa pregunta si se deciman los registros. Entradas válidas son y para
sí y n para no. Si se usa y, se debe poner el factor de decimación. Solo valores enteros
pueden ser ingresados.

- Remover RMS y tendencia

Se remueven el RMS y la tendencia de los archivos de template y la base de datos antes del cálculo
de las correlaciones. El RMS se calcula usando una función interna. La tendencia se remueve usando  
la propiedad del objeto stream de obspy detrend (vea la documentación de ObsPy para más información).
Por defecto, se calcula y se remueve una tendencia lineal. El tipo de tendencia se puede cambiar en 
la línea 250.

- Correlación

El cálculo de la correlación se realiza usando la función de ObsPy obspy.signal.cross_correlation.correlate
y obspy.signal.cross_correlation.xcorrmax (para más información sobre el uso de estas funciones, refiérase
a la documentación de ObsPy).

- Multiprocessing

El cálculo multiproceso de los valores R se realiza usando la función pool (para más información de esta
función, refiérase a la documentación de Multiprocessing en Python standard library). Por defecto, se implementa
pero esto se cambia comentando las líneas 284 - 286 y quitando el símbolo de comentario (#) de la línea 281.

- Detection of events

detect_peaks function of Duarte and Watanabe (2018) is implemented to search for peaks in R plots (for more information
about this function, see https://github.com/BMClab/BMC). 

Output data:

- .txt file of absolute correlation (|R|) values (R-file) per month. 
   Name of the file: R_values_component_year_templatefilename.txt
   
- .txt file that contains index of the elements in the |R| array above threshold.
  Name of the file: Peaks_year_component_templatefilename.txt

References











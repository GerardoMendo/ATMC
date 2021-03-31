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

El año no se considera en el nombre de los archivos debido a que la base 
de datos se separa por año, y para cada año los nombres de los archivos
son los mismos. Si se requiere, se puede cambiar el formato del nombre
de los archivos de entrada en la línea 231.

c) Valor umbral:

Cuando se ejecuta el código, el valor umbral es requerido para continuar.
El valor umbral es flotante por defecto. Si se ingresa un entero, se convierte
automáticamente en flotante.

d) OFactor de traslape s

Cuando se ejecuta el código, el factor de traslape s es requerido para continuar.
El valor s es entero por defecto. Si un valor flotante es ingresado, se redondea
automáticamente a entero.

Funciones implementadas

- Diezmado de señales

Diezmado de señales es aplicado tanto para los archivos de la base de datos como al archivo de template. Se aplica para 
reducir el tiempo de cálculo. El diezmado se realiza usando la función scipy.signal.decimate
(vease https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.decimate.html para más información acerca de esta
función).
Antes del comienzo de los cálculos, el programa pregunta si las señales se deben diezmar. Entradas válidas son: Tecla y (yes) y tecla n (no).
Si se ingresa el caracter y, se pide introducir un factor de diezmado; sólo se pueden ingresar valores enteros.

- RMS and tendencia

Se remueve el RMS y la tendencia de las señales, de la base de datos y del template, antes del comienzo de los cálculos. 
El RMS se calcula con una función establecida. La tendencia se elimina usando la propiedad del objeto Stream de Obspy
detrend (vease https://docs.obspy.org/packages/autogen/obspy.core.stream.Stream.decimate.html para más información). 
Se elimina tendencia lineal por defecto. El tipo de tendencia que se elimina se puede cambiar en la línea 250.

- Correlación 

El cálculo de los coeficientes de correlación (R) se realiza con las funciones obspy.signal.cross_correlation.correlate
y obspy.signal.cross_correlation.xcorrmax (para más información sobre estas funciones, véase
https://docs.obspy.org/packages/autogen/obspy.signal.cross_correlation.html). 

- Multiprocessing

El cálculo multiproceso de los coeficientes de correlación values se realiza usando la función pool. Para más información 
relacionada con la función pool, véase https://docs.python.org/3/library/multiprocessing.html. 
Por defecto está implementada, pero puede cambiarse al comentar las líneas 284 - 286 y quitando el signo de comentario (#) 
de la línea 281.

- Detección de eventos

La función detect_peaks de Duarte and Watanabe (2018) se implementa para buscar los picos que sobrepasan el valor umbral
en los arreglos de valores R (para más información de cómo funciona esta función, véase https://github.com/BMClab/BMC). 

Datos de salida:

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


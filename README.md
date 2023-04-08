# Challenge-Data-Scientist-Rolf-Traeger

Work about predicting the probability of delay of the ﬂights that land or take oﬀ from the airport of Santiago de Chile  (SCL). `delay_15` reflect if the flight was a delay or not.


## Definición del problema

**El problema consiste en predecir la probabilidad de retraso de los vuelos(representado por la columna `delay_15`)** que aterrizan o despegan del aeropuerto de Santiago de Chile (SCL). Para eso tendrás un dataset con datos públicos y reales donde cada fila corresponde a un vuelo que aterrizó o despegó de SCL durante el 2017.

Para cada vuelo se encuentra disponible la siguiente información:
Columns in `data\dataset_SCL.csv`:

```python
"Fecha-I" : "Scheduled date and time of the ﬂight"
"Vlo-I" : "Scheduled ﬂight number"
"Ori-I" : "Programmed origin city code"
"Des-I" : "Programmed destination city code"
"Emp-I" : "Scheduled ﬂight airline code"
"Fecha-O" : "Date and time of ﬂight operation"
"Vlo-O" : "Flight operation number of the ﬂight"
"Ori-O" : "Operation origin city code"
"Des-O" : "Operation destination city code"
"Emp-O" : "Airline code of the operated ﬂight"
"DIA" : "Day of the month of ﬂight operation"
"MES" : "Number of the month of operation of the ﬂight"
"AÑO" : "Year of ﬂight operation"
"DIANOM" : "Day of the week of ﬂight operation"
"TIPOVUELO" : "Type of ﬂight, I =International, N =National"
"OPERA" : "Name of the airline that operates"
"SIGLAORI" : "Name city of origin"
"SIGLADES" : "Destination city name"
```

A modo de resumen los atributos que posee  `-I` definen el valor programado originalmente, y los atributos Acompañados por un `-O` son los atributos que resultaron finalmente, tras realizado el vuelo. esto se refleja directamente en las columnas `"Fecha-I"` y `"Fecha-O"` y la logica para el cálculo del `min_diff`

Columns to make:

```python
"high_season" : 'Binary variable that reflects if the flight was on a high demand date or not'
"period_day" : 'Reflects the situation on the day the flight lands'
"min_diff" : 'Flight delay in minutes'
"delay_15" : 'Binary variable that reflects if the flight was a delay or not'
```

## Librearias utilizadas

Comandos de instalación:

```cmd
conda install plotnine
conda install pandas
conda install scikit-learn
conda install -c anaconda git
```

- conda install plotnine
    > Graficador configurable con amplia gama de graficos y temas
- conda install pandas
    > Gestor de dataframes
- conda install scikit-learn
    > Libreria de modelos predictivos
- conda install -c anaconda git
    > Libreria que habilita la gestion de repositorios.


## Data de estudio

Toda la data a utilizar se encuentra en la carpeta `...\data\`

Se incorporó además de la data propuesta para el desafio, información meteorologica de todo el año 2017, la cual está particionada a nivel hora, debido a que esta información no existe para todos los registros, se utilizó el promedio del mes que se realizó el vuelo para rellenar la información faltante de cada vuelo.

## Columnas a utilizar

Tomando en cuenta que existen varias columnas que reflejan lo mismo o informaicón que representa el futuro como `Fecha-O` o el atributo construido `min_diff`, se debe reducir las columnas que ensucien el proceso y que no influyan sobre `delay_15`.

## Procesamiento de datos

Se definieron las principales transformaciones para el data frame probeniente del archivo dataset_SCL.csv en la libreria `exploratory_lib.py`. Este archivo python es utilizado para guardar las funciones, procedimiento y clases más repetitivos.

## Atributos de interes

Tomando en cuenta que los atributos presentes en el archivo inicial representan la misma información o no es relevante para predecir los atrasos se seleccionarón los más influyente por un analisis cualitativo y un analizis de Chi-cuadrado.

## Data utilizada para el estudio

Se realizó un filtrado doble sobre los datos, donde en primer lugar se eliminarón de los registros todos los vuelos a destinos con menos del mil registros en el DF. Luego se realizó el mismo filtro sobre los operadores y por último nuevamente sobre las ciudades de destino, quedando así con 7 compañias y 18 ciudades de destino.
pese a ello se abordo al rededor de l 80% de los datos entregados inicialmente.

## 
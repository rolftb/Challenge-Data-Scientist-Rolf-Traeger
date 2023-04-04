# Challenge-Data-Scientist-Rolf-Traeger

Work about predicting the probability of delay of the ﬂights that land or take oﬀ from the airport of Santiago de Chile  (SCL). `delay_15` reflect if the flight was a delay or not.

## Índice o Proceso de trabajo

1. Definición del problema
2. Librearias utilizadas
3. Data de estudio
4. Columnas a utilizar

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

## Data de estudio

Toda la data a utilizar se encuentra en la carpeta `...\data\`

## Columnas a utilizar

Tomando en cuenta que existen varias columnas que reflejan lo mismo o informaicón que representa el futuro como `Fecha-O` o el atributo construido `min_diff`, se debe reducir las columnas que ensucien el proceso y que no influyan sobre `delay_15`.

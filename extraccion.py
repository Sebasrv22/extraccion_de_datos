print("APLICACION DE EXTRACCION DE DATOS")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_excel('detalle_precios_productos_fabricados_2022.xlsx')
# print(df.info)

# print(df.head())

# FILTRO 1 por objeto
filtro1=df[df["NOMBRE_VENDEDOR"] == "LETICIA RAMIREZ HERNANDEZ"]
print(filtro1)
filtro1.to_csv("Entregable1.csv")

# FILTRO 2 por fila
filtro2= df.iloc[2:8,: ]   
print(filtro2)
filtro2.to_csv("Entregable2.csv")

#FILTRO 3 por columnas
filtro3=df.iloc[ : , [1, 3, 4,10]]  
print(filtro3)
filtro3.to_csv("Entregable3.csv")


df['FECHA_DOC'] = pd.to_datetime(df['FECHA_DOC'])

# FILTRO 4 corregido: Filtrar por rango de fechas específico
filtro4 = df[df['FECHA_DOC'].isin(['2022-11-22', '2022-12-23'])][['SUBTOTAL_PARTIDA']]
print(filtro4)
filtro4.to_csv("Entregable4.csv")


#FILTRO 5
filtro5=df.head(8)
filtro5

#FILTRO 6
filtro6=df[df["SUBTOTAL_PARTIDA"] > 77000]
filtro6
filtro6.to_csv("Entregable6.csv")

#FILTRO 7
filtro7=df[(df["SUBTOTAL_PARTIDA"] > 77000) & (df["FECHA_DOC"] == "2022-05-24")]
filtro7
filtro7.to_csv("Entregable7.csv")

#FILTRO 8
filtro8=df[(df["SUBTOTAL_PARTIDA"] > 77000)| (df["FECHA_DOC"] == "2022-05-24")]
filtro8
filtro8.to_csv("Entregable8.csv")

# FILTRO 9
filtro9=df[~(df["SUBTOTAL_PARTIDA"] > 77000) & ~(df["FECHA_DOC"] == "2022-05-24")]
filtro9
filtro9.to_csv("Entregable9.csv")


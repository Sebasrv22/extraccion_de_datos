import pandas as pd

df = pd.read_excel("datos_facturacion.xlsx")
print(df.head())

filtro1 = df['CVE_CLPV'].between(1000, 2000)
print(filtro1)
filtro1.to_csv("practica_facturacion_1.csv")
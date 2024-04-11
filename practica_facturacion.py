import pandas as pd


df = pd.read_excel("datos_facturacion.xlsx")

# Filtro 1: CVE_CLPV debe estar entre 1000 y 2000
filtro1 = (df['CVE_CLPV'] >= 1000) & (df['CVE_CLPV'] <= 2000)
#print(filtro1)
filtro1.to_csv("Practica_facturacion1.csv")

# Filtro 2: CVE_VEND no debe ser 5 ni 4
filtro2 = df[ ~(df["CVE_VEND"] == 5.0) & ~(df["CVE_VEND"] == 4.0) ]
print(filtro2)
filtro2.to_csv("Practica_facturacion2.csv")

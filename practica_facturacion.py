import pandas as pd


df = pd.read_excel("datos_facturacion.xlsx")

# Filtro 1: CVE_CLPV debe estar entre 1000 y 2000
filtro1 = (df['CVE_CLPV'] >= 1000) & (df['CVE_CLPV'] <= 2000)
print(filtro1)
filtro1.to_csv("Practica_facturacion1.csv")

import pandas as pd


df = pd.read_excel("datos_facturacion.xlsx")

# Filtro 1: CVE_CLPV debe estar entre 1000 y 2000
filtro1 = (df['CVE_CLPV'] >= 1000) & (df['CVE_CLPV'] <= 2000)
#print(filtro1)
filtro1.to_csv("Practica_facturacion1.csv")

# Filtro 2: CVE_VEND no debe ser 5 ni 4
filtro2 = df[ ~(df["CVE_VEND"] == 5.0) & ~(df["CVE_VEND"] == 4.0) ]
#print(filtro2)
filtro2.to_csv("Practica_facturacion2.csv")

# filtro 3
# year
#filtro3=df[ df["FECHA_ENT"].dt.strftime('%Y') == '2019']
# year-month
#filtro3=df[ df["FECHA_ENT"].dt.strftime('%Y-%m') == '2019-10']
# year-month-day
filtro3=df[ df["FECHA_ENT"].dt.strftime('%Y-%m-%d') == '2019-10-02']

print(filtro3)

# Filtro 4: CAN_TOT debe ser menor que 5951.7 o STATUS debe ser 'E'
filtro4 = (df['CAN_TOT'] < 5951.7) | (df['STATUS'] == 'E')
print(filtro4)
filtro4.to_csv("Practica_facturacion4.csv")

# Filtro 5: Seleccionamos solo las columnas especificadas
filtro5 = ['CVE_DOC', 'FECHA_ENT', 'FECHA_VEN', 'CAN_TOT']
print(filtro5)

#importar biblioteca
import pandas as pd 
"""
#series
#crear serie
lista=[10,20,30,40,50]
serie=pd.Series(lista)

print(lista)
print(serie)

#dataframe
datos = {
    "Nombres":["Cesar","Edwin","Ivan","Brandon","Cristian"],
    "Edad":[19,22,22,23,25],
    "Asignatura":["Bases de datos","Arquitectura","Programacion","Estadistica","Ingenieria"]
}

libreria=pd.DataFrame(datos)
print(datos)
print(libreria)


#leer archivos desde pandas

Datos_csv=pd.read_csv('tips.csv')
#head()--> primeras filas y encabezados de columnas
print(Datos_csv.head())
"""

#cargar archivo excel
"""
datos_excel = pd.read_excel("ventas_limpio.xlsx",sheet_name="copia") #leer otra hoja de excel
print(datos_excel.head())
"""
"""
datos_excel = pd.read_excel("ventas_limpio.xlsx") 
print(datos_excel.head())
#metodos para trabajo con archivos y pandas
#ver las columnas del archivo
print(datos_excel.columns) #imprime el index, las 1eras 

#mostrar columnas en especifico con sus datos
print(datos_excel[['categoria','producto','precio']])
"""
"""
datos_excel = pd.read_excel("ventas_limpio.xlsx",sheet_name="none") #leer todas las hojas excel
"""
datos_excel = pd.read_excel("ventas_limpio.xlsx") 
print(datos_excel.head())
print(datos_excel[datos_excel['precio']==100000])
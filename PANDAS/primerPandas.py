
import pandas as pd 

datos = {
   'nombre':['lady','edwin','sebastian', 'samantha'],
   'edad':[35,23,52,63],
   'ciudad':['bogota','chiquinquira','españa', 'barbosa']
}
#podemos crear a traves de diccionarios columnas etc, "dataframes"= tabla organizada que permite vizualizar de mejor manera
control = pd.DataFrame(datos)
control.to_csv('dataframepython.csv',index=False) #convertir a csv
print('archivo creado con exito')

#"archivos csv" grandes cantidades de informacion con peso minimo
"""
archivo = pd.read_csv(tips.csv) #se tiene que importar el csv en vs
print(archivo.head()) #5 primeras filas
print(archivo.tail()) #5 ultimas filas
#numpy y pandas no se instala en colab
"""

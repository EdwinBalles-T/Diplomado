#Taller estudiantes 

import pandas as pd

estudiantes = {
    "Nombre": ["Cesar", "Edwin", "Ivan", "Brandon", "Cristian"],
    "Edad": [19, 22, 22, 23, 25],
    "Nota1": [2.3, 4.5, 3.8, 5.0, 2.8],
    "Nota2": [2.9, 3.4, 3.9, 2.5, 2.9]
}

listaEst = pd.DataFrame(estudiantes)
#Columna promedio
listaEst["Promedio"]= (listaEst["Nota1"] + listaEst["Nota2"])/2

aprobados = listaEst[listaEst["Promedio"] >= 3.0]

print(listaEst)
print("\nEstudiantes aprobados\n",aprobados)

aprobados.to_csv("aprobados.csv")



import matplotlib.pyplot as plt
import pandas as pd
"""
x=[1,2,3,4,5,6]
y=[2,4,6,8,10,12]

fig, ax = plt.subplots()
ax.plot(x, y, marker="s" ) #marker puede ser o,s,t
ax.set(title="regresion lineal", xlabel="X", ylabel="y")

ax.grid(True, alpha=0.8)

plt.show()
"""
"""
#Diagrama de linea ingresos diarios
archivo.groupby("fecha")["ingreso"].sum().plot(kind='line',figsize=(8,4))
plt.title("ingresos diarios")
plt.xlabel("Fecha")
plt.ylabel("Ingresos")
plt.show()
"""
archivo= pd.read_excel('datosventa.xlsx')
#diagrama de barrras
archivo.groupby('sucursal')['precio']|sum().plot(kind='barh',color=["red","blue","purple","black"], figsize=(6,4))
plt.title("precios por sucursal")
plt.xlabel("sucursal")
plt.ylabel("precios")
plt.show()
#Diagrama torta
archivo.groupby("categoria")["ingreso"].sum().plot(
   kind='pie',figsize=(6,6),autopct="%1.1f%%"
)
plt.title("Distribucion de ingresos por categoria")
plt.show()
#funcion sin parametros
def mensaje_bienvenida():
    print('Bienvenido a python')
mensaje_bienvenida()
mensaje_bienvenida()
mensaje_bienvenida()

#funcion con parametros
nombre=input('digite su nombre: ')

def saludar(nombre):
    print('holaaa ',nombre)

saludar(nombre)

#funcion con retorno de valor

def calcular_area_rectangulo():
    base=int(input('digite la base en cm del rectangulo: '))
    altura=int(input('digite la altura en cm del rectangulo: '))
    return base*altura
print(calcular_area_rectangulo())
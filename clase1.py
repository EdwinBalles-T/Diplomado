#Proyecto 1
"""
Edwin Ballesteros
inge

"""

#Funcion propias de python
"""print()


input()"""
"""
num1=0
num2=0
num1=int(input('digite un numero'))
num2=int(input('digite un numero'))
print('la suma es: ',num1+num2)
print(f'la suma es: {num1+num2}')

a=12
b=4.5
c="hola"
d=True

print(type(a)) #dice la clase de las variables

#listas= variable que puede contener muchos valores
ejemplo_lista = []
"""
lista_elementos = [4, 3, 5, 6, 77, 8, 655, 4, 3, 4, 5, 7, 3, 33, -9]
listo_decimales = [3.4, 2.4, 4.6, -9.5]
lista_general = [4, 3.5, True, "Texto"]

#tuplas= inmutables, elementos constantes

# Agregar un elemento a la lista
"""print(listo_decimales)
# listo_decimales.append(input('Digite el elemento para adicionar: '))
listo_decimales.insert(2,98.56)
print(listo_decimales)
#eliminar un elemento de la lista
#pop remove
print(lista_general)
#lista_general.pop()

lista_general.remove(4)
print(lista_general)
print(lista_elementos)
print(sorted(lista_elementos, reverse(True)))
"""
"""
#tuplas
tupla = {2,3,4,5,6,7,8,9,}
print(sorted(tupla, reverse(True)))"""

#Diccionario = manejan elementos clave valor, cada valor tiene una clave
#coleccion desordenada mutable
"""ejemplo={ "nombre":"edisson",
          "edad":39 ,
          "hobbies": ["leer","pasear","calificar"]  }
print(ejemplo)
print(ejemplo["nombre"])
print(ejemplo.get("edad"))
ejemplo["hobbies"]="caminar"
print(ejemplo)
"""

# ciclos condicional if
"""a=5
b=43
calificacion = float(input('digite su calificacion: '))
if calificacion==5:
    print('excelente')

elif calificacion>=4 and calificacion<5:
    print('sobresaliente')
elif calificacion>2 and calificacion>=3:
    print('es')"""
#bucle for
"""
lista=[1,2,3,4,5,6,4,2,6,0]
palabra = "hola a todos"
for i in palabra:
    print(i)

for i in range(5):
    print(i)
"""
"""
num = int(input())
for i in range(1,11,1):
    print(f'{num} X {i} = {num*i}')
#while
i=0
while i<5:
 print(i)
 i+=1

while True:
   a=int(input('digite un numero: '))
   if a>0:
      print('numero positivo')
      break
   else:
      a= int(input('digite un numero: '))
"""

#while------------------------
"""i=1
num = int(input())
while i <= 10:
    print(f'{num} X {i} = {num * i}')
    i += 1

while True:
    numero = int(input("Escribe un número (0 para salir): "))
    if numero == 0:
        print("Programa terminado.")
        break
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
#Funciones con y sin parametros

#importar bibliotecas
#declaracion de funciones
#codigo

def multiplicar(x,y):
    return x*y

a=int(input('Digite el numero 1: '))
b=int(input('Digite el numero 1: '))

print(multiplicar(a,b))
"""
#conversion de tipos
"""int()
float()
str()
bool()"""
numero =int('10') #de texto a numero entero
decimal =float('45.234') #de texto a decimal
print(numero, decimal)

#OPERACIONES CON NUMEROS
#abs() muestra el valor absoluto de un numero
print(abs(-45))
#round() redondea numero
print(round(3.14159,2))
#pow() potencia
print(pow(2,3))
#max() min()
print(max(1,5,6,7,2,3,5))
print(min(3,5,2,5,6-1,5))
#sum() sumar
print(sum([5,4,3,7,2,7,2,7,2,-45]))
#longitud de una cadena len()
print(len("edwin"))
#type() muestra el tipo de variable que se usa
a=10
print(type(a))
#funcion unicode de un caracter
print(ord("@"))
#funcion caracter a partir de unicode
print(chr(142))

#sistema estudiantes
estudiantes=[]

nombre=input('digite su nombre')
edad=int(input('digite su edad'))

def agregar_estudiante(nombre, edad):
  tupla={nombre, edad}
  lista=[tupla]
  return lista

def mostrar_estudiante(lista):
  for i in range (2):
    print(lista(i))
    i+=1
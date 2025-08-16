#uso de funciones integradas
texto=input('redacta un texto: ')
print(texto.lower())
print(texto.upper())
print(len(texto))
print(texto.capitalize())

#filtrado de numeros
lista=[1,2,3,4,5,6,7,8,9,10]
mayores = filter(lambda x: x > 3, lista)
print(list(mayores)) 

#Enumeracion
lista=['cartagena','paipa','bogota','medellin']
enun=enumerate(lista) 
print(list(enun))

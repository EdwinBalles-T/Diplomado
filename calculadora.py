#Calculadora
from sumar import suma
from restar import resta
from multiplicar import multiplicacion
from dividir import division
from potenciar import potenciar
from menu import menu

control = 0

while True:
    menu()
    control = int(input('Digite la opcion deseada: '))
    if control == 1:
        print(f'la suma es: {suma()}')
        continuar = input('desea continuar? Presione S para continuar o N para salir:  ')
        continuar = continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 2:
        print(f'la resta es: {resta()}')
        continuar = input('desea continuar? Presione S para continuar o N para salir:  ')
        continuar = continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 3:
        print(f'la multiplicacion es: {multiplicacion()}')
        continuar = input('desea continuar? Presione S para continuar o N para salir:  ')
        continuar = continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 4:
        print(f'la division es: {division()}')
        continuar = input('desea continuar? Presione S para continuar o N para salir:  ')
        continuar = continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 5:
        print(f'la potencia es: {potenciar()}')
        continuar = input('desea continuar? Presione S para continuar o N para salir:  ')
        continuar = continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 6:
        print('Hasta pronto')
        break
    else: 
        print('opcion invalida')

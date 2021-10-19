import random as rd

#----------EJERCICIO 1---------------------
print('\n---EJERCICIO 1-------\n')

valuesUserList = list(input('Ingrese valores de a,b y c: '))

a = ''.join(valuesUserList[0:valuesUserList.index(' ')])

b = ''.join(valuesUserList[valuesUserList.index(' ')+1:valuesUserList.index(' ',valuesUserList.index(' ')+1)])

c = ''.join(valuesUserList[valuesUserList.index(' ',valuesUserList.index(' ',valuesUserList.index(' ')+1))+1:])

randomNum = rd.randint(1,5)
print(f'El valor de x es: {randomNum}')

myFunction = (int(a) * randomNum**2 ) + (int(b) * randomNum) + int(c)

print(f'El resultado de la operación es: {myFunction}')


#----------EJERCICIO 2---------------------
print('\n\n---EJERCICIO 2-------\n')
userName = input('Ingrese su nombre: ')

randomNums = [rd.randint(1,6),rd.randint(1,6),rd.randint(1,6),rd.randint(1,6),rd.randint(1,6)]

print(f'Hola {userName}, los dados dieron los siguientes valores:')
print(randomNums)

print(f'El numero mas alto es: {max(randomNums)}')
print(f'El nuemero mas bajo es: {min(randomNums)}')
print(f'El promedio de los valores es: {sum(randomNums)/len(randomNums)}')


#----------EJERCICIO 3---------------------
print('\n\n---EJERCICIO 3-------\n')
list1= [8,9,10]
print('Copia de la lista lista1 que se aloje en la variable lista2')
list2 = list1[:]
print(list2)

print('En lista1, insertar como segundo elemento el valor de 17')
list1.insert(1,17)
print(list1)

print('Añadir 4, 5, y 6 al final de la lista1')
list1+= [4,5,6]
print(list1)

print('Remover el primer elemento de la lista2')
list2.pop(0)
print(list2)

print('Ordenar la lista lista2 de forma ascendente')
list2.sort()
print(list2)

print('Buscar el segundo elemento de lista2 en lista1')
print(list1.index(list2[1]))

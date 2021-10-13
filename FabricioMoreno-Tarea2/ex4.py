import random as rd

str = input('Ingrese una palabra: ')

totalIndexStr = len(str)-1
randomIndexStr1 = rd.randint(0,totalIndexStr)
randomIndexStr2 = rd.randint(0,totalIndexStr)
randomIndexStr3 = rd.randint(0,totalIndexStr)
randomIndexStr4 = rd.randint(0,totalIndexStr)
randomIndexStr5 = rd.randint(0,totalIndexStr)

finalMessage = 'Los caracteres aleatorios son: \n' + str[randomIndexStr1] + '-' + str[randomIndexStr2] + '-' + str[randomIndexStr3] + '-' + str[randomIndexStr4] + '-' + str[randomIndexStr5]

print(finalMessage)

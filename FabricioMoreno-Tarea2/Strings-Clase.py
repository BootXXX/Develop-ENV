
print('\n---INDEX---\n')
str = 'Fabricio'
print(f'This is my string: {str}')
print(f'{str[0]} ->Index 0 \n')
print(f'{str[2]} ->Index 2 \n')

print('\n----LENGTH---\n')
lengthStr = len(str)
print(lengthStr)

print('\n---Last Character---\n')
print(str[lengthStr-1])
print(str[-1])

print('\n----SLICING---\n')
subStr2 = str[2:6]
subStr3 = str[2:6:2]
subStr4 = str[:5]         #Equivalent str[0:5]
subStr5 = str[3:]         #Equivalent str[3:len(str)]
subStr6 = str[-5:-2]
subStr7 = str[:-2:-1]
print(subStr2)
print(subStr3)
print(subStr4)
print(subStr5)
print(subStr6)
print(subStr7)

print('\n---Concatenating--')
print('Hello ' + str)

print('\n----Multiply Strings---\n')
repeatStr = 'Hello '*4
print(repeatStr)




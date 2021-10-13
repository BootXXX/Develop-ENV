wordUser = input('Ingrese una palabra: ')

message1 = 'La primera letra de esta palabra es: ' + str(wordUser[0]) + '\n'

message2 = 'La ultima letra de esta palabra es: ' + str(wordUser[-1]) + '\n'

message3 = 'La cantidad de letras en la palabra es: ' + str(len(wordUser)) + '\n'

finalMessage = message1 + message2 + message3

print(finalMessage)

str = 'Estoy practicando para aprender a programar'

message1 = 'a) ' + str[0].lower() + str[1:].upper() + '\n'

message2 = 'b) ' + str[::-1] + '\n'

message3 = 'c) ' + str.replace('a','i') + '\n'

finalMessage = message1 + message2 + message3

print(finalMessage)

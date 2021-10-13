temperatureFarenheit = input('Ingrese la temperatura en grados Farenheit: ')

temperatureCelsius = (5/9) * (int(temperatureFarenheit)-32)

message = 'La conversion a Celsius es: ' + str(round(temperatureCelsius,2)) + ' grados'

print(message)
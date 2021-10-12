estatura = float(input("Ingrese la estatura en metros: "))
peso = float(input("Ingrese el peso en kilogramos: "))

imc = peso/(estatura**2)

tieneBajoPeso = imc < 18.5
tieneMedioPeso = 18.5 <= imc < 24.99
tieneSobrePeso = imc >= 25.00

print("Bajo peso: ", tieneBajoPeso)
print("Peso Normal: ", tieneMedioPeso)
print("Sobrepeso: ", tieneSobrePeso)

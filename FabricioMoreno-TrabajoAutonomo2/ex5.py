import random

listaCartas = ['AS','1','2','3','4','5','6','7','8','9','10','J','Q','K']

longitud = len(listaCartas)
numeroAzar = random.randint(0,longitud-1)
cartaAlAzar = listaCartas[numeroAzar]

cartaIngresada = input("Cual carta crees que salio?: ")
sonCartasIguales = cartaAlAzar == cartaIngresada
print("Resultado: ",sonCartasIguales)
print("Esta fue la carta al azar: ",cartaAlAzar)
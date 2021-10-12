palabra = input("Ingrese una palabra a verificar: ")

palabraInvertida = palabra[::-1]

esPalindroma = palabra == palabraInvertida

print("Es palindroma: ",esPalindroma)
# 2do ejercicio: verificador de caracteres para deterinar si son letras

cadena = input("Ingrese caracteres: ")

todos_son_letras = all(caracter.isalpha() for caracter in cadena)

# Resultado final
print(f"¿Todos los caracteres son letras? {todos_son_letras}")
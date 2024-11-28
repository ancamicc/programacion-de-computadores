# 1er ejercicio: contar ocurrencias de una letra 
palabra = input("ingresar una palabra:")
letra = input("ingresar la letra que se debe contar:")
c = 0 #contador 

for caracter in palabra:
    if caracter == letra:
      c += 1

print("la letra", letra,"aparece", c,"veces.")


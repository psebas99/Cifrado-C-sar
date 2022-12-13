texto = input("Ingrese el texto que desea decodificar: ")
c = input("Magnitud de la clave de corrimiento: ")
corrimiento = int(c)
mensaje_decodificado= ""

for n in texto:
    num = ord(n)
    mensaje_decodificado += chr(num - corrimiento)

print(mensaje_decodificado)
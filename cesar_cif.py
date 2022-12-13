texto = input("Ingrese el caracter: ")
d = input("Magnitud del corrimiento: ")
corrimiento = int(d)
mensaje= ""

for n in texto: 
    num = ord(n)
    mensaje += chr(num + corrimiento)

print(mensaje)
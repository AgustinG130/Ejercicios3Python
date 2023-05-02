def multiplicacionesuno(n,x):
    resultado = round(n * x)
    if resultado == 1:
        return True
    else:
        return False
n = float(input("Escriba numero "))
multiplicador = float(input("Escriba el multiplicador"))

if multiplicacionesuno(n,multiplicador):
    print("La multiplicación da 1")
else:
    print("La multiplicación no da 1")
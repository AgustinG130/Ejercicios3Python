def edad(n,e):
    if e >= 18:
        print(n + ", eres mayor de edad ")
    if e < 18:
        print(n + ", eres menor de edad ")
        
nombre = input("Escriba su nombre ")
eda = int(input("Escriba su edad "))
print(edad(nombre,eda))
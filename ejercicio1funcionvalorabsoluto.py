def valorabs(n):
    if n >= 0:
        return n
    else:
        return n*-1
    
n = int(input("Ingrese su numero "))
print("Su numero absoluto es: ", valorabs(n))
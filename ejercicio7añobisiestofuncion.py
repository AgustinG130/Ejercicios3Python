def aniobisiesto(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                print("El año", a, "es bisiesto")
            else:
                print("El año", a , "no es bisiesto")
        else:
            print("El año", a , "no es bisiesto")
    else:
        print("El año", a , "no es bisiesto")

anio = int(input("Escriba su año "))

aniobisiesto(anio)

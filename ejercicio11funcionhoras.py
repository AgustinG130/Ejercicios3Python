def horasdadas(hora1,hora2,min1,seg1,min2,seg2):
    if hora1 and min1 and seg1 < hora2 and min2 and seg2:
        return True
    else:
        return False
def horasaseg(hora,min,seg):
    segundos = ((hora * 3600) + (min *60) + seg)
    return segundos

hora1 = int(input("Ingrese hora 1 "))
min1 = int(input("Ingrese minuto 1 "))
seg1 = int(input("Ingrese segundo 1 "))
hora2 = int(input("Ingrese hora 2 "))
min2 = int(input("Ingrese minuto 2 "))
seg2 = int(input("Ingrese segundo 2 "))

if horasaseg(hora1,min1,seg1) == horasaseg(hora2,min2,seg2):
    print("Verdadero")
else:
    print("Falso")
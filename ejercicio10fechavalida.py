def fechadada (dia,mes,año):
    match mes:
        case "Enero":
            if dia <= 31:
                return True
            else:
                return False
        case "Febrero":
            if aniobisiesto(año):
                if dia <= 29:
                    return True
            else:
                if dia < 29:
                    return True
                if dia >= 29:
                    return False
        case "Marzo":
            if dia <= 31:
                return True
            else:
                return False
        case "Abril":
            if dia <= 30:
                return True
            else:
                return False
        case "Mayo":
            if dia <= 31:
                return True
            else:
                return False
        case "Junio":
            if dia <= 30:
                return True
            else:
                return False
        case "Julio":
            if dia <= 31:
                return True
            else:
                return False
        case "Agosto":
            if dia <= 31:
                return True
            else:
                return False
        case "Septiembre":
            if dia <= 30:
                return True
            else:
                return False
        case "Octubre":
            if dia <= 31:
                return True
            else:
                return False
        case "Noviembre":
            if dia <= 31:
                return True
            else:
                return False
        case "Diciembre":
            if dia <= 31:
                return True
            else:
                return False
def aniobisiesto(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

año = int(input("Ingrese Año "))
mes = input("Ingrese Mes ")
dia = int(input("Ingrese Dia "))

if fechadada(dia,mes,año):
    print("Es valido")
else:
    print("No es valida")
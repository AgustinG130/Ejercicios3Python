def SueldoAcordado(sueldo , aniotrabajado):

    if aniotrabajado >= 20:
        SueldoAntiguedad = 20
        SueldoA = sueldo + SueldoAntiguedad
        sueldototal = SueldoA
    else:
        SueldoAntiguedad = sueldo * 0.1 * aniotrabajado
        SueldoA = sueldo + SueldoAntiguedad
        sueldototal = SueldoA - ((SueldoA * 0.11) + (SueldoA * 0.6))
    if SueldoA > 120000:
        sueldodescontado = sueldototal - (sueldototal * 0.25)
        print("Su sueldo es de:",sueldodescontado)
    elif SueldoA > 70000 and SueldoA < 120000:
        sueldodescontado = sueldototal - (sueldototal * 0.20)
        print("Su sueldo es de:",sueldodescontado)
    else:
        print("Su sueldo es de:",SueldoA)

sueldo = float(input("Ingrese sueldo "))
años = int(input("Ingrese años trabajados "))
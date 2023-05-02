dia = input("\n 1- Lunes \n 2- Martes \n 3- Miercoles \n 4- Jueves \n 5- Viernes \n 6- Sabado \n 7- Domingo \n Escriba su dia ")

match dia:
    case "Lunes":
        print("Hoy comienza la semana. Animo!")
    case "Martes":
        print("Vamos que se puede!")
    case "Miercoles":
        print("Vamos que se puede!")
    case "Jueves":
        print("Vamos que se puede!")
    case "Viernes":
        print("Ya casi termina!")
    case "Sabado":
        print("Siiii! Fin de semana!")
    case "Domingo":
        print("Siiii! Fin de semana!")
    case _:
        print("Numero incorrecto")

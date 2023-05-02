dia = int(input("\n 1- Lunes \n 2- Martes \n 3- Miercoles \n 4- Jueves \n 5- Viernes \n 6- Sabado \n 7- Domingo \n Escriba su dia "))
match dia:
    case 1:
        print("Hoy comienza la semana. Animo!")
    case 2:
        print("Vamos que se puede!")
    case 3:
        print("Vamos que se puede!")
    case 4:
        print("Vamos que se puede!")
    case 5:
        print("Ya casi termina!")
    case 6:
        print("Siiii! Fin de semana!")
    case 7:
        print("Siiii! Fin de semana!")
    case _:
        print("Numero incorrecto")
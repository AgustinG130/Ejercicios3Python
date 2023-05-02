voto = input("A = Partido Rojo \n B = Partido Verde \n C = Partido Azul \n Escriba su voto ")
match voto:
    case "A":
        print("Usted ha votado por el Partido Rojo")
    case "B":
        print("Usted ha votado por el Partido Verde")
    case "C":
        print("Usted ha votado por el Partido Azul")
    case _:
        print("Opción errónea")


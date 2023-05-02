
pesopersona = int(input("Ingrese peso kg"))
alturapersona = float(input("Ingrese altura metros"))
imc = int
imc = round(pesopersona / (alturapersona ** 2))

if imc >= 30:
		print("Usted tiene obesidad")
if imc >= 25 and imc <= 29.9:
		print("Usted tiene sobrepeso")
if imc >= 18.5 and imc <= 24.9:
		print("Usted tiene peso adecuado")
if imc < 18.5:
		print("Usted tiene bajo peso")

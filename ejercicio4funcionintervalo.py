def pertenece_al_intervalo(N,linf,lsup):
 if N < linf and lsup > N:
     return True
 else:
     return False
    
N =float(input("Ingrese un número: "))

linf =float(input("Ingrese un límite inferior: "))

lsup =float(input("Ingrese un límite superior: "))

if pertenece_al_intervalo(N, linf, lsup):

     print("el número pertenece al intervalo")
else:
     print("el número no pertenece al intervalo")
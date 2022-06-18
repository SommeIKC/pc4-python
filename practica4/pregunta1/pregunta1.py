import random

def adivina_numero():
    try:
        n=int(input("Ingrese el valor de n:"))
        a = random.randint(1,n)
        entrada=0
        while(entrada!=a):
            entrada=int(input("Ingrese un numero:"))
            if(entrada<a):
                print("¡Demasiado pequeño!")
            elif(entrada>a):
                print("¡Te pasaste!")
        print("¡Adivinaste!")

    except ValueError:
        print("vuelva a ingresar valor")
        adivina_numero()
adivina_numero()    

import os

#comentario
def crear_tabla():
    n=int(input("Ingrese el numero para crear la tabla de multiplicar:"))
    if(n>=1 and n<=10):
                   
        with open(f'tabla-{n}.txt','w') as f:
            for i in range(1,12):
                texto= f'{n} x {i} = {n*i}\n'
                f.write(texto)
    else:
        crear_tabla()
def leer_fichero():
    n=int(input("Ingrese el numero para leer la tabla de multiplicar:"))
    try:
        if(n>=1 and n<=10):
            with open(f'tabla-{n}.txt','r') as f:
                data=f.read()
                print(data)
        else:
            leer_fichero()
    except FileNotFoundError:
        print("El fichero no existe")
        leer_fichero()
    
def traer_linea_m():
    try:
        n=int(input("Ingrese el numero para leer la tabla de multiplicar:"))
        m=int(input("Ingrese el numero para leer la linea de multiplicar:"))
        if(n>=1 and n<=10):
            with open(f'tabla-{n}.txt','r') as f:
                lineas=f.readlines()
                print(lineas[m-1])
        else:
            traer_linea_m()
    except FileNotFoundError:
        print("El fichero no existe")
        traer_linea_m()
    except IndexError:
        print(f"no existe la linea {m} en la tabla ")
def menu():
    print('''
        1.- Crear tabla de n
        2.- Leer tabla de n
        3.- Traer la linea m de la tabla n
        4.- Salir
    ''')
    option=int(input("Ingrese la opcion del 1 al 4: "))
    if(option==1):
        crear_tabla()
        menu()
    elif(option==2):
        leer_fichero()
        menu()
    elif(option==3):
        traer_linea_m()
        menu()
    elif(option==4):
        print("Saliendo del sistema")
menu()
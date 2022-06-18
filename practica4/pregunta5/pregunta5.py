
def contabilizar_lineas():
    try:
        ruta=input("Ingrese la ruta de un archivo .py:")
        contador=0
        if(ruta[-2:]=='py'):
            with open(ruta,'r') as f:
                lineas=f.readlines()
                for linea in lineas:
                    
                    if(linea.strip()=='' or linea[0]=="#" or linea[0:3]=='"""'):
                        contador=contador
                    else:
                        contador =contador+1
            print(f"Lineas : {contador}" )
        else:
            print("No es un archivo py, vuelva a ingresar")
            contabilizar_lineas()

    except FileNotFoundError:
        print("no se logro encontrar la ruta")
        contabilizar_lineas()
contabilizar_lineas()
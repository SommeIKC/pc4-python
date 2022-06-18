import re
text =  '52534583444444444'


def validar(text):
    
    lista=re.split(r'-',text)
    cadena=''
    
    for i in lista:
        if(len(i)==4 or len(i)==16):
            cadena = cadena + i
            
        else:
            return False
    for j in range(len(cadena)):
        if(cadena[j:j+4]==cadena[j]*4):
            return False
            
    regex = r'[4-6]\d{15}'
    if(len(re.findall(regex,cadena))==1):
        return True
    else:
        return False
def validar_tarjeta(text):
    if(validar(text)==True):
        print("Tarjeta valida")
    else:
        print("Tarjeta invalida")
validar_tarjeta('4123456789123456')
validar_tarjeta('5123-4567-8912-3456')
validar_tarjeta('61234-567-8912-3456')
validar_tarjeta('4123356789123456')
validar_tarjeta('5133-3367-8912-3456')
validar_tarjeta('5123 - 3567 - 8912 - 3456')


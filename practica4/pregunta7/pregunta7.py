import re


def validar(i):
    regex = r'.*@\D+.com'
    if(len(re.findall(regex, i))==1):
        print(f"The email {i} is valid email")
    else:
        print(f"The email {i} is invalid ")

lista=['n.john.smith@gmail.com', '87victory@hotmail.com','!#mary-=@msca.net']
for i in lista:
    validar(i)




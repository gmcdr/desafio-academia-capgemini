#QUESTÃO 2
import re 
password = input("Digite sua senha: ")
aux = 0
while True:   
    if (len(password)<6): 
        aux = -1
        break
    elif not re.search("[a-z]", password): 
        aux = -1
        break
    elif not re.search("[A-Z]", password): 
        aux = -1
        break
    elif not re.search("[0-9]", password): 
        aux = -1
        break
    elif not re.search("[_@$]", password): 
        aux = -1
        break
    elif re.search("\s", password): 
        aux = -1
        break
    else: 
        aux = 0
        print("Senha válida !!") 
        break

tam = len(password)

print(6 - tam)

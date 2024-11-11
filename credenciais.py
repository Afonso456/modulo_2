tentativas= 3
email_certo = "joaquim@gmail.com"
password_certa= "1234"
while tentativas > 0:
    email= input("Insira o seu email:")
    password= input("Insira a sua password:")
    if email == email_certo and password == password_certa:
        print("Sessão iniciada com sucesso")
        break
    tentativas = tentativas - 1
    if email != email_certo and password != password_certa:
        print("Email invalido")
    elif email != email_certo:
        print("Email invalido")
    else:
        print("Password errada")
    if tentativas == 0:
        print("Esgotou as 3 tentativas, tente novamente mais tarde")
import os
import api

os.system('cls' if os.name=='nt' else 'clear')
name = input("Придумайте себе имя (до 20 символов)\n")

con = api.Api(name)

con.load()

while True:
    print('__________')
    i = input('Чтобы обновить чат, нажмите Enter, чтобы отправить сообщение, напишите что-нибудь и нажмите Enter. Чтобы выйти, напишите q\n')

    if i == "":
        con.load()
    elif i == "q":
        raise SystemExit(1)
    else:
        con.send(i)

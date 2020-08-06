import os
import api

os.system('cls' if os.name=='nt' else 'clear')
name = input("Придумайте себе имя (до 20 символов)\n")

con = api.Api(name)

con.load()

while True:
    print('__________')
    i = input('Чтобы обновить чат, нажмите Enter, чтобы отправить сообщение, напишите что-нибудь и нажмите Enter\n')

    if i == "":
        con.load()
    else:
        con.send(i)

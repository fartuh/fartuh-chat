"""
Simple chat created using python3. Uses the API of https://fartuh.xyz
Copyright (C) 2020 Nikita Pavlov
This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/.
Author's email: nikitafartuh@ukr.net 
"""

import requests
import json
import os

class Api():
    login = ""
    password = ""

    #def __init__(self, login, password):
    #   self.setParams(login, password)

    def setParams(self, login, password):
        self.login = login
        self.password = password

    def load(self):
        login = self.login
        password = self.password
        os.system('cls' if os.name=='nt' else 'clear')
        res = requests.get("https://fartuh.xyz/api/chat/", params = {"login": login, "password": password})
        data = res.json()

        for i in range(-10, 0): 
            try:
                print(data[i]['login'] + ": " + data[i]['text'] + ": " + data[i]['sent_at'] + "\n")
            except IndexError:
                continue

    def send(self, text):
        text = text

        res = requests.post('https://fartuh.xyz/api/chat/index.php', data = {"login": self.login, "password": self.password, "text":text}) 

        if res.json()['result'] == True:
            os.system('cls' if os.name=='nt' else 'clear')
            self.load()
        else:
            print('Ошибка. Перезапустите клиент')

    def reg(self):
        print('Войдите или зарегистрируйтесь (Если указанного логина не существует, будет создан новый аккаунт)')

        login = input('Введите логин\n')
        password = input('Введите пароль (Не меньше 6 символов)\n')
        
        res = requests.post('https://fartuh.xyz/api/users/index.php', data = {"login": login, "password": password}) 

        responde = res.json()

        if responde['result'] == True:
            data = {'login': login, 'password': password}
            with open('data.json', 'w', encoding="utf8") as file:
                json.dump(data, file) 
            return data 
        else:
            if responde['errorcode'] == "1":
                print('Пароль слишком короткий')
                return self.reg()
            if responde['errorcode'] == "2":
                print('Пользователь с таким логином существует | Неверный пароль')
                return self.reg()














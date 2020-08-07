"""
Simple chat created using python3. Uses the API of https://fartuh.xyz
Copyright (C) 2020 Nikita Pavlov
This program is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License along with this program. If not, see http://www.gnu.org/licenses/.
Author's email: nikitafartuh@ukr.net 
"""

import os
import api
import json

os.system('cls' if os.name=='nt' else 'clear')

con = api.Api()

if(os.path.exists('data.json')):
    with open('data.json', 'r') as string:
        data = string.read()
    data = json.loads(data)
    try:
        if data['login'] != "" and data['password'] != "":
            con.setParams(data['login'], data['password'])
    except KeyError:
        data = con.reg()
        con.setParams(data['login'], data['password'])
else:
    data = con.reg()
    con.setParams(data['login'], data['password'])

con.load()

#chat

while True:
    print('__________')
    i = input('Чтобы обновить чат, нажмите Enter\nЧтобы отправить сообщение, напишите что-нибудь и нажмите Enter\nЧтобы выйти из чата, напишите /q\nЧтобы выйти из аккаунта, напишите /logout\n')

    if i == "":
        con.load()
    elif i == "/q":
        break
    elif i == "/logout":
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.json')
        os.remove(path) 
        break
    else:
        con.send(i)


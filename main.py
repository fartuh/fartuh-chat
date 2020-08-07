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
        break
    else:
        con.send(i)

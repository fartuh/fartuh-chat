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
    name = ""

    def __init__(self, name):
        if name == "":
            name = "Гость"
        self.setName(name)

    def setName(self, name):
        self.name = name

    def load(self):
        os.system('cls' if os.name=='nt' else 'clear')
        res = requests.get("https://fartuh.xyz/api/chat/")
        data = res.json()

        for i in range(-10, 0): 
            try:
                print(data[i]['name'] + ": " + data[i]['text'] + "\n")
            except IndexError:
                continue

    def send(self, text):
        name = self.name
        text = text

        res = requests.post('https://fartuh.xyz/api/chat/index.php', data = {"text":text, "name":name}) 

        if res.json()['result'] == True:
            os.system('cls' if os.name=='nt' else 'clear')
            self.load()
        else:
            print('Ошибка. Перезапустите клиент')

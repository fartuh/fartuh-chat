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

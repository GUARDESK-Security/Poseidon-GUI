import PySimpleGUI as sg
import requests
import urllib
import json
import time
sg.theme("Dark Purple")
layout = [[sg.Text("Poseidon")],
         [sg.Text("Made by GUARDESK Security LTD.")],
         [sg.Text("Insert URL to scan:")],
         [sg.InputText()],
         [sg.Submit(), sg.Cancel()]
         ]
window = sg.Window(title="Poseidon Malicious URL Scanner", layout=layout, margins=(100,150))
url = window.read()[1][0]
encoded_url = urllib.parse.quote(url, safe='')
api_url = "https://ipqualityscore.com/api/json/url/6iP3Ci09b83suqDijoQ4pHSD9uayadBp/"
data = requests.get(api_url + encoded_url)
sg.Print("Poseidon")
sg.Print(json.dumps(data.json(), indent=4))
time.sleep(30)
window.close()

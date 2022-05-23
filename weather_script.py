import requests

wttr_sheremetyevo = 'https://wttr.in/Шереметьево'
wttr_london = 'https://wttr.in/Лондон'
wttr_cherepovets = 'https://wttr.in/Череповец'

params = {'lang': 'ru', 'n': '', 'T': '', 'q': ''}

response_lon = requests.get(wttr_london, params=params)
response_che = requests.get(wttr_cherepovets, params=params)
response_svo = requests.get(wttr_sheremetyevo, params=params)

print(response_che.text)
print(response_lon.text)
print(response_svo.text)


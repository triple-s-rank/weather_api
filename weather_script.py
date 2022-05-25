import requests

wttr_sheremetyevo = 'https://wttr.in/Шереметьево'
wttr_london = 'https://wttr.in/Лондон'
wttr_cherepovets = 'https://wttr.in/Череповец'

params = {'lang': 'ru', 'n': '', 'T': '', 'q': ''}

weather_response_list = [
	requests.get(wttr_london, params=params),
	requests.get(wttr_cherepovets, params=params),
	requests.get(wttr_sheremetyevo, params=params),
]

for response in weather_response_list:
	print(response.text)


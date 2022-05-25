import requests

places_list = [
	'https://wttr.in/Шереметьево',
	'https://wttr.in/Лондон',
	'https://wttr.in/Череповец',
]

params = {'lang': 'ru', 'n': '', 'T': '', 'q': ''}

for place in places_list:
	print(requests.get(place, params=params).text)




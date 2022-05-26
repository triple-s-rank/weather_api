import requests

places_list = [
	'https://wttr.in/Шереметьево',
	'https://wttr.in/Лондон',
	'https://wttr.in/Череповец',
]

params = {'lang': 'ru', 'n': '', 'T': '', 'q': '', 'm': ''}


def request_weather(sequence):
	for place in sequence:
		response = requests.get(place, params=params)
		response.raise_for_status()
		print(response.text)


def main():
	try:
		request_weather(places_list)
	except requests.exceptions.HTTPError as error:
		print('Http error', error)


if __name__ == '__main__':
	main()
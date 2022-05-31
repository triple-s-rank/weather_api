import requests

WTTR_URL = 'https://wttr.in/'

params = {'lang': 'ru', 'n': '', 'T': '', 'q': '', 'm': ''}
map_points = ['Шереметьево', 'Лондон', 'Череповец']

def main(places):
	try:
		for place in places:
			url = WTTR_URL + place
			response = requests.get(url, params=params)
			response.raise_for_status()
			print(response.text)
	except requests.exceptions.HTTPError as error:
		print('Http error', error)

if __name__ == '__main__':
	main(map_points)
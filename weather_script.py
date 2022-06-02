import requests

WTTR_URL = 'https://wttr.in/'

params = {'lang': 'ru', 'n': '', 'T': '', 'q': '', 'm': ''}
map_points = ['Шереметьево', 'Лондон', 'Череповец']

def main(places: list) -> list:

	""" Returns list of request.Response objects with weather of places passed as arguments """

	responses = []
	try:
		for place in places:
			url = WTTR_URL + place
			response = requests.get(url, params=params)
			response.raise_for_status()
			responses.append(response)
		return responses
	except requests.exceptions.HTTPError as error:
		print('Http error', error)

if __name__ == '__main__':
	for response in main(map_points):
		print(response.text)
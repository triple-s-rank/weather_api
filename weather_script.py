import requests

WTTR_URL = 'https://wttr.in/'

def main():
	params = {'lang': 'ru', 'n': '', 'T': '', 'q': '', 'm': ''}
	places = ['Шереметьево', 'Лондон', 'Череповец']
	try:
		for place in places:
			url = WTTR_URL + place
			response = requests.get(url, params=params)
			response.raise_for_status()
			return (response.text)
	except requests.exceptions.HTTPError as error:
		return('Http error', error)

if __name__ == '__main__':
	print(main())
import requests

map_points = ['Шереметьево', 'Лондон', 'Череповец']

def get_weather_forecast(place):
	params = {'lang': 'ru', 'n': '', 'T': '', 'q': '', 'm': ''}
	try:
		response = requests.get(url=f"https://wttr.in/{place}", params=params)
		response.raise_for_status()
		return response.text
	except requests.HTTPError:
		print("Вы ввели неправильную ссылку.")

if __name__ == '__main__':
	for map_point in map_points:
		print(get_weather_forecast(map_point))
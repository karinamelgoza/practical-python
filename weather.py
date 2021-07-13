import requests

# temperature = 79
# forecast = 'sunny'

# if temperature > 80:
#     print("It's too hot!")
#     print('Stay inside!')
# print('Have a good day!')

# if temperature > 80:
#     print("It's too hot!")
#     print('Stay inside!')
# else:
#     print('Have a good day!')

# if temperature > 80:
#     print("It's too hot!")
#     print('Stay inside!')
# elif temperature < 60:
#     print("It's too cold!")
#     print('Stay inside!')
# else:
#     print('Have a good day!')

# if temperature > 80 or temperature < 60:
#     print('Stay inside!')
# else:
#     print('Enjoy the outdoors!')

# if temperature < 80 and forecast != 'rain':
#     print('Go outside!')
# else:
#     print('Stay inside!')

# if not forecast == 'rain':
#     print('Go outside!')
# else:
#     print('Stay inside!')

# raining = True

# if raining:
#     print('Stay inside!')
# else:
#     print('Go outside!')

# if not raining:
#     print("Go outside!")
# else:
#     print('Stay inside!')


def get_weather():
    api_key = '41b2db9fd68c3757aef081c537457543'
    city = 'Phoenix'
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + \
        city+'&appid=' + api_key + '&units=imperial'

    request = requests.get(url)
    json = request.json()
    # print(json)

    description = json.get('weather')[0].get('description')
    temp_min = json.get('main').get('temp_min')
    temp_max = json.get('main').get('temp_max')

    return {
        'description': description,
        'temp_min': temp_min,
        'temp_max': temp_max
    }


def main():
    # print the results
    weather_dictionary = get_weather()
    print("Today's forecast is", weather_dictionary.get('description'))
    print('The minimum temp is', weather_dictionary.get('temp_min'))
    print('The maximum temp is', weather_dictionary.get('temp_max'))


main()

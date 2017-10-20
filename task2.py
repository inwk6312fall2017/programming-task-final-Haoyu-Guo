from weather import Weather

def myweather(city):
    weather = Weather()
    location = weather.lookup_by_location(city)
    condition = location.condition()
    temp = condition.get('temp')
    to_forcast = location.forecast()

    for i in to_forcast:
        print ('highest temperature date:' % i['date'])
        print('highest temperature:' % i['high'])
        print('lowest temperature:' % i['low'])

from django.shortcuts import render
# import json to load json data to python dictionary
import json
#urllib.request ro make request to api
import urllib.request

# Create your views here.
def index(request):
    if request.method == "POST":
        city = request.POST['city']
        api_key = '7691ce9c9dec667d84991652df1ba5e8'

        # construct url
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        # Making q request from the api
        source = urllib.request.urlopen(url).read()
        #convert json data to dictionary
        list_of_data = json.loads(source)

        #Extracting the data from the dictionary
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                          + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp']) + 'k',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)



import requests
# Here apikey is given and we are looking at social network movie data
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
r = requests.get(url)
json_data = r.json()

for key, value in json_data.items():
    print(key+":",value)

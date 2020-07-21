import requests
import json

url = "https://developers.zomato.com/api/v2.1/cities"
response = requests.get(url)


zomato = json.loads(response.text)
for i in range(0, len(zomato)):
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print(zomato)

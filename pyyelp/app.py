import requests
from pathlib import Path


url = "https://api.yelp.com/v3/businesses/search"
api_key = Path("api.key").read_text()
headers = {
    "Authorization": "Bearer " + api_key

}
params = {
    "term": "Barber",
    "location": "NYC",
}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]

names = [business["name"] for business in businesses if business["rating"] > 4.5]
print(names)

for business in businesses:
    print(business["name"])




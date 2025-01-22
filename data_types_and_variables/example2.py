import requests

# Get weather from wttr.in
city = "Berlin"
url = f"https://wttr.in/{city}?format=3"

response = requests.get(url)
print(response.text)

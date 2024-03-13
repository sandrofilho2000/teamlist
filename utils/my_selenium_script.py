import requests

url = "https://api-football-v1.p.rapidapi.com/v3/teams"

querystring = {"search":"Vasco"}

headers = {
	"X-RapidAPI-Key": "a1c3643727msh420f41a993ae281p14b3acjsnd3fa2053f28f",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json()["response"][0])
import requests

NUMBER_QUESTIONS = 10
TYPE_QUESTIONS = "boolean"

params = {
    "amount": NUMBER_QUESTIONS,
    "type": TYPE_QUESTIONS,
}

response = requests.get(url="https://opentdb.com/api.php", params=params)
response.raise_for_status()
data = response.json()
question_data = data["results"]
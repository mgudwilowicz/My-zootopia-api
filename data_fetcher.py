import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

url = "https://api.api-ninjas.com/v1/animals?name="

headers = {
    "X-Api-Key": api_key,
    "Content-Type": "application/json"
}



def fetch_data(animal_name):
    response = requests.get(url + animal_name, headers=headers)
    data = response.json()
    print(data)

fetch_data('fox')
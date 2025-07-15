import random

import requests
from config.config import BASE_URL, HEADERS

BASE_URL = "https://petstore.swagger.io/v2"

def add_pet(pet_data):
    response = requests.post(f"{BASE_URL}/pet", json=pet_data, headers=HEADERS)
    return response

def get_pet(pet_id):
    url = f"{BASE_URL}/pet/{pet_id}"
    response = requests.get(url, headers=HEADERS)
    return response

def update_pet(pet_data):
    url = f"{BASE_URL}/pet"
    return requests.put(url, json=pet_data, headers=HEADERS)

def delete_pet(pet_id):
    return requests.delete(f"{BASE_URL}/pet/{pet_id}")
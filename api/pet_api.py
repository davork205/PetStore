import requests
from config.config import BASE_URL, HEADERS

def add_pet(pet_data):
    response = requests.post(f"{BASE_URL}/pet", json=pet_data, headers=HEADERS)
    return response

def get_pet(pet_id):
    response = requests.get(f"{BASE_URL}/pet/{pet_id}", headers=HEADERS)
    return response

def update_pet(pet_data):
    response = requests.put(f"{BASE_URL}/pet", json=pet_data, headers=HEADERS)
    return response
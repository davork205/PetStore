import time

from api.pet_api import add_pet
from utils.data_generator import generate_pet_data

def test_add_pet():
    pet_data = generate_pet_data()
    response = add_pet(pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == pet_data["name"]


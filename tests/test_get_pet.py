from api.pet_api import add_pet, get_pet
from utils.data_generator import generate_pet_data
import time

def test_get_pet_by_id():
    pet_data = generate_pet_data()
    print("Generated pet data:", pet_data)

    add_response = add_pet(pet_data)
    print("Add pet response status:", add_response.status_code)
    print("Add pet repsonse body:", add_response.text)
    assert add_response.status_code == 200

    time.sleep(1)

    get_response = get_pet(pet_data["id"])
    print("Get pet response status:", get_response.status_code)
    print("Get pet repsonse body:", get_response.text)
    assert get_response.status_code == 200
    assert get_response.json()["id"] == pet_data["id"]
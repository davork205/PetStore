from api.pet_api import add_pet, get_pet, delete_pet
from utils.data_generator import generate_pet_data
import time

def test_delete_pet():
    pet_data = generate_pet_data()
    add_response = add_pet(pet_data)
    assert add_response.status_code == 200

    delete_response = delete_pet(pet_data["id"])
    print("Delete response:", delete_response.status_code, delete_response.text)
    assert delete_response.status_code == 200

    time.sleep(1)
    get_response = get_pet(pet_data["id"])
    print("Get after delete:", get_response.status_code, get_response.text)
    assert get_response.status_code == 404
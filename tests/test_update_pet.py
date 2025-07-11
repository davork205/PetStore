from api.pet_api import add_pet, update_pet, get_pet
from utils.data_generator import generate_pet_data

def test_update_pet():
    pet_data = generate_pet_data()
    add_response = add_pet(pet_data)
    assert add_response.status_code == 200

    pet_data["name"] = "Max"
    update_response = update_pet(pet_data)
    assert update_response.status_code == 200

    get_response = get_pet(pet_data["id"])
    assert get_response.json()["name"] == "Max"
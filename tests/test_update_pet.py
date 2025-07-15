from api.pet_api import add_pet, update_pet, get_pet
from utils.data_generator import generate_pet_data

def test_update_pet():
    pet_data = generate_pet_data()
    add_response = add_pet(pet_data)
    assert add_response.status_code == 200

    print("Original pet:", pet_data)

    updated_pet = pet_data.copy()
    updated_pet["name"] = "Max"

    update_response = update_pet(updated_pet)
    print("Update response:", update_response.status_code, update_response.text)
    assert update_response.status_code == 200

    get_response = get_pet(pet_data["id"])
    print("Get after update status:", get_response.status_code)
    print("Get after update body:", get_response.text)

    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Max"
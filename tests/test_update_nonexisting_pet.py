import pytest
from api.pet_api import update_pet
import random

@pytest.mark.skip(reason="Cannot work currently")
def test_update_nonexisting_pet():
    non_existing_pet_id = random.randint(999999, 9999999)

    update_pet_data = {
        "id": non_existing_pet_id,
        "name": "SomePet",
        "photoUrls": [],
        "status": "available"
    }

    response = update_pet(update_pet_data)

    print("Update response", response.status_code, response.text)

    assert response.status_code in [200, 404, 400]
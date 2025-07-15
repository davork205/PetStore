import pytest
from api.pet_api import get_pet
import random

def test_get_nonexistent_pet():
    invalid_pet_id = random.randint(999999, 9999999)

    response = get_pet(invalid_pet_id)

    assert response.status_code == 404
    assert "Pet not found" in response.text
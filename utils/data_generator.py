import random

def generate_pet_data():
    pet_id = random.randint(1000, 9999)
    return{
        "id": pet_id,
        "category": {"id": 1, "name": "Dogs"},
        "name": "Max",
        "photoUrls": ["https://example.com/photo.jpg"],
        "tags": [{"id": 1, "name": "fiendly"}],
        "status": "available"
    }
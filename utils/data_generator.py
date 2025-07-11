import random

def generate_pet_data(pet_id=None):
    return {
        "id": pet_id or random.randint(1000, 9999),
        "name": "Buddy",
        "photoUrls": ["https://example.com/photo.jpg"],
        "status": "available"
    }
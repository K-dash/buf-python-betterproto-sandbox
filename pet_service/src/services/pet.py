from gen.pet.v1 import (
    PetStoreServiceBase,
    GetPetRequest,
    GetPetResponse,
    Pet,
    PetType,
)
from gen.google.type import DateTime

class PetServiceImpl(PetStoreServiceBase):
    async def get_pet(self, get_pet_request: GetPetRequest) -> GetPetResponse:
        print(f"get_pet: {get_pet_request.pet_id}")

        dummy_pet = Pet(
            pet_id="1",
            pet_type=PetType(PetType.DOG),
            name="Buddy",
            created_at=DateTime(year=2021, month=8, day=1, hours=12),
        )
        return GetPetResponse(pet=dummy_pet)

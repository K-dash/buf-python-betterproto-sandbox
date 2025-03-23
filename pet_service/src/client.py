import asyncio
from grpclib.client import Channel

from gen.pet.v1 import (
    PetStoreServiceStub,
    GetPetRequest,
)


async def client(host: str = "127.0.0.1", port: int = 50051) -> None:
    channel = Channel(host, port)
    service = PetStoreServiceStub(channel)
    response = await service.get_pet(GetPetRequest(pet_id="123"))
    print(response)
    channel.close()


if __name__ == "__main__":
    asyncio.run(client())

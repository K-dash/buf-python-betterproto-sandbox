from grpclib.server import Server
from services.pet import PetServiceImpl
import asyncio


async def start_server(host: str = "127.0.0.1", port: int = 50051) -> None:
    server = Server([PetServiceImpl()])
    await server.start(host, port)
    await server.wait_closed()

if __name__ == "__main__":
    asyncio.run(start_server())

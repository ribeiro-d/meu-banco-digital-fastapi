from fastapi import status
from httpx import AsyncClient
import pytest_asyncio


@pytest_asyncio.fixture(autouse=True)
async def popular_contas(db):
    from src.schemas.conta import ContaIn
    from src.services.conta import ContaService
    
    service = ContaService()
    await service.criar_conta(ContaIn(user_id=1))
    await service.criar_conta(ContaIn(user_id=2))
    await service.criar_conta(ContaIn(user_id=3, saldo=1000))
    

async def test_listar_contas_success(client: AsyncClient, access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"limit": 10}
    
    response = await client.get("/contas/", headers=headers, params=params)
    
    content = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert len(content) == 3


async def test_listar_contas_authentication_fail(client: AsyncClient):
    response = await client.get("/contas/")
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
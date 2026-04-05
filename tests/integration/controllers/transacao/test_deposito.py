from fastapi import status
from httpx import AsyncClient
import pytest_asyncio


@pytest_asyncio.fixture(autouse=True)
async def criar_conta(db):
    from src.schemas.conta import ContaIn
    from src.services.conta import ContaService
    
    service = ContaService()
    await service.criar_conta(ContaIn(user_id=1, saldo=500))


async def test_deposito_success(client: AsyncClient, access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {
        "conta_id": 1,
        "valor": 200
    }

    response = await client.post("/transacoes/deposito/", json=data, headers=headers)

    content = response.json()

    assert response.status_code == status.HTTP_201_CREATED
    assert content is not None
    

async def test_deposito_invalid_payload_fail(client: AsyncClient, access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"conta_id": 1}
    
    response = await client.post("/transacoes/deposito/", json=data, headers=headers)
    
    content = response.json()
    
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    assert content["detail"][0]["loc"] == ["body", "valor"]
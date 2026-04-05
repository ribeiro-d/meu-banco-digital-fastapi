from fastapi import status
from httpx import AsyncClient


async def test_criar_conta_success(client: AsyncClient, access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    data = {"user_id": 1}
    
    response = await client.post("/contas/", json=data, headers=headers)
    
    content = response.json()
    
    assert response.status_code == status.HTTP_201_CREATED
    assert content is not None


async def test_criar_conta_invalid_payload_fail(client: AsyncClient, access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    
    response = await client.post("/contas/", headers=headers, json={})
    
    content = response.json()
    
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_CONTENT
    assert content["detail"][0]["loc"] == ["body", "user_id"]
    
    
async def test_criar_conta_authentication_fail(client: AsyncClient):
    data = {"user_id": 1}
    
    response = await client.post("/contas/", json=data, headers={})
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
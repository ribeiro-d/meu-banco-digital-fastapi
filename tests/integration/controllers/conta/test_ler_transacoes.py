from fastapi import status
from httpx import AsyncClient
import pytest_asyncio


@pytest_asyncio.fixture(autouse=True)
async def criar_conta_e_transacoes(db):
    from src.schemas.conta import ContaIn
    from src.schemas.transacao import Saque, Deposito
    from src.services.conta import ContaService
    from src.services.transacao import TransacaoService
    
    service = ContaService()
    ts_service = TransacaoService()
    
    await service.criar_conta(ContaIn(user_id=1, saldo=1000))
    await ts_service.adicionar_transacao(Deposito(conta_id=1, valor=200))
    await ts_service.adicionar_transacao(Saque(conta_id=1, valor=300))
    await ts_service.adicionar_transacao(Saque(conta_id=1, valor=100))
    

async def test_ler_transacoes_success(client: AsyncClient, access_token: str):
    headers = {"Authorization": f"Bearer {access_token}"}
    conta_id = 1
    
    response = await client.get(f"/contas/{conta_id}", headers=headers)
    
    content = response.json()
    
    assert response.status_code == status.HTTP_200_OK
    assert len(content) == 3
    

async def test_ler_transacoes_authentication_fail(client: AsyncClient):
    conta_id = 1
    response = await client.get(f"/contas/{conta_id}")
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    

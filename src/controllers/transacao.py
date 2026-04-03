from fastapi import APIRouter, Depends, status

from src.security import login_required
from src.schemas.transacao import Saque, Deposito
from src.views.transacao import TransacaoOut
from src.services.transacao import TransacaoService


router = APIRouter(prefix="/transacoes", dependencies=[Depends(login_required)])

service = TransacaoService()

@router.post("/saque/",status_code=status.HTTP_201_CREATED ,response_model=TransacaoOut)
async def adicionar_saque(transacao: Saque):
    return await service.adicionar_transacao(transacao=transacao)

@router.post("/deposito/", status_code=status.HTTP_201_CREATED, response_model=TransacaoOut)
async def adicionar_deposito(transacao: Deposito):
    return await service.adicionar_transacao(transacao=transacao)
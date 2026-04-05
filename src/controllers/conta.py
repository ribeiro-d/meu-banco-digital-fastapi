from fastapi import APIRouter, Depends, status

from src.security import login_required
from src.schemas.conta import ContaIn
from src.views.conta import ContaOut
from src.views.transacao import TransacaoOut
from src.services import conta, transacao

router = APIRouter(prefix="/contas", dependencies=[Depends(login_required)])

service = conta.ContaService()
transacao_service = transacao.TransacaoService()


@router.get("/", response_model=list[ContaOut])
async def listar_contas(limit: int, skip: int = 0):
    return await service.listar_contas(limit=limit, skip=skip)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ContaOut)
async def criar_conta(conta: ContaIn):
    return await service.criar_conta(conta)
    

@router.get("/{conta_id}", response_model=list[TransacaoOut])
async def ler_transacoes(conta_id: int, limit: int = 10, skip: int = 0):
    return await transacao_service.ler_historico(conta_id=conta_id, limit=limit, skip=skip)
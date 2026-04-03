from fastapi import HTTPException, status
from databases.interfaces import Record
from decimal import Decimal

from src.database import database
from src.models.conta import contas
from src.schemas.transacao import Transacao
from src.models.transacao import transacoes


class TransacaoService:
    async def ler_historico(self, conta_id: int, limit: int, skip: int = 0) -> list[Record]:
        query = transacoes.select().where(transacoes.c.conta_id == conta_id).limit(limit).offset(skip)
        return await database.fetch_all(query)


    @database.transaction()
    async def adicionar_transacao(self, transacao: Transacao) -> Record:
        query = contas.select().where(contas.c.id == transacao.conta_id)
        conta = await database.fetch_one(query)

        if not conta:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Conta não encontrada")

        valor_invalido = transacao.valor <= 0
        saldo_insuficiente = transacao.valor > conta.saldo

        if valor_invalido:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Valor inválido")
        if saldo_insuficiente:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Saldo insuficiente")

        tipo = transacao.__class__.__name__
        if tipo == "Saque":
            novo_saldo = conta.saldo - Decimal(transacao.valor)
        else:
            novo_saldo = conta.saldo + Decimal(transacao.valor)

        await self.__atualizar_saldo(transacao.conta_id, novo_saldo)
        id_transacao = await self.__registrar_transacao(transacao)

        query = transacoes.select().where(transacoes.c.id == id_transacao)
        return await database.fetch_one(query)


    async def __atualizar_saldo(self, conta_id: int, novo_saldo: float) -> None:
        query = contas.update().where(contas.c.id == conta_id).values(saldo=novo_saldo)
        return await database.execute(query)


    async def __registrar_transacao(self, transacao: Transacao) -> int:
        query = transacoes.insert().values(
            tipo=transacao.__class__.__name__,
            valor=transacao.valor,
            conta_id=transacao.conta_id
        )
        return await database.execute(query)

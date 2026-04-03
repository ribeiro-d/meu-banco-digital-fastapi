from fastapi import HTTPException, status
from databases.interfaces import Record

from src.database import database
from src.schemas.conta import ContaIn
from src.models.conta import contas


class ContaService:
    async def listar_contas(self, limit: int, skip: int = 0) -> list[Record]:
        query = contas.select().limit(limit).offset(skip)
        return await database.fetch_all(query)

    async def criar_conta(self, conta: ContaIn) -> Record:
        command = contas.insert().values(user_id=conta.user_id, saldo=conta.saldo)
        conta_id = await database.execute(command)
        
        query = contas.select().where(contas.c.id == conta_id)
        return await database.fetch_one(query)
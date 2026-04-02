from pydantic import BaseModel


class ContaCorrenteIn(BaseModel):
    id: int
    nome: str
    agencia: str
    saldo: float = 0

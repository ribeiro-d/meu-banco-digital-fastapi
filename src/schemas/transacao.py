from datetime import datetime

from pydantic import BaseModel


class Transacao(BaseModel):
    conta_id: int


class Saque(Transacao):
    valor: float


class Deposito(Transacao):
    valor: float

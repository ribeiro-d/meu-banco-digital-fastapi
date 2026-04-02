from datetime import datetime

from pydantic import BaseModel


class Transacao(BaseModel):
    id: int


class SaqueIn(Transacao):
    value: float
    date: datetime = datetime.now()


class DepositoIn(Transacao):
    value: float
    date: datetime = datetime.now()

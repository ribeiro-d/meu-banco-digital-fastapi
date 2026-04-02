from pydantic import BaseModel
from transacao import Transacao


class Historico(BaseModel):
    historico: list[Transacao]

from pydantic import BaseModel, AwareDatetime, NaiveDatetime


class ContaOut(BaseModel):
    id: int
    user_id: int
    saldo: float
    data_criacao: AwareDatetime | NaiveDatetime

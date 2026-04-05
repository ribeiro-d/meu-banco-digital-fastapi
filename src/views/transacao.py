from pydantic import BaseModel, AwareDatetime, NaiveDatetime


class TransacaoOut(BaseModel):
    id: int
    conta_id: int
    tipo: str
    valor: float
    data: AwareDatetime | NaiveDatetime
from pydantic import BaseModel, AwareDatetime


class TransacaoOut(BaseModel):
    id: int
    conta_id: int
    tipo: str
    valor: float
    data: AwareDatetime
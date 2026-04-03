from pydantic import BaseModel


class ContaIn(BaseModel):
    user_id: int
    saldo: float = 0

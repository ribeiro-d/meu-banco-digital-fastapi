from src.database import metadata
import sqlalchemy as sa
from .conta import contas

historico = sa.Table(
    "historico",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("conta", sa.ForeignKey(contas.c.id))
)

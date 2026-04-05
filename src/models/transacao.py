from src.database import metadata
import sqlalchemy as sa
from .conta import contas

transacoes = sa.Table(
    "transacoes",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("tipo", sa.String, nullable=False),
    sa.Column("valor", sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column("data", sa.DateTime, default=sa.func.now(), nullable=False),
    sa.Column("conta_id", sa.Integer, sa.ForeignKey("contas.id"), nullable=False),
)

from src.database import metadata
import sqlalchemy as sa

transacoes = sa.Table(
    "transacoes",
    metadata=metadata,
)

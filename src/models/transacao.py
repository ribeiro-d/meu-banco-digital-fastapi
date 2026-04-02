from src.database import metadata
import sqlalchemy as sa

transacoes = sa.Table(
    "transacoes",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("type", sa.String, nullable=False)
)

from src.database import metadata
import sqlalchemy as sa

contas = sa.Table(
    "contas",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_id", sa.Integer, nullable=False),
    sa.Column("saldo", sa.Numeric(precision=10, scale=2), default=0, nullable=False),
    sa.Column("data_criacao", sa.TIMESTAMP(timezone=True), default=sa.func.now())
)

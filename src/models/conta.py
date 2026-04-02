from src.database import metadata
import sqlalchemy as sa

contas = sa.Table(
    "contas",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("type", sa.String, nullable=False)
)

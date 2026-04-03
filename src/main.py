from fastapi import FastAPI
from src.controllers import transacao, conta, auth
from src.database import database, metadata, engine


async def lifespan(app: FastAPI):
    from src.models import conta, transacao
    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()


app = FastAPI(title="Meu Banco Digital", lifespan=lifespan)

app.include_router(transacao.router)
app.include_router(conta.router)
app.include_router(auth.router)
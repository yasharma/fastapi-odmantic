from fastapi import Depends, FastAPI

from core.deps import EngineDep
from models.Todo import Todo

app = FastAPI()


@app.post("/")
async def create(item: Todo, engine: EngineDep) -> Todo:
    result = await engine.save(item)
    return result

@app.get("/")
async def read(engine: EngineDep):
    todos = await engine.find(Todo)
    return todos


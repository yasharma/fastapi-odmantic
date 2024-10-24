from fastapi import Depends, FastAPI

from core.deps import EngineDep
from models.Todo import Todo, PatchTodoSchema
from odmantic import ObjectId

app = FastAPI()


@app.post("/")
async def create(item: Todo, engine: EngineDep) -> Todo:
    result = await engine.save(item)
    return result

@app.get("/")
async def read(engine: EngineDep):
    todos = await engine.find(Todo)
    return todos

@app.put("/{id}")
async def update(engine: EngineDep, item: PatchTodoSchema, id: ObjectId):
    todo = await engine.find_one(Todo, Todo.id == id)
    if todo:
        update_data = item.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(todo, key, value)
        await engine.save(todo)
        return todo
    return {"error": "Todo not found"}

@app.delete("/{id}")
async def delete(engine: EngineDep, id: ObjectId):
    todo = await engine.remove(Todo, Todo.id == id)
    return todo
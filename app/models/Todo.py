from odmantic import Model, Field
from datetime import datetime, timezone
from typing import Optional
from pydantic import BaseModel
class Todo(Model):
    title: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed: bool = False

class PatchTodoSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None
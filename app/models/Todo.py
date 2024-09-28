from odmantic import Model, Field
from datetime import datetime, timezone
from typing import Optional

class Todo(Model):
    title: str
    description: Optional[str] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed: bool = False
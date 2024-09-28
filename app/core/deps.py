from typing import Annotated

from fastapi import Depends
from odmantic import AIOEngine

from core.database import get_engine


EngineDep = Annotated[AIOEngine, Depends(get_engine)]
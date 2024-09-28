from pydantic import BaseModel
import os
import logging

# Initialize logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Config')

class Config(BaseModel):
  dbUrl: str
  production: bool


# Load configuration from environment variables
def load_config():
  db_url = os.getenv('DATABASE_URL')
  if not db_url:
    raise EnvironmentError("DATABASE_URL environment variable is required.")
  
  config = Config(
    dbUrl=db_url,
    port=os.getenv('PORT', 80),
    production=os.getenv('PRODUCTION', False)
  )
  logger.info('for the app: %s', config.model_dump_json())
  return config

try:
  config = load_config()
except EnvironmentError as e:
  logger.error(e)
  raise SystemExit(e)
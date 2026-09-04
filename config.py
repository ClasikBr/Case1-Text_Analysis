from pydantic import BaseSettings


class Settings(BaseSettings):
  REDIS_URL: str = 'redis://redis:6379/0'
  CACHE_TTL: int = 3600
  MAX_TEXT_SIZE: int = 20000
  LOG_LEVEL: str = 'INFO'

  class Config:
    env_file = '.env'


settings = Settings()

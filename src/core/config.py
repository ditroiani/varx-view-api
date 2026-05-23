from pydantic_settings import BaseSettings
from functools import lru_cache
 
class Settings(BaseSettings):
    """
    Configuracoes da aplicacao.
    Os valores sao lidos automaticamente do arquivo .env.
    """
    APP_NAME: str = "VarX View API"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = False
    DATABASE_URL: str = ""
    SECRET_KEY: str = ""
 
    class Config:
        env_file = ".env"
        case_sensitive = False
 
 
@lru_cache() # Definição de cache para ser criado uma unica vez a instância desta classe
def get_settings() -> Settings:
    """
    Retorna as configuracoes em cache.
    lru_cache garante que o .env e lido apenas uma vez.
    """
    return Settings()
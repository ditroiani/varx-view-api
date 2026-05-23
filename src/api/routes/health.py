from fastapi import APIRouter
from datetime import datetime, timezone
from src.core.config import get_settings

router = APIRouter(
    tags=["Health"]
)
settings = get_settings()

@router.get("/health")
async def health_check():
    """
    Verifica se a API esta operacional.
 
    Retorna status, versao e timestamp atual.
    Usado por sistemas de monitoramento e plataformas de deploy.
    """

    return {
        "status": "healthy",
        "servico": settings.APP_NAME,
        "versao": settings.APP_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "ambiente": "development" if settings.DEBUG else "production",
    }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.core.config import get_settings
from src.api.routes import health, audience, devices

# Get Settings
settings = get_settings()

app = FastAPI (
    title=settings.APP_NAME,
    description="""
    ## Smart Retail Analytics API

    API de analise anonima de audiencia para ambientes comerciais.
    Processa dados de cameras localmente e expoe KPIs via endpoints REST.

    ### Funcionalidades
    - Ingestao de dados de audiencia do Agent
    - Consulta de KPIs por periodo
    - Distribuicao de fluxo por hora
    - Autenticacao por API Key

    Privacidade: Zero imagens armazenadas. 100 LGPD-compliant.
    """,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc", 
)

# CORS — permite que o dashboard web acesse a API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em producao: especificar dominios
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# Registrar rotas
app.include_router(health.router, tags=["Health"])
app.include_router(audience.router, prefix="/audience", tags=["Audience"])
app.include_router(devices.router, prefix="/devices", tags=["Devices"])

@app.get("/", include_in_schema=False)
async def root():
    return {
        "produto": "VarX View API",
        "versao": settings.app_version,
        "docs": "/docs",
        "status": "online",
    }
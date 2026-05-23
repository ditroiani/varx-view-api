from fastapi import APIRouter
from pydantic import BaseModel
import uuid

router = APIRouter()

class DeviceRegisterRequest(BaseModel):
    nome: str
    localizacao: str
    client_id: str
 
    model_config = {
        "json_schema_extra": {
            "example": {
                "nome": "Camera Entrada Loja",
                "localizacao": "Academia Smart Fit Paulista",
                "client_id": "client-0001",
            }
        }
    }

## REGISTER DEVICE
@router.post("/register", status_code=201)
async def register_device(payload: DeviceRegisterRequest):
    """
    Registra um novo device (Agent) no sistema.
 
    Retorna token de autenticacao e intervalo de sync configurado.
    O Agent usara esse token em todas as requisicoes subsequentes.
    """
    token = str(uuid.uuid4())
    return {
        "device_id": str(uuid.uuid4()),
        "token": token,
        "sync_interval_minutes": 1440,  # Padrao: plano Essencial (1x/dia)
        "mensagem": "Device registrado com sucesso (mock — banco na Semana 2)",
    }
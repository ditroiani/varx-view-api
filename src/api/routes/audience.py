from fastapi import APIRouter, Query
from datetime import datetime, timezone
from typing import Literal

router = APIRouter()

## LIVE AUDIENCE
@router.get("/live")
async def get_live_audience():
    """
    Retorna a contagem de pessoas detectadas em tempo real.
    """
    return {
        "pessoas_detectadas": 3,
        "engajamento_pct": 0.67,
        "ultima_atualizacao": datetime.now(timezone.utc).isoformat(),
        "device_id": "ambiente-device-001",
        "nota": "Dados simulados — banco sera conectado posterirmente",
    }

## GET STATS AUDIENCE
@router.get("/stats")
async def get_audience_stats(
    period: Literal["today", "week", "month"] = Query(
        default="today",
        description="Periodo de consulta: today, week ou month",
    )
):
    """
    Retorna KPIs agregados de audiencia do periodo selecionado.
    """
    return {
        "periodo": period,
        "total_pessoas": 142,
        "media_por_hora": 14.2,
        "hora_pico": "10:00",
        "engajamento_medio_pct": 0.54,
        "perfil_predominante": {
            "faixa_etaria": "25-35",
            "genero_estimado": "M",
        },
        "nota": "Dados simulados — banco sera conectado posteriormente",
    }

@router.get("/hourly")
async def get_hourly_distribution():
    """
    Retorna distribuicao de fluxo hora a hora do dia atual.
    """
    horas = [
        {"hora": f"{h:02d}:00", "pessoas": v}
        for h, v in enumerate(
            [0, 0, 0, 0, 0, 2, 8, 15, 22, 18, 12, 14,
             16, 11, 9, 13, 19, 17, 10, 6, 4, 2, 1, 0]
        )
    ]
    return {"data": horas, "nota": "Dados simulados"}

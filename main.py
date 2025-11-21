from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import datetime
from mangum import Mangum

app = FastAPI(title="User Events API", version="1.0.0")

# Almacenamiento simple en memoria
events_storage = []


class CustomField(BaseModel):
    name: str
    value: Union[str, int, float]


class UserEvent(BaseModel):
    source: str
    event: str
    organization_slug: str
    user_id: int
    email: str
    name: str
    custom_fields: List[CustomField]


class UserEventWithTimestamp(UserEvent):
    timestamp: str


@app.post("/events", response_model=UserEventWithTimestamp, status_code=200)
async def create_event(event: UserEvent):
    """Crea un nuevo evento de usuario"""
    # Compatible con Pydantic v1 y v2
    event_dict = event.dict() if hasattr(event, 'dict') else event.model_dump()
    event_with_timestamp = UserEventWithTimestamp(
        **event_dict,
        timestamp=datetime.now().isoformat()
    )
    events_storage.append(event_with_timestamp)
    return event_with_timestamp


@app.get("/events", response_model=List[UserEventWithTimestamp])
async def get_events():
    """Obtiene todos los eventos almacenados"""
    return events_storage


@app.get("/health")
async def health():
    """Endpoint de health check"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/")
async def root():
    """Endpoint raíz"""
    return {
        "message": "User Events API",
        "endpoints": {
            "GET /health": "Verificar el estado de la API",
            "POST /events": "Crear un nuevo evento",
            "GET /events": "Obtener todos los eventos"
        }
    }


# Handler para Vercel usando Mangum
handler = Mangum(app)

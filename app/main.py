from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api_sources import fetch_all_sources
from app.processor import normalize_data, calculate_dii_score
from app.output import export_to_json

app = FastAPI()

# Servir archivos estáticos (CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Configurar el motor de plantillas Jinja2
templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def dashboard(request: Request):
    #  Extrae fuentes
    raw_data = fetch_all_sources()

    #	Calcular DII
    normalized = normalize_data(raw_data)
    enriched = [calculate_dii_score(entry) for entry in normalized]

    # Exporta JSON
    export_to_json(enriched)

    # Dashboard HTML
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "incidents": enriched
    })

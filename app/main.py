from fastapi import FastAPI
from app.routes import nappes, rivieres, gravite, meteo, messages, recommandations

app = FastAPI(title='API Sécheresse')

# Inclusion des routes
app.include_router(nappes.router)
app.include_router(rivieres.router)
app.include_router(gravite.router)
app.include_router(meteo.router)
app.include_router(messages.router)
app.include_router(recommandations.router)

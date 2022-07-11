from fastapi import FastAPI
from .imdb.routes.views import router as IMDBRouter
from .admin.routes.views import router as AdminRouter

app = FastAPI()
app.include_router(IMDBRouter, tags=["IMDB"], prefix="/imdb/movies")
app.include_router(AdminRouter, tags=["Admin"], prefix="/accounts")

@app.get("/", tags=["Base"])
async def read_root():
    return {"knock knock!!!": "Who's there..."}

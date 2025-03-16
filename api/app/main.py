from app.routes import router
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/", include_in_schema=False)
def home() -> RedirectResponse:
    return RedirectResponse("/docs")


app.include_router(router)

from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI(
        title="Ejercicio Integrador",
        description="Corazza",
        version="1.0.0"
    )

    return app

app = create_app()
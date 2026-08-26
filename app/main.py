from fastapi import FastAPI
from app.modules.producto.routers import router as producto_router
from app.modules.categoria.routers import router as categoria_router

def create_app() -> FastAPI:
    app = FastAPI(
        title="Ejercicio Integrador",
        description="Corazza",
        version="1.0.0"
    )

    app.include_router(producto_router)
    app.include_router(categoria_router)

    return app

app = create_app()
from pydantic import BaseModel, Field
from typing import Optional


class ProductoBase(BaseModel):
    nombre: str = Field(..., example="Escritorio")
    categoria: str = Field(..., pattern=r"^[A-Z]{3}-\d{2}$", example="ESC-01")
    precio: float = Field(gt=0, example=150.50)
    stock: int = Field(ge=0, example=20)
    stock_minimo: int = Field(ge=0, example=5)
    activo: bool = True


class ProductoCreate(ProductoBase):
    pass

class ProductoRead(ProductoBase):
    id: int

class ProductoStockResponse(BaseModel):
    stock: int
    bajo_stock_minimo: bool
    activo: bool
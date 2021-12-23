from typing import Optional

from pydantic import BaseModel
from pydantic import Field


class Product(BaseModel):
    codigo_producto: int
    iva_compra: int
    nit_proveedor: int
    nombre_producto: Optional[str] = Field(..., max_length=50)
    precio_compra: float
    precio_venta: float

    class Config:
        schema_extra = {
            "example": {
                "codigo_producto": 123456,
                "iva_compra": 16,
                "nit_proveedor": 12334455766,
                "nombre_producto": "cerveza",
                "precio_compra": 9876654,
                "precio_venta": 1324234
            }
        }

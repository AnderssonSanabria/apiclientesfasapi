def productEntity(item) -> dict:
    return {
        "codigo_producto": item["codigo_producto"],
        "iva_compra": item["iva_compra"],
        "nit_proveedor": item["nit_proveedor"],
        "nombre_producto": item["nombre_producto"],
        "precio_compra": item["precio_compra"],
        "precio_venta": item["precio_venta"]
    }


def productsEntity(entity) -> list:
    return [productEntity(item) for item in entity]

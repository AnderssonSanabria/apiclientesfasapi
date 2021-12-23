from fastapi.param_functions import Path
from models.modelProducts import Product
from fastapi import Body
from fastapi import status
from fastapi import APIRouter
from config.db import conn, db, col
from schemas.schemaProducts import productEntity, productsEntity
client = APIRouter()


@client.get('/productos', status_code=status.HTTP_200_OK, tags=['Consultar productos'])
async def getProducts():
    return productsEntity(col.find())


@client.get('/productos/{codigo_producto}', response_model=Product, status_code=status.HTTP_200_OK, tags=['Consultar productos'])
async def getProduct(codigo_producto: str = Path(...)):
    get_product = col.find_one({"codigo_producto": int(codigo_producto)})
    return productEntity(get_product)


@client.post('/productos', response_model=Product, status_code=status.HTTP_201_CREATED, tags=['Crear producto'])
async def setProduct(product: Product = Body(...)):
    new_product = dict(product)
    col.insert_one(new_product)
    col_product = col.find_one({"codigo_producto": product.codigo_producto})
    return productEntity(col_product)


@client.delete('/productos/{codigo_producto}', status_code=status.HTTP_200_OK, tags=['Eliminar producto'])
async def deleteProducts(codigo_producto: str = Path(...)):
    get_product = col.find_one({"codigo_producto": int(codigo_producto)})
    col.delete_one(get_product)
    return 'el producto con codigo numero {codigo_producto} se borro correctamente'.format(codigo_producto=codigo_producto)


@client.put('/productos', response_model=Product, status_code=status.HTTP_200_OK, tags=['Actualizar producto'])
async def updateProducts(product: Product = Body(...)):
    col.find_one_and_update(
        {"codigo_producto": int(product.codigo_producto)}, {"$set": dict(product)})
    get_product = col.find_one(
        {"codigo_producto": int(product.codigo_producto)})
    return get_product

from fastapi import FastAPI
from routes.routeProducts import client
app = FastAPI(
    title='RestApi products whit fastApi an MongoDB',
    description='This is a api for productos',
    version='0.1',
)

app.include_router(client)

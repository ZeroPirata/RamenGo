from fastapi import FastAPI
from .broths import broths_route
from .proteins import proteins_route
from .orders import orders_route


def define_routes(app: FastAPI):
    app.include_router(broths_route)
    app.include_router(proteins_route)
    app.include_router(orders_route)

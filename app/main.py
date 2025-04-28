from fastapi import FastAPI
from app.routes import user
from app.routes import product
from app.config.db import Base, engine

app = FastAPI()

# Create the tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(user.router)

app.include_router(product.router)
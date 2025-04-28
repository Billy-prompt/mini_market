from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.product import ProductOut, ProductCreate
from app.models.product import Product
from app.config.db import get_db
from typing import List


router = APIRouter(prefix='/product', tags=["Products"])


@router.get("/", response_model=List[ProductOut])
def get_users(db: Session = Depends(get_db)):
    return db.query(Product).all()


@router.post("/", response_model=ProductOut)
def create_product(user_data: ProductCreate, db: Session = Depends(get_db)):
    # Example implementation for creating a product
    product = Product(name=user_data.name, price=user_data.price, user_id=user_data.user_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    user_id: int

class ProductOut(BaseModel):
    id: int
    name: str
    price: float
    user_id: int

    class Config:
        orm_mode = True
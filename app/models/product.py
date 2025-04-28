from sqlalchemy import Column, Integer, String
from app.config.db import Base

class product(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100))
    precio = Column(Integer)
    stock = Column(Integer)
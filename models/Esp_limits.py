from config.database import Base
from sqlalchemy import Column,Integer,Float
from sqlalchemy.orm import relationship

class Esp_limits(Base):
    __tablename__ = "Esp_limits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    pres_limit = Column(Float, default=0)
    sensors = relationship("BMP180", back_populates="limits")

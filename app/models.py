from sqlalchemy import Column, Integer, String, Boolean, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from .db import Base


class Area(Base):
    __tablename__ = "areas"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    postcode_prefix = Column(String, nullable=True, index=True)
    city = Column(String, nullable=True, index=True)
    avg_income_monthly = Column(Integer, nullable=True)  # optional, for affordability analytics

    listings = relationship("Listing", back_populates="area", cascade="all, delete-orphan")


class Listing(Base):
    __tablename__ = "listings"

    id = Column(Integer, primary_key=True, index=True)

    area_id = Column(Integer, ForeignKey("areas.id"), nullable=False, index=True)

    title = Column(String, nullable=False, index=True)
    rent_pcm = Column(Integer, nullable=False, index=True)  # rent per calendar month
    bedrooms = Column(Integer, nullable=False, index=True)
    property_type = Column(String, nullable=False, index=True)  # flat/house/studio...
    furnished = Column(Boolean, nullable=False, default=False)
    available_from = Column(Date, nullable=True)

    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    area = relationship("Area", back_populates="listings")
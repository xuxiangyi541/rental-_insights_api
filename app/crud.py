from sqlalchemy.orm import Session
from . import models, schemas


def create_listing(db: Session, data: schemas.ListingCreate) -> models.Listing:
    listing = models.Listing(**data.model_dump())
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return listing


def get_listing(db: Session, listing_id: int) -> models.Listing | None:
    return db.query(models.Listing).filter(models.Listing.id == listing_id).first()


def list_listings(
    db: Session,
    area_id: int | None = None,
    max_rent: int | None = None,
    bedrooms: int | None = None,
    skip: int = 0,
    limit: int = 50,
) -> list[models.Listing]:
    q = db.query(models.Listing)
    if area_id is not None:
        q = q.filter(models.Listing.area_id == area_id)
    if max_rent is not None:
        q = q.filter(models.Listing.rent_pcm <= max_rent)
    if bedrooms is not None:
        q = q.filter(models.Listing.bedrooms == bedrooms)
    return q.offset(skip).limit(limit).all()


def update_listing(db: Session, listing: models.Listing, data: schemas.ListingUpdate) -> models.Listing:
    patch = data.model_dump(exclude_unset=True)
    for k, v in patch.items():
        setattr(listing, k, v)
    db.add(listing)
    db.commit()
    db.refresh(listing)
    return listing


def delete_listing(db: Session, listing: models.Listing) -> None:
    db.delete(listing)
    db.commit()
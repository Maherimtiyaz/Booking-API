from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models import Booking, FitnessClass
from app.schemas import BookingCreate, BookingResponse
from app.dependencies import get_current_user

router = APIRouter(prefix="/bookings", tags=["Bookings"])


# Create a new booking

@router.post("/")
def book_class(
    booking: BookingCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing = (
        db.query(Booking)
        .filter(Booking.user_id == current_user.id, Booking.class_id == booking.class_id)
        .first()
    )
    if existing:
        raise HTTPException(status_code=400, detail="You have already booked this class")

    # Get class
    fitness_class = (
        db.query(FitnessClass)
        .filter(FitnessClass.id == booking.class_id)
        .with_for_update()
        .first()
    )

    if not fitness_class:
        raise HTTPException(status_code=404, detail="Class not found")
        
    if fitness_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No available slots")
        
    fitness_class.available_slots -= 1

    new_booking = Booking(
            user_id = current_user.id,
            class_id = fitness_class.id,
            client_name = booking.client_name,
            client_email = booking.client_email
    )

    db.add(new_booking)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Booking failed due to database error")

    db.refresh(new_booking)
    return {"message": "Booking successful"}


# Get all bookings

@router.get("/", response_model=List[BookingResponse])
def get_user_bookings(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    bookings = (
        db.query(Booking)
        .filter(Booking.user_id == current_user.id)
        .all()
    )

    return bookings

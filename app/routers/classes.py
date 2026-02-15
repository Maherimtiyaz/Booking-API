from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import FitnessClass
from app.schemas import ClassCreate, ClassResponse
from app.dependencies import require_admin
from app.utils.timezone import convert_to_ist

router = APIRouter(prefix="/classes", tags=["Classes"])

# Create a new fitness class

@router.post(
        "/", 
        response_model=ClassResponse,
        status_code=status.HTTP_201_CREATED
)
def create_class(
    class_data: ClassCreate,
    db: Session = Depends(get_db),
    admin=Depends(require_admin)
):
    dt_ist = convert_to_ist(class_data.datetime)

    if dt_ist < convert_to_ist(datetime.utcnow()):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Class date and time must be scheduled in the future"
        )

    new_class = FitnessClass(
        name=class_data.name,
        datetime=dt_ist,
        instructor=class_data.instructor,
        available_slots=class_data.availableSlots,
        created_by=admin.id

    )

    db.add(new_class)
    db.commit()
    db.refresh(new_class)

    return new_class


# Get all fitness classes

@router.get("/", response_model=list[ClassResponse])
def get_classes(db: Session = Depends(get_db)):
    now_ist = convert_to_ist(datetime.utcnow())

    classes = (
        db.query(FitnessClass)
        .filter(FitnessClass.datetime > now_ist)
        .all()
    )

    return classes

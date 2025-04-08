import sys
import os

# Add the parent directory to sys.path to allow direct execution of this file
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from fastapi import APIRouter, Depends
from socialease_backend.database import get_db
from socialease_backend.services.progress_services import add_progress, get_progress
from socialease_backend.schemas import ProgressSchema

router = APIRouter()

@router.post("/progress")
def create_progress(progress: ProgressSchema, db=Depends(get_db)):
    return add_progress(db, progress)

@router.get("/progress/{user_id}")
def read_progress(user_id: int, db=Depends(get_db)):
    progress_data = get_progress(db, user_id)  # Call the service function
    return {"user_id": user_id, "progress": progress_data}  # Return progress details

@router.get("/progress")
def get_all_progress(db=Depends(get_db)):
    progress_data = db["progress"].find()  # Retrieve all progress data from the database
    return {"progress": list(progress_data)}  # Convert cursor to list and return

# This allows the file to be run directly for testing
if __name__ == "__main__":
    print("Progress router loaded successfully")

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud, models, database

router = APIRouter(prefix="skills", tags=["skills"])

@router.get("/", response_model=list[schemas.SkillOut])
def read_skills(db: Session = Depends(database.get_db)):
    return crud.get_skills(db)

@router.post("/",response_model=schemas.SkillOut)
def create_skill(skill: schemas)



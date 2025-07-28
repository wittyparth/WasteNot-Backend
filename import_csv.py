import csv
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .models import Base, Recipe, Cuisine, Course, Diet
import os

# Create tables if not exist
Base.metadata.create_all(bind=engine)

def get_or_create(model, db: Session, **kwargs):
    instance = db.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    instance = model(**kwargs)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance

def import_recipes_from_csv(csv_path: str):
    db: Session = SessionLocal()

    with open(csv_path, encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if not row["TranslatedRecipeName"].strip():
                continue  # skip empty rows

            cuisine = get_or_create(Cuisine, db, name=row["Cuisine"].strip())
            course = get_or_create(Course, db, name=row["Course"].strip())
            diet = get_or_create(Diet, db, name=row["Diet"].strip())

            recipe = Recipe(
                name=row["TranslatedRecipeName"].strip(),
                ingredients=row["TranslatedIngredients"].strip(),
                instructions=row["TranslatedInstructions"].strip(),
                prep_time=row["PrepTimeInMins"].strip() or None,
                cook_time=row["CookTimeInMins"].strip() or None,
                total_time=row["TotalTimeInMins"].strip() or None,
                servings=row["Servings"].strip() or None,
                cuisine_id=cuisine.id,
                course_id=course.id,
                diet_id=diet.id
            )

            db.add(recipe)

        db.commit()
        db.close()

if __name__ == "__main__":
    import_recipes_from_csv(os.path.join(os.path.dirname(__file__), "recepies.csv"))

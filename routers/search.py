from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from database import get_db
from models import Recipe
from typing import List
import re

router = APIRouter()

def normalize_ingredient_list(ingredients_str: str):
    """Clean and split ingredients string from DB"""
    # Remove brackets, dashes, newlines, units, etc.
    cleaned = re.sub(r'[^a-zA-Z,\s]', '', ingredients_str.lower())
    return [item.strip() for item in cleaned.split(',') if item.strip()]

@router.get("/search")
def search_recipes(ingredients: str = Query(..., description="Comma-separated ingredients"), db: Session = Depends(get_db)):
    input_ingredients = [i.strip().lower() for i in ingredients.split(",") if i.strip()]
    if not input_ingredients:
        return {"error": "No ingredients provided."}

    all_recipes = db.query(Recipe).all()
    scored = []

    for recipe in all_recipes:
        recipe_ingredients = normalize_ingredient_list(recipe.ingredients)
        match_count = len(set(recipe_ingredients) & set(input_ingredients))
        if match_count > 0:
            scored.append((match_count, recipe))

    scored.sort(key=lambda x: x[0], reverse=True)  # Best match on top

    return [
        {
           "id": recipe.id,
                "name": recipe.name,
                "translated_instructions": recipe.instructions,
                "course": recipe.course.name if recipe.course else None,
                "diet": recipe.diet.name if recipe.diet else None,
                "cuisine": recipe.cuisine.name if recipe.cuisine else None,
                "ingredients": recipe.ingredients.split(", "),
        }
        for match_count, recipe in scored
    ]

from fastapi import APIRouter, Depends, Query, Request,HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from database import get_db
from models import Recipe
from urllib.parse import urlencode
router = APIRouter()

@router.get("/recipes", summary="Get list of recipes with pagination, filters, and search")
def list_recipes(
    request: Request,
    db: Session = Depends(get_db),
    search: Optional[str] = Query(None, description="Search by recipe name"),
    course: Optional[str] = Query(None, description="Filter by course"),
    diet: Optional[str] = Query(None, description="Filter by diet"),
    cuisine: Optional[str] = Query(None, description="Filter by cuisine"),
    limit: int = Query(10, ge=1, le=100, description="Max recipes per page"),
    skip: int = Query(0, ge=0, description="Offset for pagination")
):
    # Base query
    query = db.query(Recipe)

    # Filters
    if search:
        query = query.filter(Recipe.name.ilike(f"%{search}%"))
    if course:
        query = query.join(Recipe.course).filter(Course.name == course)
    if diet:
        query = query.join(Recipe.diet).filter(Diet.name == diet)
    if cuisine:
        query = query.join(Recipe.cuisine).filter(Cuisine.name == cuisine)

    total = query.count()
    recipes = query.offset(skip).limit(limit).all()

    # Build URLs
    def build_url(new_skip: int):
        query_params = dict(request.query_params)
        query_params["skip"] = new_skip
        query_params["limit"] = limit
        return str(request.url.replace_query_params(**query_params))

    next_url = build_url(skip + limit) if (skip + limit) < total else None
    prev_url = build_url(max(skip - limit, 0)) if skip > 0 else None

    # Response
    return {
        "total": total,
        "limit": limit,
        "skip": skip,
        "next_url": next_url,
        "prev_url": prev_url,
        "results": [
            {
                "id": r.id,
                "name": r.name,
                "translated_instructions": r.instructions,
                "course": r.course.name if r.course else None,
                "diet": r.diet.name if r.diet else None,
                "cuisine": r.cuisine.name if r.cuisine else None,
                "ingredients": r.ingredients.split(", "),
            }
            for r in recipes
        ]
    }


@router.get("/recipes/{id}")
def get_recipe_by_id(id: int, db: Session = Depends(get_db)):
    recipe = db.query(Recipe).filter(Recipe.id == id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    return {
        "id": recipe.id,
        "name": recipe.name,
        "ingredients": [i.strip() for i in recipe.ingredients.split(",")] if recipe.ingredients else [],
        "instructions": recipe.instructions,
        "prep_time": recipe.prep_time,
        "cook_time": recipe.cook_time,
        "total_time": recipe.total_time,
        "servings": recipe.servings,
        "cuisine": recipe.cuisine.name if recipe.cuisine else None,
        "course": recipe.course.name if recipe.course else None,
        "diet": recipe.diet.name if recipe.diet else None
    }

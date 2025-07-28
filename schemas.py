from pydantic import BaseModel
from typing import List, Optional

class RecipeDetailOut(BaseModel):
    id: int
    translated_title: str
    image_url: str
    translated_instructions: str
    translated_ingredients: List[str]  # list format
    cuisine: Optional[str]
    course: Optional[str]
    diet: Optional[str]
    prep_time: Optional[str]
    cook_time: Optional[str]
    total_time: Optional[str]
    servings: Optional[str]
    source_url: Optional[str]

    class Config:
        orm_mode = True

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Cuisine(Base):
    __tablename__ = "cuisines"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    recipes = relationship("Recipe", back_populates="cuisine")

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    recipes = relationship("Recipe", back_populates="course")

class Diet(Base):
    __tablename__ = "diets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    recipes = relationship("Recipe", back_populates="diet")

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)  
    ingredients = Column(String, nullable=False)  
    instructions = Column(String, nullable=False)  
    prep_time = Column(String)
    cook_time = Column(String)
    total_time = Column(String)
    servings = Column(String)

    cuisine_id = Column(Integer, ForeignKey("cuisines.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    diet_id = Column(Integer, ForeignKey("diets.id"))

    cuisine = relationship("Cuisine", back_populates="recipes")
    course = relationship("Course", back_populates="recipes")
    diet = relationship("Diet", back_populates="recipes")

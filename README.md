```markdown
# 🧑‍🍳 Recipe API Backend - FastAPI

A modular, fast, and scalable RESTful backend to manage recipes, cuisines, courses, and diets using **FastAPI** and **SQLite**. Built with simplicity and extensibility in mind.

---

## 🌟 Features

- 🔍 Retrieve all recipes or a single recipe by ID
- 🍽 Filter recipes by cuisine, course, or diet
- ➕ Add, update, delete recipes
- ⚡ Built with FastAPI and SQLAlchemy
- 🧱 Clean modular architecture (`routers/`, `models/`, `schemas/`)
- 📚 Auto-generated Swagger API docs

---

## 🏗️ Project Structure

```

recipe-backend/
│
├── main.py              # App entrypoint
├── database.py          # DB connection and session management
├── models.py            # SQLAlchemy ORM models
├── schemas.py           # Pydantic schemas
├── routers/             # All route modules
│   ├── recipes.py
│   ├── cuisine.py
│   ├── course.py
│   └── diet.py
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

````

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/recipe-backend.git
cd recipe-backend
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Development Server

```bash
uvicorn main:app --reload
```

Now visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
You can explore all endpoints in the interactive Swagger UI.

---

## 🔌 API Endpoints

### 🔹 Recipe Routes

| Method | Endpoint        | Description             |
| ------ | --------------- | ----------------------- |
| GET    | `/recipes`      | Get all recipes         |
| GET    | `/recipes/{id}` | Get details of a recipe |
| POST   | `/recipes`      | Add a new recipe        |
| PUT    | `/recipes/{id}` | Update a recipe         |
| DELETE | `/recipes/{id}` | Delete a recipe         |

### 🔹 Cuisine / Course / Diet

| Method | Endpoint    | Description         |
| ------ | ----------- | ------------------- |
| GET    | `/cuisines` | List all cuisines   |
| GET    | `/courses`  | List all courses    |
| GET    | `/diets`    | List all diet types |

---

## 📘 Sample Recipe JSON

```json
{
  "name": "Masala Dosa",
  "ingredients": [
    "Rice", "Urad dal", "Potato", "Onion", "Mustard seeds"
  ],
  "instructions": "Soak, grind, ferment, cook dosa and stuff.",
  "prep_time": "10 mins",
  "cook_time": "15 mins",
  "total_time": "25 mins",
  "servings": "2",
  "cuisine_id": 1,
  "course_id": 1,
  "diet_id": 2
}
```

---

## 🧪 Development & Testing

* 🔄 Use `--reload` flag for live changes
* 🧪 Swagger UI: `/docs`
* 🧾 Redoc: `/redoc`

---

## 📦 Requirements

```
fastapi
uvicorn
sqlalchemy
pydantic
```

> Install with: `pip install -r requirements.txt`

---

## 🛠 Future Enhancements

* ✅ User authentication
* 🔍 Search and pagination
* 🐳 Docker containerization
* 🔒 Role-based access (Admin / User)
* 💾 PostgreSQL support

---

## 📄 License

MIT License © 2025 [Munakala Parthasaradhi](https://github.com/your-github-profile)

```

---

### ✅ Optional Additions
Let me know if you want me to generate:
- `requirements.txt`
- `Dockerfile`
- `env.example`
- Example `curl` or Postman requests

Would you like to push this to GitHub with a commit-ready `.gitignore` and `requirements.txt` as well?
```

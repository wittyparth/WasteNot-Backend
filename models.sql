-- categories
CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- cuisines
CREATE TABLE cuisine (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- recipes
CREATE TABLE recipe (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    instructions TEXT,
    image_url TEXT,
    prep_time TEXT,
    cook_time TEXT,
    total_time TEXT,
    servings TEXT,
    category_id INTEGER REFERENCES category(id),
    cuisine_id INTEGER REFERENCES cuisine(id)
);

-- ingredients
CREATE TABLE ingredient (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

-- recipe_ingredient mapping table (many-to-many)
CREATE TABLE recipe_ingredient (
    recipe_id INTEGER REFERENCES recipe(id) ON DELETE CASCADE,
    ingredient_id INTEGER REFERENCES ingredient(id) ON DELETE CASCADE,
    PRIMARY KEY (recipe_id, ingredient_id)
);

import json

# Load the database_recipes.json file
import os

def load_database_recipes():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "database_recipes.json")
    with open(file_path, "r") as file:
        return json.load(file)

def get_all_unique_directions():
    database_recipes = load_database_recipes()
    return list(set(state["Direction"] for state in database_recipes.values()))

def get_states_by_direction(direction):
    database_recipes = load_database_recipes()
    return [state for state, data in database_recipes.items() if data["Direction"] == direction]

def get_dishes_by_state(state_name):
    database_recipes = load_database_recipes()
    state = database_recipes.get(state_name)
    if not state:
        return []
    # Use index as unique id for each dish
    return [
        {
            "id": f"{state_name}_{i}",
            "name": dish["Name"],
            "images": dish.get("Images", [])
        }
        for i, dish in enumerate(state.get("Dishes", []))
    ]

def get_dish_by_id(dish_id):
    database_recipes = load_database_recipes()
    try:
        state_name, idx = dish_id.rsplit("_", 1)
        idx = int(idx)
        state = database_recipes.get(state_name)
        if not state:
            return None
        return state["Dishes"][idx]
    except Exception:
        return None
    

def init_backend():
    """ Initialize backend and load data """
    # Load the database_recipes.json file to ensure it's accessible
    load_database_recipes()
    print("Backend initialized and database loaded.")
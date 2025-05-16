import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import urllib.request
import io
import json
import os

# ---------- Backend Code ----------
def load_database_recipes():
    """Load recipes from database_recipes.json."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "database_recipes.json")
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("database_recipes.json not found.")
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load recipes: {e}")
        return {}

def get_all_unique_directions():
    """Get all unique regions (directions)."""
    database_recipes = load_database_recipes()
    return sorted(list(set(state["Direction"] for state in database_recipes.values())))

def get_states_by_direction(direction):
    """Get states for a given region (direction)."""
    database_recipes = load_database_recipes()
    return sorted([state for state, data in database_recipes.items() if data["Direction"] == direction])

def get_dishes_by_state(state_name):
    """Get dishes for a given state."""
    database_recipes = load_database_recipes()
    state = database_recipes.get(state_name)
    if not state:
        return []
    return [
        {
            "id": f"{state_name}_{i}",
            "name": dish["Name"],
            "images": dish.get("Images", [])
        }
        for i, dish in enumerate(state.get("Dishes", []))
    ]

def get_dish_by_id(dish_id):
    """Get detailed dish information by ID."""
    database_recipes = load_database_recipes()
    try:
        state_name, idx = dish_id.rsplit("_", 1)
        idx = int(idx)
        state = database_recipes.get(state_name)
        if not state or idx >= len(state.get("Dishes", [])):
            return None
        return state["Dishes"][idx]
    except Exception:
        return None

def init_backend():
    """Initialize backend and load data."""
    try:
        load_database_recipes()
        print("Backend initialized and database loaded.")
    except Exception as e:
        print(f"Backend initialization failed: {e}")

# ---------- Frontend Code ----------
# Settings
LOGIN_W, LOGIN_H = 500, 350
MAIN_W, MAIN_H = 650, 500
FAVORITES_FILE = "favorites.json"
favorites = []
open_windows = {}  # Track open windows to prevent duplicates

# Helpers
def center(win, w, h):
    """Center a window on the screen."""
    sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
    x, y = (sw - w) // 2, (sh - h) // 2
    win.geometry(f"{w}x{h}+{x}+{y}")

def load_favorites():
    """Load favorites from JSON file."""
    global favorites
    if os.path.exists(FAVORITES_FILE):
        try:
            with open(FAVORITES_FILE, "r") as f:
                favorites = json.load(f)
        except:
            favorites = []
    else:
        favorites = []

def save_favorites():
    """Save favorites to JSON file."""
    with open(FAVORITES_FILE, "w") as f:
        json.dump(favorites, f)

def close_window(window_id):
    """Close a window and remove it from open_windows."""
    if window_id in open_windows:
        open_windows[window_id].destroy()
        del open_windows[window_id]

# UI Functions
def show_recipe_details(dish_id):
    """Show detailed recipe information."""
    if dish_id in open_windows:
        open_windows[dish_id].focus_force()
        return

    dish = get_dish_by_id(dish_id)
    if not dish:
        messagebox.showinfo("Info", f"No detailed recipe available for ID: {dish_id}")
        return

    recipe_win = tk.Toplevel()
    recipe_win.title(f"{dish['Name']} – Recipe Details")
    center(recipe_win, 500, 600)
    recipe_win.configure(bg="#fffaf0")
    open_windows[dish_id] = recipe_win
    recipe_win.protocol("WM_DELETE_WINDOW", lambda: close_window(dish_id))

    canvas = tk.Canvas(recipe_win, bg="#fffaf0")
    scrollbar = tk.Scrollbar(recipe_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#fffaf0")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scrollable_frame, text=dish["Name"], font=("Georgia", 16, "bold"),
             bg="#fffaf0", fg="#8B0000").pack(pady=10)

    if dish.get("Images"):
        try:
            with urllib.request.urlopen(dish["Images"][0]) as response:
                img_data = response.read()
            img = Image.open(io.BytesIO(img_data)).resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(scrollable_frame, image=photo, bg="#fffaf0")
            img_label.image = photo
            img_label.pack(pady=10)
        except Exception:
            tk.Label(scrollable_frame, text="Unable to load image", font=("Verdana", 10), bg="#fffaf0").pack()

    def toggle_favorite():
        dish_name = dish["Name"]
        if dish_name in favorites:
            favorites.remove(dish_name)
            messagebox.showinfo("Removed", f"{dish_name} removed from Favorites.")
        else:
            favorites.append(dish_name)
            messagebox.showinfo("Added", f"{dish_name} added to Favorites.")
        save_favorites()

    tk.Button(scrollable_frame, text="❤️ Toggle Favorite", font=("Verdana", 10),
              bg="#ffb6c1", command=toggle_favorite).pack(pady=5)

    tk.Label(scrollable_frame, text="Description", font=("Verdana", 12, "bold"), bg="#fffaf0").pack(anchor="w", padx=20)
    tk.Message(scrollable_frame, text=dish.get("BasicInfo", "No description available."), font=("Verdana", 10), bg="#fffaf0", width=450).pack(anchor="w", padx=20)

    for section, key in [("Ingredients", "Ingredients"), ("Steps", "Steps"), ("Health Benefits", "HealthBenefits"), ("Tags", "Tags")]:
        tk.Label(scrollable_frame, text=section, font=("Verdana", 12, "bold"), bg="#fffaf0").pack(anchor="w", padx=20, pady=5)
        data = dish.get(key, [])
        if isinstance(data, list):
            for item in data:
                tk.Label(scrollable_frame, text=f"• {item}", font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=30)
        elif isinstance(data, dict):  # Nutrition is a dict
            for k, v in data.items():
                tk.Label(scrollable_frame, text=f"{k}: {v}", font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=30)
        else:
            tk.Label(scrollable_frame, text=str(data), font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=30)

    # Nutrition section (handled separately due to dict format)
    tk.Label(scrollable_frame, text="Nutrition", font=("Verdana", 12, "bold"), bg="#fffaf0").pack(anchor="w", padx=20, pady=5)
    for k, v in dish.get("Nutrition", {}).items():
        tk.Label(scrollable_frame, text=f"{k}: {v}", font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=30)

def show_dishes(state):
    """Show dishes for a given state."""
    if state in open_windows:
        open_windows[state].focus_force()
        return

    dishes = get_dishes_by_state(state)
    dish_win = tk.Toplevel()
    dish_win.title(f"{state} – Dishes")
    center(dish_win, 400, 400)
    dish_win.configure(bg="#fffaf0")
    open_windows[state] = dish_win
    dish_win.protocol("WM_DELETE_WINDOW", lambda: close_window(state))

    tk.Label(dish_win, text=f"{state} Specialties", font=("Georgia", 16, "bold"), bg="#fffaf0", fg="#8B0000").pack(pady=15)

    if not dishes:
        tk.Label(dish_win, text="No dishes available.", font=("Verdana", 12), bg="#fffaf0").pack(pady=20)
    else:
        for dish in dishes:
            frame = tk.Frame(dish_win, bg="#fffaf0")
            frame.pack(fill="x", padx=30, pady=2)
            tk.Label(frame, text="• " + dish["name"], font=("Verdana", 12), bg="#fffaf0").pack(side="left")
            tk.Button(frame, text="View", font=("Verdana", 10), bg="#90ee90",
                      command=lambda d=dish["id"]: show_recipe_details(d)).pack(side="right")

def show_states(direction):
    """Show states for a given region."""
    if direction in open_windows:
        open_windows[direction].focus_force()
        return

    states = get_states_by_direction(direction)
    state_win = tk.Toplevel()
    state_win.title(f"{direction} – States")
    center(state_win, 350, 400)
    state_win.configure(bg="white")
    open_windows[direction] = state_win
    state_win.protocol("WM_DELETE_WINDOW", lambda: close_window(direction))

    tk.Label(state_win, text=f"{direction} States", font=("Georgia", 16, "bold"),
             fg="#2E8B57", bg="white").pack(pady=10)

    for state in states:
        tk.Button(state_win, text=state, font=("Verdana", 12), width=25,
                  bg="#f0f8ff", command=lambda s=state: show_dishes(s)).pack(pady=5)

def show_favorites():
    """Show favorite dishes."""
    if "favorites" in open_windows:
        open_windows["favorites"].focus_force()
        return

    fav_win = tk.Toplevel()
    fav_win.title("Your Favorites")
    center(fav_win, 400, 400)
    fav_win.configure(bg="#fffaf0")
    open_windows["favorites"] = fav_win
    fav_win.protocol("WM_DELETE_WINDOW", lambda: close_window("favorites"))

    tk.Label(fav_win, text="⭐ Your Favorites", font=("Georgia", 16, "bold"), bg="#fffaf0", fg="#8B0000").pack(pady=10)

    if not favorites:
        tk.Label(fav_win, text="No favorites yet.", font=("Verdana", 12), bg="#fffaf0").pack(pady=20)
    else:
        # Map dish names to IDs
        dish_id_map = {}
        for state in load_database_recipes().keys():
            for dish in get_dishes_by_state(state):
                dish_id_map[dish["name"]] = dish["id"]

        for dish_name in favorites:
            dish_id = dish_id_map.get(dish_name)
            if not dish_id:
                continue  # Skip if dish not found
            frame = tk.Frame(fav_win, bg="#fffaf0")
            frame.pack(fill="x", padx=30, pady=2)
            tk.Label(frame, text="• " + dish_name, font=("Verdana", 12), bg="#fffaf0").pack(side="left")
            tk.Button(frame, text="View", font=("Verdana", 10), bg="#90ee90",
                      command=lambda d=dish_id: show_recipe_details(d)).pack(side="right")

def search_recipe(query):
    """Search for a recipe by name (case-insensitive, partial match)."""
    query = query.strip().lower()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a search query.")
        return

    database_recipes = load_database_recipes()
    matches = []
    for state in database_recipes:
        for i, dish in enumerate(database_recipes[state].get("Dishes", [])):
            if query in dish["Name"].lower():
                matches.append((dish["Name"], f"{state}_{i}"))

    if not matches:
        messagebox.showinfo("Not Found", f"No recipes found for: {query}")
        return

    if len(matches) == 1:
        show_recipe_details(matches[0][1])
    else:
        search_win = tk.Toplevel()
        search_win.title("Search Results")
        center(search_win, 400, 400)
        search_win.configure(bg="#fffaf0")
        open_windows["search"] = search_win
        search_win.protocol("WM_DELETE_WINDOW", lambda: close_window("search"))

        tk.Label(search_win, text="Search Results", font=("Georgia", 16, "bold"), bg="#fffaf0", fg="#8B0000").pack(pady=10)
        for name, dish_id in matches:
            frame = tk.Frame(search_win, bg="#fffaf0")
            frame.pack(fill="x", padx=30, pady=2)
            tk.Label(frame, text="• " + name, font=("Verdana", 12), bg="#fffaf0").pack(side="left")
            tk.Button(frame, text="View", font=("Verdana", 10), bg="#90ee90",
                      command=lambda d=dish_id: show_recipe_details(d)).pack(side="right")

def show_recipes():
    """Show the recipes page with regions and search."""
    if "recipes" in open_windows:
        open_windows["recipes"].focus_force()
        return

    recipe_win = tk.Toplevel()
    recipe_win.title("Recipes – Flavour Fusion")
    center(recipe_win, 400, 450)
    recipe_win.configure(bg="#f0f8ff")
    open_windows["recipes"] = recipe_win
    recipe_win.protocol("WM_DELETE_WINDOW", lambda: close_window("recipes"))

    tk.Label(recipe_win, text="Select a Region", font=("Georgia", 16, "bold"), bg="#f0f8ff", fg="#2E8B57").pack(pady=10)

    search_entry = tk.Entry(recipe_win, font=("Verdana", 11), width=25)
    search_entry.pack(pady=5)
    tk.Button(recipe_win, text="🔍 Search", font=("Verdana", 10), bg="#add8e6",
              command=lambda: search_recipe(search_entry.get())).pack(pady=5)

    directions = get_all_unique_directions()
    for direction in directions:
        tk.Button(recipe_win, text=direction, font=("Verdana", 13), width=25,
                  bg="#90ee90", command=lambda d=direction: show_states(d)).pack(pady=5)

def show_about():
    """Show the about page."""
    if "about" in open_windows:
        open_windows["about"].focus_force()
        return

    about_win = tk.Toplevel()
    about_win.title("About Us – Flavour Fusion")
    center(about_win, 500, 300)
    about_win.configure(bg="#fffaf0")
    open_windows["about"] = about_win
    about_win.protocol("WM_DELETE_WINDOW", lambda: close_window("about"))

    tk.Label(about_win, text="About Flavour Fusion", font=("Georgia", 18, "bold"), fg="#2E8B57", bg="#fffaf0").pack(pady=10)
    tk.Message(about_win, text="Flavour Fusion is your one-stop app for exploring authentic regional dishes across India. Discover, cook, and enjoy recipes from all corners of the country.",
               font=("Verdana", 12), width=450, bg="#fffaf0").pack(pady=10)

def show_main(username):
    """Show the main page."""
    if "main" in open_windows:
        open_windows["main"].focus_force()
        return

    main = tk.Toplevel()
    main.title("Flavour Fusion")
    center(main, MAIN_W, MAIN_H)
    main.configure(bg="#f5fffa")
    open_windows["main"] = main
    main.protocol("WM_DELETE_WINDOW", lambda: close_window("main"))

    tk.Label(main, text=f"Welcome, {username}!", font=("Georgia", 22, "bold"), fg="#2E8B57", bg="#f5fffa").pack(pady=15)
    tk.Label(main, text="CREATE · COMBINE · CRAVE", font=("Comic Sans MS", 16), fg="#8B0000", bg="#f5fffa").pack(pady=5)

    tk.Button(main, text="Explore Recipes", command=show_recipes,
              font=("Verdana", 12), bg="#32CD32", fg="white", width=20).pack(pady=10)
    tk.Button(main, text="⭐ Favorites", command=show_favorites,
              font=("Verdana", 12), bg="#ffd700", width=20).pack(pady=10)
    tk.Button(main, text="About Us", command=show_about,
              font=("Verdana", 12), bg="#4682B4", fg="white", width=20).pack(pady=10)

# Main Application
init_backend()
load_favorites()

root = tk.Tk()
root.title("Flavour Fusion – Login")
center(root, LOGIN_W, LOGIN_H)
root.configure(bg="#e6f2ff")
root.resizable(False, False)

tk.Label(root, text="Flavour Fusion", font=("Georgia", 24, "bold"), bg="#e6f2ff", fg="#2E8B57").pack(pady=20)
tk.Label(root, text="Enter Your Name", font=("Verdana", 12), bg="#e6f2ff").pack(pady=5)

name_entry = tk.Entry(root, font=("Verdana", 12), width=25)
name_entry.pack()

tk.Button(root, text="Login", font=("Verdana", 12), bg="#90ee90", width=15,
          command=lambda: show_main(name_entry.get().strip()) if name_entry.get().strip() else messagebox.showwarning("Input Error", "Please enter your name.")).pack(pady=20)

root.mainloop()
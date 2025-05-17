import tkinter as tk
from tkinter import messagebox, ttk, Scrollbar, VERTICAL, Canvas
from PIL import Image, ImageTk
import json
import urllib.request
import io
import os

# Load recipes (adapted for nested structure)
def load_recipes():
    with open(os.path.join(os.path.dirname(__file__), "../backend/database_recipes.json"), "r", encoding="utf-8") as file:
        return json.load(file)

data = load_recipes()
favorites = []

# Helper to flatten dishes with state info
def get_all_dishes():
    all_dishes = []
    for state_name, state_data in data.items():
        for i, dish in enumerate(state_data.get("Dishes", [])):
            dish_flat = {
                "id": f"{state_name}_{i}",
                "state": state_name,
                "region": state_data.get("Direction", ""),
                "name": dish.get("Name", ""),
                "ingredients": dish.get("Ingredients", []),
                "steps": dish.get("Steps", []),
                "nutritional_value": dish.get("Nutrition", {}),
                "health_benefits": dish.get("HealthBenefits", []),
                "tags": dish.get("Tags", []),
                "images": dish.get("Images", []),
                "basic_info": dish.get("BasicInfo", "")
            }
            all_dishes.append(dish_flat)
    return all_dishes

all_dishes = get_all_dishes()

# Constants
MAIN_W, MAIN_H = 900, 650

def center(win, w, h):
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = int((sw - w) / 2)
    y = int((sh - h) / 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

def load_image_from_url(url, size):
    try:
        with urllib.request.urlopen(url) as u:
            raw = u.read()
        im = Image.open(io.BytesIO(raw))
        im = im.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(im)
    except Exception:
        return None
    
def show_recipe_details(recipe):
    detail_win = tk.Toplevel(root)
    detail_win.title(recipe['name'])
    center(detail_win, 700, 650)
    detail_win.configure(bg="#fffaf0")

    # Create a canvas and a vertical scrollbar for scrolling
    canvas = tk.Canvas(detail_win, bg="#fffaf0", highlightthickness=0)
    scrollbar = ttk.Scrollbar(detail_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#fffaf0")

    # Configure the canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the widgets
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Now, add your widgets to scrollable_frame instead of detail_win
    tk.Label(scrollable_frame, text=recipe['name'], font=("Georgia", 20, "bold"), bg="#fffaf0", fg="#8B0000").pack(pady=10)
    tk.Label(scrollable_frame, text=f"{recipe['state']} ({recipe['region']})", font=("Verdana", 12), bg="#fffaf0", fg="#006400").pack(pady=2)
    tk.Label(scrollable_frame, text=recipe.get('basic_info', ""), font=("Verdana", 10, "italic"), bg="#fffaf0", fg="#555").pack(pady=2)

    img = None
    if recipe.get('images'):
        img = load_image_from_url(recipe['images'][0], (200, 200))
    if img:
        tk.Label(scrollable_frame, image=img, bg="#fffaf0").pack()
        detail_win.image = img

    def create_section(title, content):
        tk.Label(scrollable_frame, text=title, font=("Georgia", 14, "bold"), bg="#fffaf0", fg="#006400").pack(pady=(8, 0))
        if isinstance(content, list):
            for item in content:
                tk.Label(scrollable_frame, text=f"- {item}", font=("Verdana", 10), bg="#fffaf0", anchor="w", justify="left", wraplength=650).pack(anchor="w", padx=20)
        elif isinstance(content, dict):
            for k, v in content.items():
                tk.Label(scrollable_frame, text=f"{k}: {v}", font=("Verdana", 10), bg="#fffaf0", anchor="w").pack(anchor="w", padx=20)
        else:
            tk.Message(scrollable_frame, text=content, width=650, font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=20)

    create_section("Ingredients", recipe.get('ingredients', []))
    create_section("Steps", recipe.get('steps', []))
    create_section("Nutritional Value", recipe.get('nutritional_value', {}))
    create_section("Health Benefits", recipe.get('health_benefits', []))
    create_section("Tags", ", ".join(recipe.get('tags', [])))

    tk.Button(scrollable_frame, text="Add to Favorites", bg="#ffd700", command=lambda: add_to_favorites(recipe)).pack(pady=10)

def add_to_favorites(recipe):
    if recipe not in favorites:
        favorites.append(recipe)
        messagebox.showinfo("Added", f"{recipe['name']} added to favorites!")
    else:
        messagebox.showinfo("Already Added", f"{recipe['name']} is already in favorites.")

def remove_from_favorites(recipe):
    if recipe in favorites:
        favorites.remove(recipe)
        messagebox.showinfo("Removed", f"{recipe['name']} removed from favorites!")
    else:
        messagebox.showinfo("Not Found", f"{recipe['name']} is not in favorites.")

def show_recipes_by_state(state_name):
    state_dishes = [r for r in all_dishes if r['state'] == state_name]
    recipe_win = tk.Toplevel(root)
    recipe_win.title(f"Recipes – {state_name}")
    center(recipe_win, 800, 600)
    recipe_win.configure(bg="#f5fffa")

    tk.Label(recipe_win, text=f"{state_name} Recipes", font=("Georgia", 18, "bold"), bg="#f5fffa", fg="#2e8b57").pack(pady=10)
    for recipe in state_dishes:
        btn = tk.Button(recipe_win, text=recipe['name'], font=("Verdana", 12), width=40,
                        bg="#dcdcdc", command=lambda r=recipe: show_recipe_details(r))
        btn.pack(pady=5)

def show_states_by_region(region):
    states = sorted(set(r['state'] for r in all_dishes if r['region'] == region))
    states_win = tk.Toplevel(root)
    states_win.title(f"States – {region}")
    center(states_win, 400, 400)
    states_win.configure(bg="#e0f7fa")

    tk.Label(states_win, text=f"States in {region} region", font=("Georgia", 15, "bold"), bg="#e0f7fa", fg="#006064").pack(pady=10)
    for state in states:
        btn = tk.Button(states_win, text=state, font=("Verdana", 12), width=25,
                        bg="#b2ebf2", command=lambda s=state: show_recipes_by_state(s))
        btn.pack(pady=5)

def show_regions():
    regions = sorted(set(r['region'] for r in all_dishes))
    regions_win = tk.Toplevel(root)
    regions_win.title("Browse by Region")
    center(regions_win, 350, 350)
    regions_win.configure(bg="#ffe0b2")

    tk.Label(regions_win, text="Choose a Region", font=("Georgia", 15, "bold"), bg="#ffe0b2", fg="#c66900").pack(pady=10)
    for region in regions:
        btn = tk.Button(regions_win, text=region, font=("Verdana", 12), width=20,
                        bg="#ffd54f", command=lambda r=region: show_states_by_region(r))
        btn.pack(pady=5)

def show_all_recipes():
    recipe_win = tk.Toplevel(root)
    recipe_win.title("All Recipes")
    center(recipe_win, 800, 600)
    recipe_win.configure(bg="#f5fffa")

    tk.Label(recipe_win, text="All Recipes", font=("Georgia", 18, "bold"), bg="#f5fffa", fg="#2e8b57").pack(pady=10)

    # Create a canvas and a vertical scrollbar for scrolling
    canvas = tk.Canvas(recipe_win, bg="#f5fffa", highlightthickness=0)
    scrollbar = ttk.Scrollbar(recipe_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f5fffa")

    # Bind the scrollable frame to the canvas
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Add recipe buttons to the scrollable frame
    for recipe in all_dishes:
        btn = tk.Button(scrollable_frame, text=f"{recipe['name']} ({recipe['state']})", font=("Verdana", 12), width=45,
                        bg="#dcdcdc", command=lambda r=recipe: show_recipe_details(r))
        btn.pack(pady=5)

def show_favorites():
    fav_win = tk.Toplevel(root)
    fav_win.title("Favorites")
    center(fav_win, 600, 500)
    fav_win.configure(bg="#fffacd")

    tk.Label(fav_win, text="Your Favorite Recipes", font=("Georgia", 16, "bold"), bg="#fffacd", fg="#8b0000").pack(pady=10)

    if not favorites:
        tk.Label(fav_win, text="No favorites yet!", font=("Verdana", 12), bg="#fffacd").pack(pady=20)
    else:
        for recipe in favorites:
            frame = tk.Frame(fav_win, bg="#fffacd")
            frame.pack(pady=5)
            btn = tk.Button(frame, text=recipe['name'], font=("Verdana", 11), bg="#f0e68c",
                            command=lambda r=recipe: show_recipe_details(r))
            btn.pack(side="left", padx=5)
            remove_btn = tk.Button(frame, text="Remove", font=("Verdana", 10), bg="#ff6347",
                                   command=lambda r=recipe: remove_from_favorites(r))
            remove_btn.pack(side="left", padx=5)

def search_recipe():
    query = search_entry.get().lower()
    results = [r for r in all_dishes if query in r['name'].lower() or query in r['state'].lower() or query in r['region'].lower()]

    result_win = tk.Toplevel(root)
    result_win.title(f"Search: {query}")
    center(result_win, 600, 400)
    result_win.configure(bg="#e6e6fa")

    tk.Label(result_win, text=f"Results for '{query}':", font=("Georgia", 14, "bold"), bg="#e6e6fa").pack(pady=10)

    # Add scrolling to search results
    canvas = tk.Canvas(result_win, bg="#e6e6fa", highlightthickness=0)
    scrollbar = ttk.Scrollbar(result_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#e6e6fa")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    if not results:
        tk.Label(scrollable_frame, text="No matches found.", font=("Verdana", 11), bg="#e6e6fa").pack()
    else:
        for recipe in results:
            btn = tk.Button(scrollable_frame, text=f"{recipe['name']} ({recipe['state']})", font=("Verdana", 11), bg="#dda0dd",
                            command=lambda r=recipe: show_recipe_details(r))
            btn.pack(pady=5)

def show_about():
    about_win = tk.Toplevel(root)
    about_win.title("About Us – Flavour Fusion")
    center(about_win, 500, 300)
    about_win.configure(bg="#fffaf0")

    tk.Label(about_win, text="About Flavour Fusion", font=("Georgia", 16, "bold"), fg="#8B0000", bg="#fffaf0").pack(pady=10)
    about_text = (
        "Flavour Fusion is your digital guide to Indian regional cuisine.\n"
        "Explore traditional recipes across states, understand ingredients,\n"
        "and discover the story behind every dish.\n\n"
        "Made with ❤️ by food enthusiasts and developers.\n"
        "Enjoy the taste of India, one dish at a time!\n"
        "                                      \n"
        "                                      \n"
        "                                      \n"
                                                 "Made By - Team Ruthless\n"
    )
    tk.Message(about_win, text=about_text, width=450, font=("Verdana", 11), bg="#fffaf0").pack(pady=20)

# Main UI
root = tk.Tk()
root.title("Flavour Fusion – Home")
center(root, MAIN_W, MAIN_H)
root.configure(bg="#ffe4e1")

tk.Label(root, text="Flavour Fusion", font=("Georgia", 20, "bold"), bg="#ffe4e1", fg="#8B0000").pack(pady=20)

search_entry = tk.Entry(root, font=("Verdana", 12), width=30)
search_entry.pack(pady=5)
tk.Button(root, text="🔍 Search", font=("Verdana", 11), bg="#e0ffff", command=search_recipe).pack(pady=5)

tk.Button(root, text="🍲 Browse by Region", font=("Verdana", 12), width=25, bg="#ffe082", command=show_regions).pack(pady=10)
tk.Button(root, text="🍛 All Recipes", font=("Verdana", 12), width=25, bg="#98fb98", command=show_all_recipes).pack(pady=10)
tk.Button(root, text="⭐ Favorites", font=("Verdana", 12), width=25, bg="#ffdab9", command=show_favorites).pack(pady=10)
tk.Button(root, text="ℹ️ About Us", font=("Verdana", 12), width=25, bg="#add8e6", command=show_about).pack(pady=10)
tk.Button(root, text="❌ Exit", font=("Verdana", 12), width=25, bg="#ff7f7f", command=root.quit).pack(pady=20)

root.mainloop()
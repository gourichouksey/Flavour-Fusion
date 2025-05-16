# Flavour Fusion – Updated Version with Scrollable Regions and Recipes
import tkinter as tk
from tkinter import messagebox, ttk, Canvas, Scrollbar, VERTICAL
from PIL import Image, ImageTk
import json
import urllib.request
import io
import os

# Load recipes (adapted for nested structure)
def load_recipes():
    try:
        with open(
            os.path.join(os.path.dirname(__file__), "../backend/database_recipes.json"),
            "r",
            encoding="utf-8",
        ) as file:
            return json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error", "Recipe database file not found!")
        return {}

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
                "basic_info": dish.get("BasicInfo", ""),
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

def show_recipe_details(recipe):
    detail_win = tk.Toplevel(root)
    detail_win.title(recipe["name"])
    center(detail_win, 700, 650)
    detail_win.configure(bg="#fffaf0")

    canvas = tk.Canvas(detail_win, bg="#fffaf0", highlightthickness=0)
    scrollbar = ttk.Scrollbar(detail_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#fffaf0")

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(
        scrollable_frame,
        text=recipe["name"],
        font=("Georgia", 20, "bold"),
        bg="#fffaf0",
        fg="#8B0000",
    ).pack(pady=10)
    tk.Label(
        scrollable_frame,
        text=f"{recipe['state']} ({recipe['region']})",
        font=("Verdana", 12),
        bg="#fffaf0",
        fg="#006400",
    ).pack(pady=2)
    tk.Label(
        scrollable_frame,
        text=recipe.get("basic_info", ""),
        font=("Verdana", 10, "italic"),
        bg="#fffaf0",
        fg="#555",
    ).pack(pady=2)

    img = None
    if recipe.get("images"):
        img = load_image_from_url(recipe["images"][0], (200, 200))
    if img:
        tk.Label(scrollable_frame, image=img, bg="#fffaf0").pack()
        detail_win.image = img

    def create_section(title, content):
        tk.Label(
            scrollable_frame,
            text=title,
            font=("Georgia", 14, "bold"),
            bg="#fffaf0",
            fg="#006400",
        ).pack(pady=(8, 0))
        if isinstance(content, list):
            for item in content:
                tk.Label(
                    scrollable_frame,
                    text=f"- {item}",
                    font=("Verdana", 10),
                    bg="#fffaf0",
                    anchor="w",
                    justify="left",
                    wraplength=650,
                ).pack(anchor="w", padx=20)
        elif isinstance(content, dict):
            for k, v in content.items():
                tk.Label(
                    scrollable_frame,
                    text=f"{k}: {v}",
                    font=("Verdana", 10),
                    bg="#fffaf0",
                    anchor="w",
                ).pack(anchor="w", padx=20)
        else:
            tk.Message(
                scrollable_frame,
                text=content,
                width=650,
                font=("Verdana", 10),
                bg="#fffaf0",
            ).pack(anchor="w", padx=20)

    create_section("Ingredients", recipe.get("ingredients", []))
    create_section("Steps", recipe.get("steps", []))
    create_section("Nutritional Value", recipe.get("nutritional_value", {}))
    create_section("Health Benefits", recipe.get("health_benefits", []))
    create_section("Tags", ", ".join(recipe.get("tags", [])))

    tk.Button(
        scrollable_frame,
        text="Add to Favorites",
        bg="#ffd700",
        command=lambda: add_to_favorites(recipe),
    ).pack(pady=10)

def show_browse_by_region():
    region_win = tk.Toplevel(root)
    region_win.title("Browse by Region")
    center(region_win, 800, 600)
    region_win.configure(bg="#f5fffa")

    canvas = tk.Canvas(region_win, bg="#f5fffa", highlightthickness=0)
    scrollbar = ttk.Scrollbar(region_win, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f5fffa")

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(
        scrollable_frame,
        text="Browse by Region",
        font=("Georgia", 18, "bold"),
        bg="#f5fffa",
        fg="#2e8b57",
    ).pack(pady=10)

    for state_name, state_data in data.items():
        tk.Label(
            scrollable_frame,
            text=f"State: {state_name}, Region: {state_data.get('Direction', '')}",
            font=("Verdana", 12),
            bg="#f5fffa",
        ).pack(pady=5)

def show_all_recipes():
    recipe_win = tk.Toplevel(root)
    recipe_win.title("All Recipes")
    center(recipe_win, 800, 600)
    recipe_win.configure(bg="#f5fffa")

    canvas = tk.Canvas(recipe_win, bg="#f5fffa", highlightthickness=0)
    scrollbar = ttk.Scrollbar(recipe_win, orient=VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#f5fffa")

    scrollable_frame.bind(
        "<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(
        scrollable_frame,
        text="All Recipes",
        font=("Georgia", 18, "bold"),
        bg="#f5fffa",
        fg="#2e8b57",
    ).pack(pady=10)

    for recipe in all_dishes:
        tk.Button(
            scrollable_frame,
            text=recipe["name"],
            font=("Verdana", 12),
            bg="#dcdcdc",
            command=lambda r=recipe: show_recipe_details(r),
        ).pack(pady=5)

# Main UI
root = tk.Tk()
root.title("Flavour Fusion – Home")
center(root, MAIN_W, MAIN_H)
root.configure(bg="#ffe4e1")

tk.Label(
    root, text="Flavour Fusion", font=("Georgia", 20, "bold"), bg="#ffe4e1", fg="#8B0000"
).pack(pady=20)

tk.Button(
    root,
    text="🍲 Browse by Region",
    font=("Verdana", 12),
    width=25,
    bg="#ffe082",
    command=show_browse_by_region,
).pack(pady=10)
tk.Button(
    root,
    text="🍛 All Recipes",
    font=("Verdana", 12),
    width=25,
    bg="#98fb98",
    command=show_all_recipes,
).pack(pady=10)

root.mainloop()
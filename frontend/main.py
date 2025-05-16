# Flavour Fusion – Final Version with About, Recipes, Favorites, Search
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json
import urllib.request
import io

# Load recipes
def load_recipes():
    with open("updated_recipes.json", "r") as file:
        return json.load(file)

data = load_recipes()
favorites = []

# Constants
MAIN_W, MAIN_H = 800, 600

# Centering window
def center(win, w, h):
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x = int((sw - w) / 2)
    y = int((sh - h) / 2)
    win.geometry(f"{w}x{h}+{x}+{y}")

# Load image from URL
def load_image_from_url(url, size):
    try:
        with urllib.request.urlopen(url) as u:
            raw = u.read()
        im = Image.open(io.BytesIO(raw))
        im = im.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(im)
    except:
        return None

# Recipe Detail Page
def show_recipe_details(recipe):
    detail_win = tk.Toplevel(root)
    detail_win.title(recipe['name'])
    center(detail_win, 700, 600)
    detail_win.configure(bg="#fffaf0")

    tk.Label(detail_win, text=recipe['name'], font=("Georgia", 20, "bold"), bg="#fffaf0", fg="#8B0000").pack(pady=10)

    img = load_image_from_url(recipe.get('image', ''), (200, 200))
    if img:
        tk.Label(detail_win, image=img, bg="#fffaf0").pack()
        detail_win.image = img

    def create_section(title, content):
        tk.Label(detail_win, text=title, font=("Georgia", 14, "bold"), bg="#fffaf0", fg="#006400").pack(pady=(15, 0))
        if isinstance(content, list):
            for item in content:
                tk.Label(detail_win, text=f"- {item}", font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=20)
        else:
            tk.Message(detail_win, text=content, width=650, font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=20)

    create_section("Ingredients", recipe.get('ingredients', []))
    create_section("Steps", recipe.get('steps', []))
    create_section("Nutritional Value", recipe.get('nutritional_value', ''))
    create_section("Health Benefits", recipe.get('health_benefits', ''))
    create_section("Tags", ", ".join(recipe.get('tags', [])))

    tk.Button(detail_win, text="Add to Favorites", bg="#ffd700", command=lambda: add_to_favorites(recipe)).pack(pady=10)

# Add to favorites
def add_to_favorites(recipe):
    if recipe not in favorites:
        favorites.append(recipe)
        messagebox.showinfo("Added", f"{recipe['name']} added to favorites!")
    else:
        messagebox.showinfo("Already Added", f"{recipe['name']} is already in favorites.")

# Recipe List View
def show_recipes():
    recipe_win = tk.Toplevel(root)
    recipe_win.title("All Recipes")
    center(recipe_win, 800, 600)
    recipe_win.configure(bg="#f5fffa")

    tk.Label(recipe_win, text="Recipes by State and Region", font=("Georgia", 18, "bold"), bg="#f5fffa", fg="#2e8b57").pack(pady=10)

    for recipe in data:
        btn = tk.Button(recipe_win, text=recipe['name'], font=("Verdana", 12), width=40,
                        bg="#dcdcdc", command=lambda r=recipe: show_recipe_details(r))
        btn.pack(pady=5)

# Show Favorites
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
            btn = tk.Button(fav_win, text=recipe['name'], font=("Verdana", 11), bg="#f0e68c",
                            command=lambda r=recipe: show_recipe_details(r))
            btn.pack(pady=5)

# Search Recipes
def search_recipe():
    query = search_entry.get().lower()
    results = [r for r in data if query in r['name'].lower()]

    result_win = tk.Toplevel(root)
    result_win.title(f"Search: {query}")
    center(result_win, 600, 400)
    result_win.configure(bg="#e6e6fa")

    tk.Label(result_win, text=f"Results for '{query}':", font=("Georgia", 14, "bold"), bg="#e6e6fa").pack(pady=10)

    if not results:
        tk.Label(result_win, text="No matches found.", font=("Verdana", 11), bg="#e6e6fa").pack()
    else:
        for recipe in results:
            btn = tk.Button(result_win, text=recipe['name'], font=("Verdana", 11), bg="#dda0dd",
                            command=lambda r=recipe: show_recipe_details(r))
            btn.pack(pady=5)

# About Page
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
        "Enjoy the taste of India, one dish at a time!"
    )
    tk.Message(about_win, text=about_text, width=450, font=("Verdana", 11), bg="#fffaf0").pack(pady=20)

# Main UI
root = tk.Tk()
root.title("Flavour Fusion – Home")
center(root, MAIN_W, MAIN_H)
root.configure(bg="#ffe4e1")

# Title and Buttons
tk.Label(root, text="Flavour Fusion", font=("Georgia", 20, "bold"), bg="#ffe4e1", fg="#8B0000").pack(pady=20)

search_entry = tk.Entry(root, font=("Verdana", 12), width=30)
search_entry.pack(pady=5)
tk.Button(root, text="🔍 Search", font=("Verdana", 11), bg="#e0ffff", command=search_recipe).pack(pady=5)

tk.Button(root, text="🍲 Browse Recipes", font=("Verdana", 12), width=25, bg="#98fb98", command=show_recipes).pack(pady=10)
tk.Button(root, text="⭐ Favorites", font=("Verdana", 12), width=25, bg="#ffdab9", command=show_favorites).pack(pady=10)
tk.Button(root, text="ℹ️ About Us", font=("Verdana", 12), width=25, bg="#add8e6", command=show_about).pack(pady=10)
tk.Button(root, text="❌ Exit", font=("Verdana", 12), width=25, bg="#ff7f7f", command=root.quit).pack(pady=20)

root.mainloop()
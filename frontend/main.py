# Final Flavour Fusion App
# Automatically generated with all recipes, states, search, and favorites
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import urllib.request
import io

# ---------- Recipes Data ----------
recipes = {
    "Sarson Da Saag": {
        "Name": "Sarson Da Saag",
        "BasicInfo": "A winter favorite, made from mustard greens, spinach, and bathua (goosefoot). Traditionally served with Makki di Roti.",
        "Ingredients": [
            "Mustard greens \u2013 2 cups",
            "Spinach \u2013 1 cup",
            "Bathua \u2013 1 cup",
            "Ginger, garlic \u2013 1 tsp each (chopped)",
            "Green chili \u2013 1",
            "Makki atta (cornmeal) \u2013 1 tbsp (for thickening)",
            "Ghee \u2013 2 tbsp",
            "Salt \u2013 to taste"
        ],
        "Steps": [
            "Boil greens with ginger, garlic, chili until soft.",
            "Mash or blend coarsely.",
            "Add makki atta, cook till thick.",
            "Temper with ghee and serve with Makki di Roti."
        ],
        "Nutrition": {
            "Calories": "~180 kcal",
            "Protein": "6g",
            "Carbs": "18g",
            "Fiber": "6g"
        },
        "HealthBenefits": [
            "High in iron, calcium",
            "Great for immunity and warmth",
            "Aids digestion with fiber-rich greens"
        ],
        "Tags": [
            "#WinterFood",
            "#GreenPower",
            "#PunjabiClassic",
            "#VeganOptional",
            "#FiberRich"
        ],
        "Images": [
            "http://www.innereflection.com/wp-content/uploads/2016/11/Sarson-da-saag-feature-image-logo.jpg"
        ]
    },
    "Dal Makhani": {
        "Name": "Dal Makhani",
        "BasicInfo": "A creamy black lentil curry made with urad dal and kidney beans, simmered overnight for depth and richness.",
        "Ingredients": [
            "Whole urad dal \u2013 1 cup",
            "Rajma \u2013 \u00bc cup",
            "Onion, garlic, ginger \u2013 finely chopped",
            "Tomato puree \u2013 \u00bd cup",
            "Butter \u2013 3 tbsp",
            "Fresh cream \u2013 2 tbsp",
            "Spices \u2013 cumin, garam masala, red chili"
        ],
        "Steps": [
            "Soak dals overnight",
            "Boil until soft",
            "Saut\u00e9 onions, ginger, garlic in butter.",
            "Add tomato puree and spices, cook till oil separates.",
            "Add boiled dals, simmer for 1\u20132 hours.",
            "Finish with cream and extra butter."
        ],
        "Nutrition": {
            "Calories": "~300 kcal",
            "Protein": "12g",
            "Fat": "18g",
            "Carbs": "25g"
        },
        "HealthBenefits": [
            "High protein",
            "Rich in fiber and iron",
            "Comforting and energy-dense"
        ],
        "Tags": [
            "#PunjabiDal",
            "#Vegetarian",
            "#SlowCooked",
            "#Creamy",
            "#ComfortFood"
        ],
        "Images": [
            "https://maunikagowardhan.co.uk/wp-content/uploads/2017/11/Black-Dal-Makhani-scaled.jpg"
        ]
    }
}

# ---------- State-wise Dishes ----------
state_dishes = {
    "Punjab": [
        "Butter Chicken",
        "Sarson Da Saag",
        "Makki di Roti",
        "Dal Makhani",
        "Chole Bhature",
        "Rajma Chawal",
        "Lassi",
        "Amritsari Fish",
        "Aloo Paratha",
        "Paneer Tikka",
        "Pinni",
        "Kadhi Pakora",
        "Amritsari Kulcha",
        "Tandoori Chicken"
    ],
    "Himachal Pradesh": [
        "Siddu",
        "Chana Madra",
        "Babru",
        "Dham",
        "Tudkiya Bhath",
        "Babru",
        "Chha Gosht"
    ],
    "Haryana": [
        "Bajre ki Khichdi",
        "Churma",
        "Besan Masala Roti"
    ],
    "Uttarakhand": [
        "Aloo Ke Gutke",
        "Kafuli",
        "Chainsoo"
    ],
    "Leh Ladakh": [
        "Thukpa",
        "Skyu",
        "Momos"
    ],
    "Tamil Nadu": [
        "Sambar",
        "Rasam",
        "Chettinad Chicken"
    ],
    "Kerala": [
        "Appam",
        "Puttu",
        "Fish Curry"
    ],
    "Karnataka": [
        "Bisi Bele Bath",
        "Ragi Mudde",
        "Mysore Pak"
    ],
    "Andhra Pradesh": [
        "Pulihora",
        "Gongura Pachadi",
        "Kodi Kura"
    ],
    "Telangana": [
        "Hyderabadi Biryani",
        "Pesarattu",
        "Sakinalu"
    ],
    "Goa": [
        "Fish Curry Rice",
        "Prawn Balchao",
        "Bebinca"
    ],
    "West Bengal": [
        "Shorshe Ilish",
        "Chingri Malai Curry",
        "Mishti Doi"
    ],
    "Odisha": [
        "Dalma",
        "Chhena Poda",
        "Pakhala Bhata"
    ],
    "Bihar": [
        "Litti Chokha",
        "Sattu Paratha",
        "Thekua"
    ],
    "Jharkhand": [
        "Dhuska",
        "Chilka Roti",
        "Handia"
    ],
    "Assam": [
        "Masor Tenga",
        "Khar",
        "Pitha"
    ],
    "Sikkim": [
        "Phagshapa",
        "Gundruk",
        "Sel Roti"
    ],
    "Rajasthan": [
        "Dal Baati Churma",
        "Gatte ki Sabzi",
        "Laal Maas"
    ],
    "Gujarat": [
        "Dhokla",
        "Undhiyu",
        "Khandvi"
    ],
    "Maharashtra": [
        "Pav Bhaji",
        "Puran Poli",
        "Vada Pav"
    ],
    "Madhya Pradesh": [
        "Poha",
        "Bhutte Ka Kees",
        "Dal Bafla"
    ],
    "Chhattisgarh": [
        "Chana Samosa",
        "Faraa",
        "Dehrori"
    ]
}

# ---------- Region-wise States ----------
regions = {
    "North India": ["Punjab", "Haryana", "Himachal Pradesh", "Uttarakhand", "Leh Ladakh"],
    "South India": ["Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh", "Telangana", "Goa"],
    "East India": ["West Bengal", "Odisha", "Bihar", "Jharkhand", "Assam", "Sikkim"],
    "West India": ["Rajasthan", "Gujarat", "Maharashtra", "Goa"],
    "Central India": ["Madhya Pradesh", "Chhattisgarh"]
}

# ---------- App Code (UI + Logic) ----------

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import urllib.request
import io
import json

# ---------- Load Recipes from JSON ----------
with open("updated_recipes.json", "r") as f:
    recipes = json.load(f)

# ---------- Settings ----------
LOGIN_W, LOGIN_H = 500, 350
MAIN_W, MAIN_H = 650, 500
favorites = []

# ---------- Helpers ----------
def center(win, w, h):
    sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
    x, y = (sw - w)//2, (sh - h)//2
    win.geometry(f"{w}x{h}+{x}+{y}")

# ---------- Region Data ----------
regions = {
    "North India": ["Punjab", "Haryana", "Himachal Pradesh", "Uttarakhand", "Leh Ladakh"],
    "South India": ["Tamil Nadu", "Kerala", "Karnataka", "Andhra Pradesh", "Telangana", "Goa"],
    "East India": ["West Bengal", "Odisha", "Bihar", "Jharkhand", "Assam", "Sikkim"],
    "West India": ["Rajasthan", "Gujarat", "Maharashtra", "Goa"],
    "Central India": ["Madhya Pradesh", "Chhattisgarh"]
}

state_dishes = {
    "Punjab": list({r for r in recipes if "punjab" in recipes[r]["Tags"][0].lower()} | {"Butter Chicken", "Sarson Da Saag"}),
    "Himachal Pradesh": ["Siddu", "Chana Madra", "Babru"],
    # (Other states continue as previously defined...)
}

# ---------- Show Recipe Details ----------
def show_recipe_details(dish):
    recipe = recipes.get(dish)
    if not recipe:
        messagebox.showinfo("Info", f"No detailed recipe available for {dish}.")
        return

    recipe_win = tk.Toplevel()
    recipe_win.title(f"{dish} – Recipe Details")
    center(recipe_win, 500, 600)
    recipe_win.configure(bg="#fffaf0")

    canvas = tk.Canvas(recipe_win, bg="#fffaf0")
    scrollbar = tk.Scrollbar(recipe_win, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg="#fffaf0")

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    tk.Label(scrollable_frame, text=recipe["Name"], font=("Georgia", 16, "bold"),
             bg="#fffaf0", fg="#8B0000").pack(pady=10)

    if recipe["Images"]:
        try:
            with urllib.request.urlopen(recipe["Images"][0]) as response:
                img_data = response.read()
            img = Image.open(io.BytesIO(img_data)).resize((200, 200), Image.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(scrollable_frame, image=photo, bg="#fffaf0")
            img_label.image = photo
            img_label.pack(pady=10)
        except:
            tk.Label(scrollable_frame, text="Unable to load image", font=("Verdana", 10), bg="#fffaf0").pack()

    def add_to_favorites():
        if dish not in favorites:
            favorites.append(dish)
            messagebox.showinfo("Added", f"{dish} added to Favorites.")
        else:
            messagebox.showinfo("Exists", f"{dish} is already in Favorites.")

    tk.Button(scrollable_frame, text="❤️ Add to Favorites", font=("Verdana", 10),
              bg="#ffb6c1", command=add_to_favorites).pack(pady=5)

    tk.Label(scrollable_frame, text="Description", font=("Verdana", 12, "bold"), bg="#fffaf0").pack(anchor="w", padx=20)
    tk.Message(scrollable_frame, text=recipe["BasicInfo"], font=("Verdana", 10), bg="#fffaf0", width=450).pack(anchor="w", padx=20)

    for section, data in [("Ingredients", recipe["Ingredients"]), ("Steps", recipe["Steps"]),
                          ("Nutrition", recipe["Nutrition"].items()), ("Health Benefits", recipe["HealthBenefits"]),
                          ("Tags", [", ".join(recipe["Tags"])])]:
        tk.Label(scrollable_frame, text=section, font=("Verdana", 12, "bold"), bg="#fffaf0").pack(anchor="w", padx=20, pady=5)
        if isinstance(data, list):
            for item in data:
                tk.Label(scrollable_frame, text=f"• {item}", font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=30)
        else:
            for k, v in data:
                tk.Label(scrollable_frame, text=f"{k}: {v}", font=("Verdana", 10), bg="#fffaf0").pack(anchor="w", padx=30)

# ---------- Show Dishes ----------
def show_dishes(state):
    dishes = state_dishes.get(state, ["No dishes available."])
    dish_win = tk.Toplevel()
    dish_win.title(f"{state} – Dishes")
    center(dish_win, 400, 400)
    dish_win.configure(bg="#fffaf0")

    tk.Label(dish_win, text=f"{state} Specialties", font=("Georgia", 16, "bold"), bg="#fffaf0", fg="#8B0000").pack(pady=15)

    for dish in dishes:
        frame = tk.Frame(dish_win, bg="#fffaf0")
        frame.pack(fill="x", padx=30, pady=2)
        tk.Label(frame, text="• " + dish, font=("Verdana", 12), bg="#fffaf0").pack(side="left")
        tk.Button(frame, text="View", font=("Verdana", 10), bg="#90ee90",
                  command=lambda d=dish: show_recipe_details(d)).pack(side="right")

# ---------- Show States ----------
def show_states(region):
    state_win = tk.Toplevel()
    state_win.title(f"{region} – States")
    center(state_win, 350, 400)
    state_win.configure(bg="white")

    tk.Label(state_win, text=f"{region} States", font=("Georgia", 16, "bold"),
             fg="#2E8B57", bg="white").pack(pady=10)

    for state in regions[region]:
        tk.Button(state_win, text=state, font=("Verdana", 12), width=25,
                  bg="#f0f8ff", command=lambda s=state: show_dishes(s)).pack(pady=5)

# ---------- Favorites ----------
def show_favorites():
    fav_win = tk.Toplevel()
    fav_win.title("Your Favorites")
    center(fav_win, 400, 400)
    fav_win.configure(bg="#fffaf0")

    tk.Label(fav_win, text="⭐ Your Favorites", font=("Georgia", 16, "bold"), bg="#fffaf0", fg="#8B0000").pack(pady=10)

    if not favorites:
        tk.Label(fav_win, text="No favorites yet.", font=("Verdana", 12), bg="#fffaf0").pack(pady=20)
    else:
        for dish in favorites:
            frame = tk.Frame(fav_win, bg="#fffaf0")
            frame.pack(fill="x", padx=30, pady=2)
            tk.Label(frame, text="• " + dish, font=("Verdana", 12), bg="#fffaf0").pack(side="left")
            tk.Button(frame, text="View", font=("Verdana", 10), bg="#90ee90",
                      command=lambda d=dish: show_recipe_details(d)).pack(side="right")

# ---------- Search ----------
def search_recipe(dish):
    if dish in recipes:
        show_recipe_details(dish)
    else:
        messagebox.showinfo("Not Found", f"No recipe found for: {dish}")

# ---------- Recipes Page ----------
def show_recipes():
    recipe_win = tk.Toplevel()
    recipe_win.title("Recipes – Flavour Fusion")
    center(recipe_win, 400, 450)
    recipe_win.configure(bg="#f0f8ff")

    tk.Label(recipe_win, text="Select a Region", font=("Georgia", 16, "bold"), bg="#f0f8ff", fg="#2E8B57").pack(pady=10)

    search_entry = tk.Entry(recipe_win, font=("Verdana", 11), width=25)
    search_entry.pack(pady=5)
    tk.Button(recipe_win, text="🔍 Search", font=("Verdana", 10), bg="#add8e6",
              command=lambda: search_recipe(search_entry.get().strip())).pack(pady=5)

    for region in regions:
        tk.Button(recipe_win, text=region, font=("Verdana", 13), width=25,
                  bg="#90ee90", command=lambda r=region: show_states(r)).pack(pady=5)

# ---------- About ----------
def show_about():
    about_win = tk.Toplevel(root)
    about_win.title("About Us – Flavour Fusion")
    center(about_win, 500, 300)
    about_win.configure(bg="#fffaf0")
    tk.Label(about_win, text="About Flavour Fusion", font=("Georgia", 18, "bold"), fg="#2E8B57", bg="#fffaf0").pack(pady=10)
    tk.Message(about_win, text=("Flavour Fusion is your one-stop app for exploring authentic regional dishes "
                                "across India. Discover, cook, and enjoy recipes from all corners of the country."),
               font=("Verdana", 12), width=450, bg="#fffaf0").pack(pady=10)

# ---------- Main ----------
def show_main(username):
    main = tk.Toplevel(root)
    main.title("Flavour Fusion")
    center(main, MAIN_W, MAIN_H)
    main.configure(bg="#f5fffa")

    tk.Label(main, text=f"Welcome, {username}!", font=("Georgia", 22, "bold"), fg="#2E8B57", bg="#f5fffa").pack(pady=15)
    tk.Label(main, text="CREATE · COMBINE · CRAVE", font=("Comic Sans MS", 16), fg="#8B0000", bg="#f5fffa").pack(pady=5)

    tk.Button(main, text="Explore Recipes", command=show_recipes,
              font=("Verdana", 12), bg="#32CD32", fg="white", width=20).pack(pady=10)
    tk.Button(main, text="⭐ Favorites", command=show_favorites,
              font=("Verdana", 12), bg="#ffd700", width=20).pack(pady=10)
    tk.Button(main, text="About Us", command=show_about,
              font=("Verdana", 12), bg="#4682B4", fg="white", width=20).pack(pady=10)

# ---------- Login ----------
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
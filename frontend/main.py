# import tkinter as tk
# from tkinter import Toplevel, messagebox
# import json
# from backend import get_all_unique_directions, get_states_by_direction

# # ---------------------- Recipes Data ----------------------
# recipes_by_region = {
#     "Western India": {
#         "Rajasthan": {
#             "Main Course": [
#                 "Dal Baati Churma", "Gatte ki Sabzi", "Ker Sangri", "Rajasthani Kadhi", 
#                 "Laal Maas (Vegetarian Version with Paneer)", "Pyaaz Kachori", "Jodhpuri Sabzi", 
#                 "Bajra Khichdi", "Rabodi ki Sabzi", "Mangodi ki Sabzi"
#             ],
#             "Side Dishes": [
#                 "Papad ki Sabzi", "Lehsun ki Chutney", "Bajre ki Roti", "Mirchi Vada", 
#                 "Kachri ki Chutney"
#             ],
#             "Sweet Dishes": [
#                 "Ghevar", "Mawa Kachori", "Malpua", "Churma Ladoo", "Halwa (Gajar ka Halwa)"
#             ],
#             "Famous Drinks": [
#                 "Jal Jeera", "Masala Chaas", "Thandai", "Kesar Badam Milk", "Sattu Sharbat"
#             ]
#         },
#         # Add other states (Gujarat, Maharashtra, Goa) similarly...
#     }
# }

# # ---------------------- Tkinter Setup ----------------------
# root = tk.Tk()
# root.title("Flavour Fusion")
# root.geometry("600x700")
# root.configure(bg="#FFE4B5")  # Soft yellow background color

# # ---------------------- Functions ----------------------
# def show_state_dishes(state):
#     """ Show dishes for the selected state """
#     # TODO: Integrate get_dishes_by_state from backend to fetch and display dishes for the selected state
#     # TODO: Integrate get_dish_by_id to show full dish details when a dish is selected
#     state_window = Toplevel(root)
#     state_window.title(f"{state} Recipes")
#     state_window.geometry("400x600")
#     state_window.configure(bg="#FFF5E1")  # Light cream color for the state window
    
#     tk.Label(state_window, text=f"{state} Recipes", font=("Arial", 16, "bold"), bg="#FFF5E1", fg="#8B4513").pack(pady=10)

#     # Show Main Course Dishes
#     tk.Label(state_window, text="Main Course", font=("Arial", 14, "bold"), bg="#FFF5E1", fg="#8B4513").pack(pady=5)
#     for item in recipes_by_region["Western India"][state]["Main Course"]:
#         tk.Label(state_window, text=f"\u2022 {item}", font=("Arial", 12), bg="#FFF5E1", anchor="w", fg="#2F4F4F").pack(pady=2, padx=20, anchor="w")
    
#     # Add similar sections for Side Dishes, Sweet Dishes, and Famous Drinks...

# def show_region_dialog():
#     """ Show dialog with regional choices (dynamic from backend) """
#     # TODO: Already integrated get_all_unique_directions from backend for dynamic region listing
#     # TODO: Integrate get_dishes_by_state to show dishes for a selected state after state selection
#     region_dialog = Toplevel(root)
#     region_dialog.title("Choose Region")
#     region_dialog.geometry("300x300")
#     region_dialog.configure(bg="#FFE4B5")

#     tk.Label(region_dialog, text="Select a Region", font=("Arial", 16, "bold"), bg="#FFE4B5", fg="#8B4513").pack(pady=10)

#     # Get regions (directions) from backend
#     regions = get_all_unique_directions()
#     for region in regions:
#         btn = tk.Button(region_dialog, text=region, font=("Arial", 12), bg="#F4A460", fg="white", width=20,
#                         command=lambda r=region: show_states(r))
#         btn.pack(pady=5)
#         btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#D2691E"))
#         btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#F4A460"))


# def show_states(region, database_recipes=None):
#     """ Show states based on the region selected (dynamic from backend) """
#     # TODO: Already integrated get_states_by_direction from backend for dynamic state listing
#     # TODO: Integrate get_dishes_by_state to show dishes for a selected state after state selection
#     states_dialog = Toplevel(root)
#     states_dialog.title(f"{region} States")
#     states_dialog.geometry("300x300")
#     states_dialog.configure(bg="#FFE4B5")

#     tk.Label(states_dialog, text=f"{region} States", font=("Arial", 16, "bold"), bg="#FFE4B5", fg="#8B4513").pack(pady=10)

#     # Get states for the selected region from backend
#     states = get_states_by_direction(region)
#     for state in states:
#         btn = tk.Button(states_dialog, text=state, font=("Arial", 12), bg="#F4A460", fg="white", width=20,
#                         command=lambda s=state: show_state_dishes(s))
#         btn.pack(pady=5)
#         btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#D2691E"))
#         btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#F4A460"))

# # ---------------------- Login and Signup ----------------------

# def login_signup():
#     """ Show login or signup options """
#     login_window = Toplevel(root)
#     login_window.title("Login or Signup")
#     login_window.geometry("400x300")
#     login_window.configure(bg="#FFF5E1")

#     tk.Label(login_window, text="Login or Signup", font=("Arial", 16, "bold"), bg="#FFF5E1", fg="#8B4513").pack(pady=20)

#     btn_login = tk.Button(login_window, text="Login", font=("Arial", 12), bg="#F4A460", fg="white", width=20, command=messagebox.showinfo("Login", "Login functionality here"))
#     btn_login.pack(pady=10)

#     btn_signup = tk.Button(login_window, text="Sign Up", font=("Arial", 12), bg="#F4A460", fg="white", width=20, command=messagebox.showinfo("Signup", "Signup functionality here"))
#     btn_signup.pack(pady=10)

#     btn_google = tk.Button(login_window, text="Continue with Google", font=("Arial", 12), bg="#F4A460", fg="white", width=20, command=messagebox.showinfo("Google", "Google login here"))
#     btn_google.pack(pady=10)

# # ---------------------- About Us ----------------------
# def about_us():
#     """ Show about us information """
#     about_window = Toplevel(root)
#     about_window.title("About Us")
#     about_window.geometry("400x300")
#     about_window.configure(bg="#FFF5E1")

#     tk.Label(about_window, text="Flavour Fusion - Combine Crave", font=("Arial", 16, "bold"), bg="#FFF5E1", fg="#8B4513").pack(pady=20)
#     tk.Label(about_window, text="An app to explore regional Indian recipes", font=("Arial", 12), bg="#FFF5E1", fg="#2F4F4F").pack(pady=10)

#     tk.Label(about_window, text="Enjoy cooking and tasting delicious dishes from all over India.", font=("Arial", 12), bg="#FFF5E1", fg="#2F4F4F").pack(pady=10)

# # ---------------------- Main Menu ----------------------

# def main_menu():
#     """ Display the main menu of the app """
#     tk.Label(root, text="Welcome to Flavour Fusion!", font=("Arial", 20, "bold"), bg="#FFE4B5", fg="#8B4513").pack(pady=20)

#     tk.Button(root, text="Login / Sign Up", font=("Arial", 14), bg="#F4A460", fg="white", width=20, command=login_signup).pack(pady=10)
#     tk.Button(root, text="Continue with Google", font=("Arial", 14), bg="#F4A460", fg="white", width=20, command=messagebox.showinfo("Google", "Google login here")).pack(pady=10)
#     tk.Button(root, text="Recipes", font=("Arial", 14), bg="#F4A460", fg="white", width=20, command=show_region_dialog).pack(pady=10)
#     tk.Button(root, text="About Us", font=("Arial", 14), bg="#F4A460", fg="white", width=20, command=about_us).pack(pady=10)
#     tk.Button(root, text="Exit", font=("Arial", 14), bg="#F4A460", fg="white", width=20, command=root.quit).pack(pady=10)

# # ---------------------- Running the Application ----------------------
# def run_frontend():
#     print(f"Starting Frontend")
#     main_menu()
#     root.mainloop()



import tkinter as tk
from tkinter import Toplevel, messagebox
from tkinter import ttk
import json
from backend import get_all_unique_directions, get_states_by_direction, get_dishes_by_state

# Tkinter Setup
root = tk.Tk()
root.title("Flavour Fusion")
root.geometry("800x600")
root.configure(bg="#FFE4B5")

# Functions
def on_region_select(event):
    """Populate states Combobox when a region is selected"""
    selected_region = region_var.get()
    states = get_states_by_direction(selected_region)
    for widget in dishes_frame.winfo_children():
        widget.destroy()
    if states:
        state_combo['values'] = states
        state_var.set('')  # Clear state selection
    else:
        state_combo['values'] = []
        tk.Label(dishes_frame, text="No states found for this region.", font=("Arial", 12), bg="#FFF5E1", fg="#2F4F4F").pack(pady=10)

def on_state_select(event):
    """Display dishes when a state is selected"""
    selected_state = state_var.get()
    for widget in dishes_frame.winfo_children():
        widget.destroy()
    if selected_state:
        dishes = get_dishes_by_state(selected_state)
        if dishes:
            for category, dish_list in dishes.items():
                category_frame = tk.LabelFrame(dishes_frame, text=category, font=("Arial", 14, "bold"), bg="#FFF5E1")
                category_frame.pack(fill='x', padx=10, pady=5)
                for dish in dish_list:
                    tk.Label(category_frame, text=f"\u2022 {dish}", font=("Arial", 12), anchor="w", bg="#FFF5E1").pack(fill='x', padx=20, pady=2)
        else:
            tk.Label(dishes_frame, text="No dishes found for this state.", font=("Arial", 12), bg="#FFF5E1", fg="#2F4F4F").pack(pady=10)
    else:
        tk.Label(dishes_frame, text="Please select a state.", font=("Arial", 12), bg="#FFF5E1", fg="#2F4F4F").pack(pady=10)

def login_signup():
    """Show login or signup options"""
    login_window = Toplevel(root)
    login_window.title("Login or Signup")
    login_window.geometry("400x300")
    login_window.configure(bg="#FFF5E1")
    tk.Label(login_window, text="Login or Signup", font=("Arial", 16, "bold"), bg="#FFF5E1", fg="#8B4513").pack(pady=20)
    tk.Button(login_window, text="Login", font=("Arial", 12), bg="#F4A460", fg="white", width=20, command=lambda: messagebox.showinfo("Login", "Login functionality here")).pack(pady=10)
    tk.Button(login_window, text="Sign Up", font=("Arial", 12), bg="#F4A460", fg="white", width=20, command=lambda: messagebox.showinfo("Signup", "Signup functionality here")).pack(pady=10)
    tk.Button(login_window, text="Continue with Google", font=("Arial", 12), bg="#F4A460", fg="white", width=20, command=lambda: messagebox.showinfo("Google", "Google login here")).pack(pady=10)

def about_us():
    """Show about us information"""
    about_window = Toplevel(root)
    about_window.title("About Us")
    about_window.geometry("400x300")
    about_window.configure(bg="#FFF5E1")
    tk.Label(about_window, text="Flavour Fusion - Combine Crave", font=("Arial", 16, "bold"), bg="#FFF5E1", fg="#8B4513").pack(pady=20)
    tk.Label(about_window, text="An app to explore regional Indian recipes", font=("Arial", 12), bg="#FFF5E1", fg="#2F4F4F").pack(pady=10)
    tk.Label(about_window, text="Enjoy cooking and tasting delicious dishes from all over India.", font=("Arial", 12), bg="#FFF5E1", fg="#2F4F4F").pack(pady=10)

# Main Window Setup
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Frames for Tabs
home_frame = ttk.Frame(notebook)
home_frame.configure(bg="#FFE4B5")
recipes_frame = ttk.Frame(notebook)
recipes_frame.configure(bg="#FFE4B5")
about_frame = ttk.Frame(notebook)
about_frame.configure(bg="#FFE4B5")

# Add Frames to Notebook
notebook.add(home_frame, text='Home')
notebook.add(recipes_frame, text='Recipes')
notebook.add(about_frame, text='About Us')

# Home Tab
tk.Label(home_frame, text="Welcome to Flavour Fusion!", font=("Arial", 20, "bold"), bg="#FFE4B5", fg="#8B4513").pack(pady=20)
tk.Button(home_frame, text="Login / Sign Up", font=("Arial", 14), bg="#F4A460", fg="white", width=20, command=login_signup).pack(pady=10)
tk.Button(home_frame, text="Continue with Google", font=("Arial", 14), bg="#F4A460", fg="white", width=20, command=lambda: messagebox.showinfo("Google", "Google login here")).pack(pady=10)
tk.Button(home_frame, text="Exit", font=("Arial", 14), bg="#F4A460", fg="white", width=20, command=root.quit).pack(pady=10)

# Recipes Tab
regions = get_all_unique_directions()
region_var = tk.StringVar()
tk.Label(recipes_frame, text="Select Region:", font=("Arial", 14), bg="#FFE4B5", fg="#8B4513").pack(pady=10)
region_combo = ttk.Combobox(recipes_frame, textvariable=region_var, values=regions, state='readonly')
region_combo.pack(pady=5)
region_combo.bind("<<ComboboxSelected>>", on_region_select)

state_var = tk.StringVar()
tk.Label(recipes_frame, text="Select State:", font=("Arial", 14), bg="#FFE4B5", fg="#8B4513").pack(pady=10)
state_combo = ttk.Combobox(recipes_frame, textvariable=state_var, values=[], state='readonly')
state_combo.pack(pady=5)
state_combo.bind("<<ComboboxSelected>>", on_state_select)

dishes_frame = tk.Frame(recipes_frame, bg="#FFF5E1")
dishes_frame.pack(fill='both', expand=True, padx=10, pady=10)

# About Us Tab
tk.Label(about_frame, text="Flavour Fusion - Combine Crave", font=("Arial", 16, "bold"), bg="#FFE4B5", fg="#8B4513").pack(pady=20)
tk.Label(about_frame, text="An app to explore regional Indian recipes", font=("Arial", 12), bg="#FFE4B5", fg="#2F4F4F").pack(pady=10)
tk.Label(about_frame, text="Enjoy cooking and tasting delicious dishes from all over India.", font=("Arial", 12), bg="#FFE4B5", fg="#2F4F4F").pack(pady=10)

# Run Application
root.mainloop()
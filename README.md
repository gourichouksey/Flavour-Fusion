# Flavour Fusion

## Project Overview
Flavour Fusion is a digital guide to Indian regional cuisine. It allows users to explore traditional recipes across various states, understand ingredients, and discover the story behind every dish.

## Project Structure
- **Frontend files**: Located in the `./frontend` directory.
- **Backend files**: Located in the `./backend` directory.

## Features
- Browse recipes by region or state.
- View detailed recipe steps, ingredients, nutritional value, and health benefits.
- Search for recipes using keywords.
- Save favorite recipes for easy access.
- User-friendly GUI built with Tkinter.

## How to Setup and Run the App

### Prerequisites
1. **Python Installed**:
   - Ensure Python 3.6 or higher is installed on your machine. [Download Python](https://www.python.org/downloads/)
2. **Virtual Environment Setup** (recommended for dependency isolation):
   - If you're on Windows, use `venv` for creating a virtual environment.
   - On Mac/Linux, ensure `python3-venv` is installed.

### Step-by-Step Guide

## How to Run
1. Clone the repository:
    ```bash
    git clone https://github.com/gourichouksey/Flavour-Fusion.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Flavour-Fusion
    ```
3. Activate the virtual environment:
    ```bash
    source ./myenv/Scripts/activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the application:
    ```bash
    python main.py
    ```
    Or, if `python3` is required:
    ```bash
    python3 main.py
    ```

### Development Notes
- The backend is responsible for managing recipe data and providing APIs to fetch recipes based on states, regions, or IDs.
- The frontend is a Tkinter-based GUI that communicates with the backend to display recipes and interact with users.

### Troubleshooting
1. **Database File Not Found Error**:
   - Ensure `database_recipes.json` is present in the `backend` directory.
2. **Image Loading Issues**:
   - The app fetches images from online URLs. Ensure you have an active internet connection.

### Challenges Faced
1. The provided recipes were insufficient compared to the data required for the application.
2. Recipes had to be extracted based on state information from Grok.
3. Grok returned invalid images, necessitating the use of SERP to extract images based on dish names.


### Steps to push code
- git add .
- git commit -m "YOUR_MSG"
- git push origin main


## Credits
This project was created by **Gouri Chouksey** and the **Team Ruthless** with ❤️ for Indian cuisine enthusiasts.

# Flavour Fusion

## Project Structure
- **Frontend files**: Located in the `./frontend` directory.
- **Backend files**: Located in the `./backend` directory.

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

## Notes
### Challenges Faced
1. The provided recipes were insufficient compared to the data required for the application.
2. Recipes had to be extracted based on state information from Grok.
3. Grok returned invalid images, necessitating the use of SERP to extract images based on dish names.

### Pending Frontend Tasks
- Make all components dynamic, including:
  - Directions
  - States
  - Dishes
  - Data displayed upon clicking a dish name
- Improve UI/UX for better user interaction.

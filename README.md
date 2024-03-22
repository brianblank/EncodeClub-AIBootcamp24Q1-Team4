# EncodeClub-AIBootcamp24Q1-Team4

## Prerequisite

1. Create OPENAI_API_KEY environment variable.  API Keys can be managed here: https://platform.openai.com/api-keys
   * Linux BASH Shell (~/.bashrc)
     export OPENAI_API_KEY=[Your API Key Here]

3. Change to the directory of the desired project.  For example, assuming Project1 (ChefGPT)
   ```
   cd Project1
   ```
4. Create Python Virtual Environment
   ```
   python -m venv venv
   ```
5. Activate Virtual Environment
   * Windows
     ```
     .\venv\Scripts\Activate.ps1
     ```
   * Linux
     ```
     source ./venv/bin/activate
     ```
6. Install Dependencies
   ```
   pip install -r requirements.txt
   ```


## Project 1 - ChefGPT

The ChefGPT application uses LLMs to simulate a chef.  It has 4 different roles as follows:
1. Suggest random ingredients that can be used in a recipe
2. Suggest a dish that can be made with a given set of ingredients
3. Provide a recipe for a specified dish
4. Give critique for a given recipe

To run the application, simply type:
```
python Project1/main.py [<uniqueid>]
```
unique id is optional.  When not provided, 3 chefs will be picked at random.  When the unique id is provided, all 3 chefs roles will be assumed by that given unique id.

Valid Unique ID values are in main.py as follows:
```
# Unique IDs for the team members
team4_uniqueids = [
    "YTZTDV", # @Max Degenhardt 
    "4KTBAl", # @Guy Cioffi 
    "LMaGmf", # @Brian Blank 
    "0EY4BL", # Ritik Bompilwar
    "Ton3LP", # @ckxddd 
    "kC2AZ4", # @CryptoCortez 
    "nmv94F", # @Prasanna Malla 
    "TySKci", # @alex 
]
```


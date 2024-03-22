import sys
import os
import random
from openai import OpenAI
import subprocess

# Requirements of this script:
# 7. Create a `main.py` script that will call the different scripts based on the user input
# 8. Experiment passing a list of ingredients for one script, then ask another script for a recipe for that dish, and then criticize the recipe given by the last script with a third script
# 9. Create a report with the results of the experiment and the different outputs of the AI chefs

# Function to make call to ChefGPT Script and return output as String
def callChefGPT(uniqueid, collected_messages_str):
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))+os.sep
 
    print (f"** Calling ChefGPT-{uniqueid}.py:\n")
    command = ["python3", f"{script_dir}ChefGPT-{uniqueid}.py", collected_messages_str]
    process = subprocess.run(command, capture_output=True, text=True)
    output = process.stdout
    return output

# Unique IDs for the team members
team4_uniqueids = [
    # "YTZTDV", # @Max Degenhardt 
    # "4KTBAl", # @Guy Cioffi 
    "LMaGmf", # @Brian Blank 
    # "0EY4BL", # Ritik Bompilwar
    # "Ton3LP", # @ckxddd 
    # "kC2AZ4", # @CryptoCortez 
    # "nmv94F", # @Prasanna Malla 
    # "TySKci", # @alex 
]

# Select 3 User IDs to use for the content generation
userids = []
for _ in range(3):
    if len(sys.argv) > 1:
        userids.append(sys.argv[1])
    else:
        userids.append(random.choice(team4_uniqueids))

# First get a random list of ingredients to pass to the first script
num_ingredients = 15

client = OpenAI()
messages = [
     {
          "role": "system",
          "content": "You are a food guru and can suggest world class ingredients for any dish in the world.",
     }
]

messages.append(
    {
        "role": "user",
        "content": f"Give me a list of {num_ingredients} random ingredients for world class food dishes.  Do not add any commentary.  Just provide the list of ingredients."
    }
)

model = "gpt-4-0125-preview"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

print("List of Ingredients:")
collected_messages = ["--- START OF INGREDIENTS ---\n\n"]
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)
collected_messages.append("\n\n--- END OF INGREDIENTS ---\n\n")
ingredients = ''.join(collected_messages)

# Now that we have the ingredients, let's get a dish that can use those ingredients
print("\n\n-=-=-=-=-=-=-=-")
print("\n\nGet a dish that can be made with these ingredients:")
dish = callChefGPT(userids[0], ingredients)
print(dish, "\n\n")

# Now that we have a dish, let's get the recipe for that dish
print("-=-=-=-=-=-=-=-")
print("\n\nGet a recipe for this dish:")
recipe = callChefGPT(userids[1], dish)
print(recipe, "\n\n")

# Now that we have a recipe, let's criticize it
print("-=-=-=-=-=-=-=-")
print("\n\nCriticize the recipe for this dish:")
critique = callChefGPT(userids[2], recipe)
print(critique, "\n\n")

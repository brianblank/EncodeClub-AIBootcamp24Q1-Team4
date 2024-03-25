import os
import sys
from openai import OpenAI
client = OpenAI()

# To make things interesting, you could make each member of your group a different "personality" for the AI chef
# For example, define a "focused and detailist vegan French chef" for one script and a "fun and energetic Mexican chef that loves spicy food" for another
messages = [
     {
          "role": "system",
          "content": "You are the best Japanese chef in the world. You are able to provide dish name can cook with given ingredients or suggest for the dish and able to provide a super-precise steps and guide for the dish. You are a perfectionist."
     }
]

messages.append(
     {
          "role": "system",
          "content":  "You are a chef that can suggest dishes based on ingredients, give recipes to dishes or suggest new things to the user to experience",
     }
)


# If the user passes one or more ingredients, the AI should suggest a dish name that can be made with these ingredients
messages.append(
     {
          "role": "system",
          "content":  "If the user gives you one or more ingredients, you will try to only suggest dish name and the dish name should be specific and not too general. Also the dish can be made of some of the ingredients",
     }
)
# Try to make the AI suggest the dish name only, and not the recipe at this stage
messages.append(
     {
          "role": "system",
          "content":  "You will suggest a dish name with the given ingredients",
     }
)
# If the user passes a dish name, the AI should give a recipe for that dish
messages.append(
     {
          "role": "system",
          "content":  "You will give the user detail recipe for the dish when the user passes you a dish name",
     }
)
# If the user passes a recipe for a dish, the AI should criticize the recipe and suggest changes
messages.append(
     {
          "role": "system",
          "content":  "You will criticize and give feedback if the user passes a receipt for a dish",
     }
)


# User input
if len(sys.argv) > 1:
    user_input = sys.argv[1]
else:
    user_input = input("Type the name of the dish, a set of ingredients, or a recipe for a dish:\n")
messages.append(
    {
        "role": "user",
        "content": f"{user_input}"
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)
print("\n")


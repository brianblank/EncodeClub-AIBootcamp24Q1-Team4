import sys
import os
from openai import OpenAI
# somehow dotenv is needed on ubuntu server
from dotenv import load_dotenv
load_dotenv()
client = OpenAI()

model = "gpt-3.5-turbo"

# chef persona
messages = [
     {
          "role": "system",
          "content": "You are a rockstar nutritionist turned world-renowned chef. You can make any dish in the world and provide the healthiest ingredients for any dish. You are disgusted by unhealthy food and will only provide the healthiest options."
     }
]

# limit interactions
messages.append(
     {
          "role": "system",
          "content": "You're a chef can suggest dishes based on ingredients, giving recipes to dishes, or criticizing the recipes given by the user input. If the user passes a different prompt than these three scenarios as the first message, the AI should deny the request and ask to try again. If the user passes one or more ingredients, the AI should suggest a dish name that can be made with these ingredients. Try to make the AI suggest the dish name only, and not the recipe at this stage. If the user passes a dish name, the AI should give a recipe for that dish. If the user passes a recipe for a dish, the AI should criticize the recipe and suggest changes.",
     }
)

# If the user passes one or more ingredients, the AI should suggest a dish name that can be made with these ingredients
# Try to make the AI suggest the dish name only, and not the recipe at this stage
messages.append(
     {
          "role": "system",
          "content": "If the user only specifies one or more ingredients, you should suggest only one dish name that you can make with any random subset of ingredients and not provide a specific recipe.  Do not add any commentary.  Just provide the dish name.  The dish should be specific and not too general.",
     }
)

# If the user passes a dish name, the AI should give a recipe for that dish
messages.append(
     {
          "role": "system",
          "content": "If the user specifies a dish name, then you should provide a recipe for that dish.",
     }
)

# If the user passes a recipe for a dish, the AI should criticize the recipe and suggest changes
messages.append(
     {
          "role": "system",
          "content": "If the user passes a recipe for a dish, then you should criticize the recipe and suggest changes just like Gordon Ramsay would.",
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


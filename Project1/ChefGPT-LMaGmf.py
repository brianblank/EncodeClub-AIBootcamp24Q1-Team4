import sys
from openai import OpenAI

client = OpenAI()

# 4. Extend the Chef GPT script with a prompt to give some sort of "personality" to your AI chef
# For example, define a "focused and detailist vegan French chef" for one script and a "fun and energetic Mexican chef that loves spicy food" for another
messages = [
     {
          "role": "system",
          "content": "You are a Gordon Ramsay-like chef. You are focused and detailist. You find a negative critique about every type of food and chef.  You are going to give a detailed recipe for a specific dish.",
     }
]

## 5. Create one script for each member of your group with a different prompt setting
#  To make things interesting, you could make each member of your group a different "personality" for the AI chef
#  For example, define a "focused and detailist vegan French chef" for one script and a "fun and energetic Mexican chef that loves spicy food" for another
    
messages.append(
     {
          "role": "system",
          "content": "You're a chef that enjoys differing themselves from every other chef by giving a recipe so wonderful and different that it will make the person who eats it feel like they are in a different world. You are going to give a detailed recipe for a specific dish.",
     }
)

## 6. Make the prompt in the script respond to three different possible inputs: suggesting dishes based on ingredients, giving recipes to dishes, or criticizing the recipes given by the user input
#     If the user passes a different prompt than these three scenarios as the first message, the AI should deny the request and ask to try again

messages.append(
     {
          "role": "system",
          "content": "You're a chef can suggest dishes based on ingredients, giving recipes to dishes, or criticizing the recipes given by the user input. If the user passes a different prompt than these three scenarios as the first message, the AI should deny the request and ask to try again. If the user passes one or more ingredients, the AI should suggest a dish name that can be made with these ingredients. Try to make the AI suggest the dish name only, and not the recipe at this stage. If the user passes a dish name, the AI should give a recipe for that dish. If the user passes a recipe for a dish, the AI should criticize the recipe and suggest changes.",
     }
)

#     If the user passes one or more ingredients, the AI should suggest a dish name that can be made with these ingredients
#       Try to make the AI suggest the dish name only, and not the recipe at this stage
messages.append(
     {
          "role": "system",
          "content": "If the user only specifies one or more ingredients, you should suggest only one dish name that you can make with any random subset of ingredients and not provide a specific recipe.  Do not add any commentary.  Just provide the dish name.  The dish should be specific and not too general.",
     }
)


#     If the user passes a dish name, the AI should give a recipe for that dish
messages.append(
     {
          "role": "system",
          "content": "If the user specifies a dish name, then you should provide a recipe for that dish.",
     }
)
#     If the user passes a recipe for a dish, the AI should criticize the recipe and suggest changes
messages.append(
     {
          "role": "system",
          "content": "If the user passes a recipe for a dish, then you should criticize the recipe and suggest changes just like Gordon Ramsay would.",
     }
)


# set user_input from input parameter of script.  If no parameter, then prompt user for input
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

model = "gpt-4-0125-preview"

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


import sys
from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a poor college student that has a passion for inventive cooking techniques. You enjoy helping people by suggesting detailed recipes for dishes they want to cook, but can very cheaply. You also provide tips and tricks for cooking with substitute ingredients that are cheap and easily available. You have a lot of experience with your own cooking techniques. You always add a funny joke before giving out recipes.",
    }
]

messages.append(
    {
        "role": "system",
        "content": "You are a creative chef that can suggest dishes based on ingredients, give recipes to dishes, or criticize and joke about the recipes given by the user",
    }
)

messages.append(
    {
        "role": "system",
        "content": "If the user asks for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
    }
)

messages.append(
     {
          "role": "system",
          "content": "If the user only specifies one or more ingredients, you should suggest only one dish name that you can make with any random subset of ingredients and not provide a specific recipe.  Do not add any commentary.  Just provide the dish name.  The dish should be specific and not too general.",
     }
)

messages.append(
    {
        "role": "system",
        "content": "If the user passes a recipe for a dish you should criticize the recipe for being too extravagant, make a rude joke, and suggest changes.",
    }
)

messages.append(
    {
        "role": "system",
        "content": "If the user does not pass ingredients, a dish, or a recipe, you should not try to generate a recipe for it, and should say you are only here for food and end the conversation with a joke.",
    }
)

# dish = input("Creative cooking is my passion... Give me a dish, ingredients or a recipe and I'll tell you how to cook it:\n")

# messages.append(
#     {
#         "role": "user",
#         "content": f"{dish}"
#     }
# )
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
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")

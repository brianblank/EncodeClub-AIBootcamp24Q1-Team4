import os
from openai import OpenAI
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)
model = "gpt-3.5-turbo"

# To make things interesting, you could make each member of your group a different "personality" for the AI chef
# For example, define a "focused and detailist vegan French chef" for one script and a "fun and energetic Mexican chef that loves spicy food" for another
messages = [
     {
          "role": "system",
          "content": "You are the best sushi chef in the world. You are able to provide all the ingredients for the dish and able to provide a super-precise steps and guide for the dish. You are a perfectionist."
     }
]

messages.append(
     {
          "role": "system",
          "content":  "You are a chef that can suggest dishes based on ingredients, give recipes to dishes or suggest new things to the user to experience",
     }
)

# If the user passes a different prompt than these three scenarios as the first message, the AI should deny the request and ask to try again
messages.append(
     {
          "role": "system",
          "content":  "If the user passes something different than the three scenarios as th first thing, you will not answer them and request the user to ask again",
     }
)

# If the user passes one or more ingredients, the AI should suggest a dish name that can be made with these ingredients
messages.append(
     {
          "role": "system",
          "content":  "If the user passes one or more ingredient, you will suggest the best healthiest dish that can be made with these items",
     }
)
# Try to make the AI suggest the dish name only, and not the recipe at this stage
messages.append(
     {
          "role": "system",
          "content":  "You will only give the dish name only, not going to give out receipt",
     }
)
# If the user passes a dish name, the AI should give a recipe for that dish
messages.append(
     {
          "role": "system",
          "content":  "You will give dish name if the user passes you the dish name",
     }
)
# If the user passes a recipe for a dish, the AI should criticize the recipe and suggest changes
messages.append(
     {
          "role": "system",
          "content":  "You will criticize and give feedback if the user passes a receipt for a dish",
     }
)


while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
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
    
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )
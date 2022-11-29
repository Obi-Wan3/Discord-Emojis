import os
import sys
import json

if not os.path.isfile("./emojis.json"):
    print("No emojis.json file found!")
    sys.exit()

with open("./emojis.json", "r", encoding="utf8") as f:
    data = json.load(f)

all_emojis = []

# Loop through main categories
for category in data.values():
    # Loop through each category
    for emoji in category:
        all_emojis.append(emoji["surrogates"])

print(all_emojis)

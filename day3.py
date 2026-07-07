import json

with open("goldens.json") as f:
    goldens = json.load(f)

for g in goldens:
    print(g["input"], "→", g["expected"])

results = [
    {"input":"what are your hours?", "score":0.92, "passed":True},
    {"input":"do you ship internationally?", "score":0.61, "passed":False}
]

with open("results.json", "w") as f:
    json.dump(results, f, indent=2)

print("Results saved to results.json")
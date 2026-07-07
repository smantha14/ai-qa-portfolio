# Day 1 — variables, lists, dicts

model = "claude-sonnet-4-6"
threshold = 0.7

print(f"Testing {model} at threshold {threshold}")

# A list — this is your test data

test_inputs = ["what are your hours?","do you ship internationally?"]
for case in test_inputs:
  print(f"Running: {case}")

print(test_inputs[0]) 

# A dict — one golden test case

golden = {
  "input":  "what are your hours?",
  "output": "Our hours are 9am to 5pm, Monday through Friday."
}
print(golden["input"])
print(golden["output"])

goldens = [
    {"input": "What are your hours?",   "expected": "9 to 5, Mon-Fri"},
    {"input": "Do you ship overseas?",  "expected": "Yes, worldwide"},
]

for g in goldens:
    print(f"Input: {g['input']}  →  Expected: {g['expected']}")
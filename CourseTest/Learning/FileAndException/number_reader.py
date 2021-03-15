import json

fileName = 'number.json'
with open(fileName,'r') as f:
    numbers = json.load(f)

print(numbers)
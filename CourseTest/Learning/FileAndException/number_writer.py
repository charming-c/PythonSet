import json

numbers = [2, 3, 5, 7, 11, 13]

fileName = 'number.json'
with open(fileName,'w') as f:
    json.dump(numbers,f)
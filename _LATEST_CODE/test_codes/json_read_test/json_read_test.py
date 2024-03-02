'''
json 모듈로 example.json 이 읽기 가능한지 테스트
'''


import json

# Write JSON data to a file
data = {'name': 'John', 'age': 30, 'city': 'New York'}
with open('example.json', 'w') as file:
    json.dump(data, file)

# Read JSON data from a file
with open('example.json', 'r') as file:
    data = json.load(file)

# Access the data in the dictionary
print(data['name'])
print(data['age'])
print(data['city'])
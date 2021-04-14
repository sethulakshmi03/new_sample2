"""
1. Delete set of keys from Python Dictionary
Given:

sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keysToRemove = ["name", "salary"]

2. Check if a value 200 exists in a dictionary
sampleDict = {'a': 100, 'b': 200, 'c': 300}
3. Get the key corresponding to the minimum value from the following dictionary
sampleDict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
4. Given a Python dictionary, Change Brad’s salary to 8500
sampleDict = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

"""
sampleDict1 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
sampleDict1.pop("name")
sampleDict1.pop("salary")
print(sampleDict1)

sampleDict2 = {'a': 100, 'b': 200, 'c': 300}
if 'a' in sampleDict2:
    print("character \'a\' in sampleDict2")

sampleDict3 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print("Min Value in sample dict3 is: ",min(sampleDict3.values()))

sampleDict4 = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

sampleDict4['emp3']['salary'] = 8500
print(sampleDict4)
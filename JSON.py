#Write a Python program to convert Python dictionary object (sort by key) to JSON data. Print the object members with indent level 4.
import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original String:")
print(j_str)
print("\nJSON data:")
print(json.dumps(j_str, sort_keys=True, indent=4))



#Write a Python program to create a new JSON file from an existing JSON file.
import json

with open('states.json') as f:
  state_data= json.load(f)

for state in state_data['states']:
  del state['area_codes']

with open('new_states.json', 'w') as f:
  json.dump(state_data, f, indent=2)
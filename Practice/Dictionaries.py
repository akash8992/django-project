# Nested dictionaries and default values
data = {
    'person1': {'name': 'Akash', 'age': 30},
    'person2': {'name': 'John', 'age': 25}
}

# Accessing nested data
print(data['person1']['name'])  # Output: Akash

# Adding default values using setdefault
data.setdefault('person3', {'name': 'Jane', 'age': 28})
print(data['person3'])

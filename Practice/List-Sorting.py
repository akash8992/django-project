# Sorting a list and using the zip function
names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 80]

# Sorting names based on scores
sorted_pairs = sorted(zip(scores, names), reverse=True)

print("Sorted names by scores:", sorted_pairs)

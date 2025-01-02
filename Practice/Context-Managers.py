# Using a context manager to handle file operations
with open('example.txt', 'w') as file:
    file.write("This is an example content.")

# File will automatically close after the block

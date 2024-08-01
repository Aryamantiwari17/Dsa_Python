import os

# Get current working directory
cwd = os.getcwd()
print(f"Current working directory is {cwd}")

# Create a new directory if it doesn't exist
new_directory = "package"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created")
else:
    print(f"Directory '{new_directory}' already exists")

# List files and directories
items = os.listdir('.')
print(items)

import os

# Specify the directory path
directory_path = "."  # Use "." for the current directory

try:
    # List contents of the directory
    contents = os.listdir(directory_path)
    print("Contents of the directory:")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")

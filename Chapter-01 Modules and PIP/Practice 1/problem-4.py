import os  # Import the os module to interact with the operating system

# Specify the directory path to explore
# Use "." to refer to the current working directory
directory_path = "."

try:
    # Attempt to list all contents of the specified directory
    contents = os.listdir(directory_path)  # Retrieve the directory contents as a list
    print("Contents of the directory:")    # Print a header for the output
    
    # Loop through each item in the directory and print it
    for item in contents:
        print(item)  # Output the name of each file or subdirectory

# Handle the case where the directory doesn't exist
except FileNotFoundError:
    print(f"Error: The directory '{directory_path}' does not exist.")

# Handle the case where the program doesn't have permission to access the directory
except PermissionError:
    print(f"Error: Permission denied to access '{directory_path}'.")

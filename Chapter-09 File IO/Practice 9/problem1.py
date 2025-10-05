f = open("poem.txt")  # Open the file
content = f.read() # Read the content of the file
if "twinkle" in content:  # Check if "twinkle" is in the content
    print("The word twinkle is present in the content")
else:
    print("The word twinkle is not present in the content")
f.close()  # Close the file


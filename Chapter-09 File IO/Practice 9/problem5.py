# words = ["Donkey", "Ganda", "bad"]

# with open("file.txt", "r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(words, "#" * len(word))

# with open("file.txt", "w") as f:
#     f.write(content)
words = ["Donkey", "Ganda", "bad"]

try:
    with open("file.txt", "r") as f:
        content = f.read()

    for word in words:
        content = content.replace(word, "#" * len(word))

    with open("file.txt", "w") as f:
        f.write(content)

except FileNotFoundError:
    print("The file 'file.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
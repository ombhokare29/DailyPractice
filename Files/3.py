# Writing to a file (creates file if not exists)
file = open("sample.txt", "w")

file.write("Hello, this is my first file!\n")
file.write("Learning Python file handling.")

file.close()


# Read file content
file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()

# Add data without deleting old content
file = open("sample.txt", "a")
file.write("\nThis line is appended later.")
file.close()

file = open("sample.txt", "r")

for line in file:
    print(line.strip())

file.close()

# No need to close file manually
with open("sample.txt", "r") as file:
    data = file.read()
    print(data)

with open("sample.txt", "r") as file:
    data = file.read()
    words = data.split()
    print("Total words:", len(words))


with open("sample.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as target:
    target.write(content)

print("File copied successfully!")
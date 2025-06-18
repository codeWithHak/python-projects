# read
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

# read binary
file = open("data.txt", "rb")
content = file.read()
print(content)
file.close()

# append and read
file = open("data.txt", "a+")
content = file.read()
print(content)
file.write("AAhhooo paajji")
file.close()

# open file with 'with'
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
    file.close()
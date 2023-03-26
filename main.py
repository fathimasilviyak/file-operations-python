# Read file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write to file
# with open("my_file.txt", mode="w") as file:
#     file.write("Hello world!")
#
# Append data to existing file
with open("my_file.txt", mode="a") as file:
    file.write("\nI also like ice cream.")
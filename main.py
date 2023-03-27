# Read file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Another method to open file, which doesn't need to separately close the file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# # Absolute file path
# with open("C:/Users/silviya/Desktop/python/project/test.txt") as file:
#     contents = file.read()
#     print(contents)


# Relative file path
with open("../test.txt") as file:
    contents = file.read()
    print(contents)


# Write to file
# with open("my_file.txt", mode="w") as file:
#     file.write("Hello world!")
#
# Append data to existing file
# with open("my_file.txt", mode="a") as file:
#     file.write("\nI also like ice cream.")

# Write to non-existent file
# with open("new_file.txt", mode="w") as file:
#     file.write("This is a new file")

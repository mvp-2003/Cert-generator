import os

with open("names.txt") as file:
    names_list = file.read().splitlines()

# Convert the list to a string
names_list_str = str(names_list)

# Write the string to list.py
with open("list.txt", "w") as file:
    file.write("names_list = " + names_list_str)
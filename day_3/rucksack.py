import string

with open("input.txt", "r") as file:
    lines = file.readlines()

rucsacks = [line.strip("\n") for line in lines]

common_items = []
for rucsack in rucsacks:
    n_items = len(rucsack)
    middle = int(n_items/2)
    first_compartment = rucsack[:middle]
    second_compartment = rucsack[middle:]
    common_items.append(list(set(first_compartment).intersection(second_compartment))[0])

lowercase = [*string.ascii_lowercase]
uppercase = [*string.ascii_uppercase]
priorities_lowercase = [lowercase.index(character) + 1 for character in lowercase]
priorities_uppercase = [uppercase.index(character) + 27 for character in uppercase]

priorities = []
for i in range(len(lowercase)):
    for item in common_items:
        if item == lowercase[i]:
            print(f"item: {item}, low: {lowercase[i]}, priority: {priorities_lowercase[i]}")

            priorities.append(priorities_lowercase[i])
        elif item == uppercase[i]:
            print(f"item: {item}, up: {uppercase[i]}, priority: {priorities_uppercase[i]}")

            priorities.append(priorities_uppercase[i])

sum_priorities = sum(priorities)
print(f"Sum of priorities: {sum_priorities}")

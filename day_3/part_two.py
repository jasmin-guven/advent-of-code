import string

with open("input.txt", "r") as file:
    lines = file.readlines()

rucsacks = [line.strip("\n") for line in lines]
n = 3
groups = [rucsacks[i * n:(i + 1) * n] for i in range((len(rucsacks) + n - 1) // n)]

badges = [list(set(groups[i][0]).intersection(groups[i][1], groups[i][2]))[0] for i in range(len(groups))]

lowercase = [*string.ascii_lowercase]
uppercase = [*string.ascii_uppercase]
priorities_lowercase = [lowercase.index(character) + 1 for character in lowercase]
priorities_uppercase = [uppercase.index(character) + 27 for character in uppercase]

priorities = []
for i in range(len(lowercase)):
    for badge in badges:
        if badge == lowercase[i]:
            print(f"badge: {badge}, low: {lowercase[i]}, priority: {priorities_lowercase[i]}")

            priorities.append(priorities_lowercase[i])
        elif badge == uppercase[i]:
            print(f"item: {badge}, up: {uppercase[i]}, priority: {priorities_uppercase[i]}")

            priorities.append(priorities_uppercase[i])
            
sum_priorities = sum(priorities)
print(f"Sum of priorities: {sum_priorities}")
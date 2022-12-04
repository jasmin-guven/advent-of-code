def to_int(value: str) -> int:
    try:
        stoi = int(value)
        return stoi
    except ValueError as error:
        print(f"could not convert to int: {error}")
        return 0

input_file = "day_1/input.txt"
with open(input_file, "r") as file:
    lines = file.read()
split_input = lines.split("\n\n")

elves = [[line.split("\n")] for line in split_input]
all_calories = [[to_int(calorie) for calorie in calories] for elf in elves for calories in elf]
total_calories_per_elf = [sum(calories_by_elf) for calories_by_elf in all_calories]
most_calories = max(total_calories_per_elf)
print(f"The most calories carried by an elf is: {most_calories}")
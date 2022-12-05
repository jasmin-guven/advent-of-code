import csv
import numpy as np 


rows = []
with open("input.txt", "r") as file:
    csvreader = csv.reader(file)
    sections = [section.split("-") for line in csvreader for section in line]

n = 2
pairs = [sections[i * n:(i + 1) * n] for i in range((len(sections) + n - 1) // n)]

all_ranges = [np.arange(int(section[0]), int(section[1])+1, 1) for pair in pairs for section in pair]

paired_ranges = [all_ranges[i * n:(i + 1) * n] for i in range((len(all_ranges) + n - 1) // n)]

counter = 0
for pair in paired_ranges:
    set_1 = set(pair[0])
    set_2 = set(pair[1])
    subset_1 = set_1.issubset(set_2)
    subset_2 = set_2.issubset(set_1)
    if subset_1:
        counter += 1
    elif subset_2:
        counter += 1

print(f"{counter} pairs fully contain each other")

counter = 0
for pair in paired_ranges:
    set_1 = set(pair[0])
    set_2 = set(pair[1])

    intersection = set_1.intersection(set_2)
    if len(intersection) > 0:
        counter += 1

print(f"{counter} pairs intersect each other")
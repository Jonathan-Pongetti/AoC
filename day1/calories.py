

with open('input.txt') as f:
    lines = f.readlines()

most_calories = []
current_elf = 0

for lineno, line in enumerate(lines):
    if line.strip():
        current_elf += int(line)

    else: 
        most_calories.append(current_elf)

        current_elf = 0

most_calories.sort(reverse=True)
print(sum(most_calories[:3]))
current_elf_cal: int = 0
highest_elf_cal: int = 0
second_elf_cal: int = 0
third_elf_cal: int = 0

input_list = open(r"Day1/input.txt", "r")
for line in input_list:
    if line == "\n":
        if current_elf_cal >= highest_elf_cal:
            third_elf_cal = second_elf_cal
            second_elf_cal = highest_elf_cal
            highest_elf_cal = current_elf_cal
        current_elf_cal = 0
    else:
        current_elf_cal = current_elf_cal + int(line)
input_list.close()

print(highest_elf_cal)
print(highest_elf_cal + second_elf_cal + third_elf_cal)

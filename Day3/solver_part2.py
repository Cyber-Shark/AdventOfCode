from string import ascii_letters

elf1_sack: str = ""
elf2_sack: str = ""
elf3_sack: str = ""
counter: int = 0
common_char: str = ""
rearrange_list: str = ""
priority_number: int = 1
pri_dict = {}
priority_sum: int = 0

input_list = open(r"Day3/day3_input.txt", "r")
for line in input_list:
    elf3_sack = elf2_sack
    elf2_sack = elf1_sack
    elf1_sack = line
    counter += 1
    if counter == 3:
        for item in elf1_sack:
            if item in elf2_sack and item in elf3_sack:
                rearrange_list = rearrange_list + item
                counter = 0
                break

for letter in ascii_letters:
    pri_dict[letter] = priority_number
    priority_number += 1
# print(pri_dict)


for thing in rearrange_list:
    priority_sum = priority_sum + pri_dict[thing]
print(priority_sum)

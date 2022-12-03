from string import ascii_letters

current_sack: str = ""
current_sack_len: int = 0
current_sack_left: str = ""
current_sack_right: str = ""
common_char: str = ""
rearrange_list: str = ""
priority_number: int = 1
pri_dict = {}
priority_sum: int = 0


def left(s, amount):
    return s[:amount]


def right(s, amount):
    return s[-amount:]


def mid(s, offset, amount):
    return s[offset : offset + amount]


input_list = open(r"Day3/day3_input.txt", "r")
for line in input_list:
    current_sack = line
    current_sack_len = len(current_sack) // 2
    current_sack_left = left(current_sack, current_sack_len)
    current_sack_right = mid(current_sack, current_sack_len, current_sack_len)
    print(current_sack)
    print(current_sack_left)
    print(current_sack_right)
    for item in current_sack_left:
        if item in current_sack_right:
            rearrange_list = rearrange_list + item
            print(item)
            break

print(rearrange_list)

for letter in ascii_letters:
    pri_dict[letter] = priority_number
    priority_number += 1
# print(pri_dict)


for thing in rearrange_list:
    print(thing)
    print(pri_dict[thing])
    priority_sum = priority_sum + pri_dict[thing]
print(priority_sum)

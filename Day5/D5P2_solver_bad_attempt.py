# [D]                     [N] [F]
# [H] [F]             [L] [J] [H]
# [R] [H]             [F] [V] [G] [H]
# [Z] [Q]         [Z] [W] [L] [J] [B]
# [S] [W] [H]     [B] [H] [D] [C] [M]
# [P] [R] [S] [G] [J] [J] [W] [Z] [V]
# [W] [B] [V] [F] [G] [T] [T] [T] [P]
# [Q] [V] [C] [H] [P] [Q] [Z] [D] [W]
#  1   2   3   4   5   6   7   8   9


def convert(string):
    list1 = []
    list1[:0] = string
    return list1


stack1: list = convert("QWPSZRHD")
stack2: list = convert("VBRWQHF")
stack3: list = convert("CVSH")
stack4: list = convert("HFG")
stack5: list = convert("PGJBZ")
stack6: list = convert("QTJHWFL")
stack7: list = convert("ZTWDLVJN")
stack8: list = convert("DTZCJGHF")
stack9: list = convert("WPVMBH")

stack_list = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

column_from = 0
column_to = 0
box_qty = 0
line_count = 0
# move 1 from 3 to 9
input_list = open(r"Day5/day5steps.txt", "r")
print(stack_list)
for line in input_list:
    aa, box_qty_str, cc, column_from_str, ee, column_to_str = line.split()

    box_qty = int(box_qty_str)
    stack_from = int(column_from_str) - 1
    stack_to = int(column_to_str) - 1

    for box in range(box_qty):
        boxes

        stack_list[stack_to] += stack_list[stack_from].pop(-box_qty)
        box_qty

print(stack_list)

final = stack_list.pop()
print(final)

[
    ["Q", "P", "S", "Z", "R", "H", "D", "R"],
    ["V", "B", "W", "Q", "H", "F"],
    ["C", "H", "J"],
    ["H", "F", "G", "B"],
    ["P", "Z"],
    ["Q", "T", "J", "H", "W", "F", "L"],
    ["Z", "T", "W", "D", "L", "V", "J", "N", "G"],
    ["D", "T", "Z", "C", "J", "G", "H", "F", "W"],
    ["W", "P", "V", "M", "B", "H", "V", "S"],
]

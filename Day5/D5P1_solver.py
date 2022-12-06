# [D]                     [N] [F]
# [H] [F]             [L] [J] [H]
# [R] [H]             [F] [V] [G] [H]
# [Z] [Q]         [Z] [W] [L] [J] [B]
# [S] [W] [H]     [B] [H] [D] [C] [M]
# [P] [R] [S] [G] [J] [J] [W] [Z] [V]
# [W] [B] [V] [F] [G] [T] [T] [T] [P]
# [Q] [V] [C] [H] [P] [Q] [Z] [D] [W]
#  1   2   3   4   5   6   7   8   9

stack1: str = "QWPSZRHD"
stack2: str = "VBRWQHF"
stack3: str = "CVSH"
stack4: str = "HFG"
stack5: str = "PGJBZ"
stack6: str = "QTJHWFL"
stack7: str = "ZTWDLVJN"
stack8: str = "DTZCJGHF"
stack9: str = "WPVMBH"

stack_list = [stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]


# move 1 from 3 to 9
input_list = open(r"Day5/day5steps.txt", "r")

for line in input_list:
    _, box_qty_str, _, column_from_str, _, column_to_str = line.split()
    box_qty = int(box_qty_str)
    column_to = int(column_to_str)
    column_from = int(column_from_str)
    # print(box_qty)
    # print(column_from)
    # print(stack_list[int(column_from)])
    # print(column_to)

    for box in range(box_qty):
        stack_list[column_to - 1] += stack_list[column_from - 1][-1]
        stack_list[column_from - 1] = stack_list[column_from - 1][:-1]
        # print(stack_list[int(column_from) - 1])
        # print(stack_list[int(column_to) - 1])
        print(stack_list)

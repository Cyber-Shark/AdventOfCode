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

column_from = 0
column_to = 0
box_qty = 0
run = 0

input_list = open(r"Day5/day5steps.txt", "r")

for line in input_list:
    aa, box_qty, cc, column_from, ee, column_to = line.split()
    box_qty = int(box_qty)

    stack_list[int(column_to) - 1] += stack_list[int(column_from) - 1][-box_qty:]
    stack_list[int(column_from) - 1] = stack_list[int(column_from) - 1][:-box_qty]

print(stack_list)

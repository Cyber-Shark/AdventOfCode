class Tree:
    def __init__(self, x_coord: int, y_coord: int, height: int):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.height = height
        self.visible_top = True
        self.visible_bottom = True
        self.visible_left = True
        self.visible_right = True
        self.view_top = 0
        self.view_bottom = 0
        self.view_left = 0
        self.view_right = 0


print("Calculating:")
input_list = open(r"Day8/Day8input.txt", "r")
tree_list: list = []

x_coord = 1
y_coord = 1
highest_scenic = 0

for line in input_list:
    tree_row = list(line)
    tree_row.pop()
    for tree_str in tree_row:
        tree = int(tree_str)
        tree_list.append(Tree(x_coord, y_coord, tree))
        x_coord += 1
    x_coord = 1
    y_coord += 1


for target_tree in tree_list:
    # Top
    offset = 1
    for other_tree in tree_list:
        if (
            other_tree.x_coord == target_tree.x_coord
            and other_tree.y_coord == target_tree.y_coord - offset
            and other_tree.height >= target_tree.height
        ):
            offset += 1
        else:
            target_tree.view_top = offset
            offset = 1
        # Bottom
        if (
            other_tree.x_coord == target_tree.x_coord
            and other_tree.y_coord > target_tree.y_coord
            and other_tree.height >= target_tree.height
        ):
            target_tree.visible_bottom = False
        # Left
        if (
            other_tree.x_coord > target_tree.x_coord
            and other_tree.y_coord == target_tree.y_coord
            and other_tree.height >= target_tree.height
        ):
            target_tree.visible_left = False
        # Right
        if (
            other_tree.x_coord < target_tree.x_coord
            and other_tree.y_coord == target_tree.y_coord
            and other_tree.height >= target_tree.height
        ):
            target_tree.visible_right = False
        # Logic
        current_scenic = (
            target_tree.view_top
            * target_tree.view_bottom
            * target_tree.view_left
            * target_tree.view_right
        )
        if current_scenic > highest_scenic:
            highest_scenic = current_scenic

print(highest_scenic)

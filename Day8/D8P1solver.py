class Tree:
    def __init__(self, x_coord: int, y_coord: int, height: int):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.height = height
        self.visible_top = True
        self.visible_bottom = True
        self.visible_left = True
        self.visible_right = True

    def visible_all(self):
        return (
            self.visible_top
            or self.visible_bottom
            or self.visible_left
            or self.visible_right
        )


print("Calculating:")
input_list = open(r"Day8/Day8input.txt", "r")
tree_list: list = []

x_coord = 1
y_coord = 1
count = 0

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
    for other_tree in tree_list:
        if (
            other_tree.x_coord == target_tree.x_coord
            and other_tree.y_coord < target_tree.y_coord
            and other_tree.height >= target_tree.height
            # and target_tree.y_coord != 1
        ):
            target_tree.visible_top = False
        # Bottom
        if (
            other_tree.x_coord == target_tree.x_coord
            and other_tree.y_coord > target_tree.y_coord
            and other_tree.height >= target_tree.height
            # and target_tree.y_coord != 99
        ):
            target_tree.visible_bottom = False
        # Left
        if (
            other_tree.x_coord > target_tree.x_coord
            and other_tree.y_coord == target_tree.y_coord
            and other_tree.height >= target_tree.height
            # and target_tree.x_coord != 1
        ):
            target_tree.visible_left = False
        # Right
        if (
            other_tree.x_coord < target_tree.x_coord
            and other_tree.y_coord == target_tree.y_coord
            and other_tree.height >= target_tree.height
            # and target_tree.x_coord != 99
        ):
            target_tree.visible_right = False
    # Logic
    if target_tree.visible_all():
        # target_tree.visible_top == True
        # or target_tree.visible_bottom == True
        # or target_tree.visible_left == True
        # or target_tree.visible_right == True
        count += 1

# for tree in tree_list:
#     print(f"X:{tree.x_coord} Y:{tree.y_coord} Bottom Vis:{tree.visible_bottom}")
print(count)

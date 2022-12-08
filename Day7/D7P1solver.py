input_list = open(r"Day7/Day7Input.txt", "r")
current_dir_list: list = []
line_no: int = 0
dir_set: set = set()
dir_list: list = []
small_dirs: list = []
file_dict: dict = {}

for line in input_list:
    line_no += 1

    if line[0:6] == "$ cd /":
        current_dir_list = ["/"]
    elif line[0:7] == "$ cd ..":
        current_dir_list.pop()
    elif line[0:4] == "$ cd":
        current_dir_list.append(line[5:].replace("\n", "/"))
        dir_set.add("".join(current_dir_list))
    elif line[0:4] == "$ ls":
        pass
    elif line[0:3] == "dir":
        pass
    else:
        file_size_str, file_name = line.split()
        file_size = int(file_size_str)
        file_dict["".join(current_dir_list) + file_name] = file_size

for path in dir_set:
    path_sizes = [val for key, val in file_dict.items() if path in key]
    path_sum = sum(path_sizes)
    if path_sum < 100000:
        small_dirs.append(path_sum)

print(sum(small_dirs))

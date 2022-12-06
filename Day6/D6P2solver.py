input_list = open(r"Day6/Day6input.txt", "r")

for line in input_list:
    print(line)

index_num = 0
read_frame_len = 14
char_list = list(line)
index_num = 14

read_frame: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# read_frame: list = []

read_item_counter = 0

for read_item in range(read_frame_len):

    read_frame[read_item_counter] = char_list[read_item_counter]
    read_item_counter += 1

    print(read_frame)

for frame_shift in char_list:
    index_num += 1
    read_frame.pop(0)
    read_frame.append(char_list[index_num])

    if len(set(read_frame)) == len(read_frame):
        print(index_num)
        print(read_frame)
        print(char_list[3036])
        break

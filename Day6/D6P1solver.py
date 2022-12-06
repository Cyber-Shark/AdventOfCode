input_list = open(r"Day6/Day6input.txt", "r")

for line in input_list:
    print(line)

char1 = "d"
char2 = "c"
char3 = "b"
char4 = "c"
index_num = 0

char_list = list(line)
print(char_list)

for character in char_list:
    char4 = char3
    char3 = char2
    char2 = char1
    char1 = character

    read_frame = [char4, char3, char2, char1]
    print(read_frame)

    index_num += 1

    if len(set(read_frame)) == len(read_frame):
        print(index_num)
        break

print(char_list[index_num - 4])
print(char_list[index_num - 3])
print(char_list[index_num - 2])
print(char_list[index_num - 1])
print(char_list[index_num])

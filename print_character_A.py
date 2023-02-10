import math

# print character A
def print_a_character(start, height):
    line_has_space = height - 1
    middle_line = math.ceil(height / 2)

    for i in range(0, height):

        # print spaces
        for j in range(line_has_space, i, -1):
            print(" ", end="")

        range_num = range(0, start)
        range_num_len = len(range_num)
        for k in range_num:
            if k == 0:
                print("*", end="")
            elif range_num_len > 1 and k == range_num_len - 1:
                print("*", end="")
            else:
                if i == middle_line:
                    print("*", end="")
                else:
                    print(" ", end="")

        start += 2
        print("")


if __name__ == '__main__':
    start = 1
    height = 5
    for i in range(height, height + 10):
        print_a_character(start, i)



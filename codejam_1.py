def recursive_check(num_to_split: int):
    num_b = int(get_four_mask(str(num_to_split)))
    num_a = num_to_split - num_b
    return num_a, num_b


def contains_digit_four(num: int):
    for char in str(num):
        if char == '4':
            return True
    return False


def get_four_mask(s: str):
    mask = list(s)
    for i in range(0, s.__len__()):
        if s[i] == '4':
            mask[i] = '1'
        else:
            mask[i] = '0'
    return "".join(mask)


if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    n_cases = int(input())  # read a line with a single integer
    for i in range(1, n_cases + 1):
        target_num = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        num_a, num_b = recursive_check(target_num[0])
        print("Case #{}: {} {}".format(i, num_a, num_b))
        # check out .format's specification for more formatting options

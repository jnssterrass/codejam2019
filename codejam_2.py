if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    n_cases = int(input())  # read a line with a single integer
    for i in range(1, n_cases + 1):
        dimensions = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        route = input().split(" ")  # read a list of integers, 2 in this case
        new_route = route[0]
        new_route = new_route.replace('E','1').replace('S', 'E').replace('1', 'S')
        print("Case #{}: {} ".format(i, new_route))
        # check out .format's specification for more formatting options

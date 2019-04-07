def get_factors(x: int):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return  factors

def mcd(a, b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a


def lcm(x, y):
    if x > y:
        z = x
    else:
        z = y

    while True:
        if (z % x == 0) and (z % y == 0):
            lcm = z
            break
        z += 1

    return lcm


def get_english_char_at(position: int):
    chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return chars[position]


if __name__ == '__main__':
    # input() reads a string with a line of input, stripping the ' ' (newline) at the end.
    # This is all you need for most Code Jam problems.
    n_cases = int(input())  # read a line with a single integer
    for i in range(1, n_cases + 1):
        max_prime, length = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        prime_products_list = [int(s) for s in input().split(" ")]  # read a list of integers, 2 in this case
        mcd_list = []
        for j in range(0, length - 1):
            a = prime_products_list[j]
            b = prime_products_list[j + 1]

            prime1 = mcd(a, b)
            if j == 0:
                if a == b:
                    prime1 = get_factors(a)[2]
                prime0 = int(a / prime1)
                mcd_list.append(prime0)
            mcd_list.append(prime1)
            if j == length - 2:
                prime0 = int(b / prime1)
                mcd_list.append(prime0)
        alphabet_numbers = mcd_list.copy()
        alphabet_numbers = list(dict.fromkeys(alphabet_numbers))
        alphabet_numbers.sort()

        final_message = []
        for char_num in mcd_list:
            char = get_english_char_at(alphabet_numbers.index(char_num))
            final_message.append(char)

        print("Case #{}: {} ".format(i, ''.join(final_message)))
        # check out .format's specification for more formatting options

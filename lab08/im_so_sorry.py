def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n


# print(blocks(8))
# print(blocks(0))
# print(blocks(-1))
# print(blocks(1))
# print(blocks(100))


def sum_of_digits(n):
    if not (type(n) is int and n > 0):
        raise ValueError("Input needs to be a positive integer")
    return n if n <= 10 else sum_of_digits(n // 10) + (n % 10)


print(sum_of_digits(-3))

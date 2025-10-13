def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n


def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)


def has_6_7(n):
    return "67" in str(n)


def count_of_6_7_s(n):
    s = str(n)
    count = 0
    for i in range(len(s)-1):
        if s[i] == "6" and s[i+1] == "7":
            count += 1
    return count


def print_count_down(n):
    if n <= 0:
        print("BOOM")
    else:
        print(n)
        print_count_down(n - 1)


print(factorial(5))
print(factorial(0))
print(factorial(52))
print(factorial(67))


print(blocks(-1))
print(blocks(1))
print(blocks(5))
print(blocks(10))

print("---------------")
print_count_down(5)
print_count_down(0)
print_count_down(52)
print_count_down(67)


print("---------------")
print(has_6_7(67))
print(has_6_7(123))
print(has_6_7(123456789))
print(has_6_7(12345678967))

print(count_of_6_7_s(67))
print(count_of_6_7_s(123))
print(count_of_6_7_s(123456789))
print(count_of_6_7_s(12676767676767678966))

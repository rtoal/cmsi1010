def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n


# Here are sample calls to the blocks function just for fun:
print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
print(blocks(995))

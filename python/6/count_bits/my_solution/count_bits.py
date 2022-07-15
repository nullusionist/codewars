def count_bits(n):
    b = format(n,"b")
    return sum(int(s) for s in b)
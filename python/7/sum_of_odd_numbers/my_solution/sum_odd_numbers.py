def row_sum_odd_numbers(n):
    sum = 0
    start = ((n - 1) * n) + 1
    end = start + (n * 2)
    for num in range (start, end):
        if num % 2 != 0:
            sum += num
    return sum
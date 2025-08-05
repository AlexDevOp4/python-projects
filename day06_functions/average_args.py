def avg_sum(*args):
    total = 0

    for num in args:
        total += num

    return total / len(args)

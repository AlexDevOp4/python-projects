def sum_of_even(numbers):
    is_even = []

    for num in numbers:
        if num % 2 == 0:
            is_even.append(num)

    total = sum(is_even)
    return total

print(sum_of_even([1,2,3,4,5]))
def sort_nums(arr):
    x = arr
    n = len(x)

    # Traverse through all list elements
    for i in range(n):

        # Traverse the list from 0 to n-i-1
        # (The last element will already be in place after first pass, so no need to re-check)
        for j in range(0, n-i-1):

            # Swap if current element is greater than next
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
    return x

print(sort_nums([5,10,1,4]))

def remove_duplicates(lst):
    seen = set()
    result = []

    for i in lst:
        if i not in seen:
            seen.add(i)
            result.append(i)

    print(result)
    return result


lst = [1, 2, 2, 3, 4, 4, 5]
remove_duplicates(lst)
# Output: [1, 2, 3, 4, 5]

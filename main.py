def digital_root(n):
    numbers = []
    for i in str(n):
        numbers.append(int(i))
    addAll = sum(numbers)
    if len(str(addAll)) != 1:
        addAll = digital_root(addAll)

    return addAll

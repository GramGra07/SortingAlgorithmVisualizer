def is_sorted(array):
    for i in range(len(array) - 1):
        if array[i] > array[i + 1]:
            return False
    return True

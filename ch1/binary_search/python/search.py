import math

def find_middle(arr: list) -> int:
    low = arr[0]
    high = arr[-1]
    middle_index = math.floor(len(arr) / 2)

    return middle_index

def binary_search(arr: list, val: int) -> int:
    "running binary search..."
    
    middle_ix = find_middle(arr)
    middle_ix_value = arr[middle_ix]

    if val == middle_ix_value:
        return middle_ix

    elif val > middle_ix_value:
        return -1

    elif val < middle_ix_value:
        return -1

    else:
        return -1


if __name__ == '__main__':
    print("search")
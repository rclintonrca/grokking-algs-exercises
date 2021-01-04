import math


def find_middle(arr: list) -> int:
    low = arr[0]
    high = arr[-1]
    middle_index = math.floor(len(arr) / 2)

    return middle_index

def binary_search(arr: list, val: int, base_ix=0) -> int:
    "running binary search..."
    
    if not arr:
        return None

    middle_ix = find_middle(arr)
    middle_ix_value = arr[middle_ix]

    if val == middle_ix_value:
        return middle_ix + base_ix

    elif val > middle_ix_value:
        arr_slice = arr[middle_ix + 1 : ]
        return binary_search(arr_slice, val, base_ix=middle_ix+1)

    elif val < middle_ix_value:
        arr_slice = arr[0:middle_ix]
        return binary_search(arr_slice, val, base_ix=base_ix)



if __name__ == '__main__':
    pass

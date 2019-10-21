def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """

    # TODO: Write your first_and_last function here
    # Note that you may want to write helper functions to find the start
    # index and the end index
    results = []
    index = binary_search(number, arr, 0, len(arr) - 1)
    if index < 0:
        return [index, index]
    first = find_first(number, arr, index)
    last = find_last(number, arr, index)
    print(index)
    print(first)
    print(last)
    results.append(first)
    results.append(last)

    return results

def binary_search(target, source, start_i, end_i):
    if start_i > end_i:
        return -1
    mid_i = (end_i + start_i) // 2
    mid = source[mid_i]
    if mid == target:
        return mid_i
    elif mid > target:
        return binary_search(target, source, start_i, mid_i - 1)
    else:
        return binary_search(target, source, mid_i + 1, end_i)

def find_first(target, source, index):
    if index is None:
        return None

    while source[index] == target:
        if index == 0:
            return 0
        if source[index - 1] == target:
            index -= 1
        else:
            return index

def find_last(target, source, index):
    if index is None:
        return None

    while source[index] == target:
        if index == len(source) - 1:
            return len(source) - 1
        if source[index + 1] == target:
            index += 1
        else:
            return index

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)
def rotated_array_search(input_list, number):
    if not input_list:
        return -1
    first = input_list[0]
    if number == first:
        return 0
    size = len(input_list) - 1
    max_val = find_max(input_list, 0, size)
    if number > first:
        return binary_search(input_list, number, 1, max_val)
    else:
        return binary_search(input_list, number, max_val + 1, size)


def binary_search(input_list, number, start, end):
    if start > end:
        return -1
    crt = (start + end) // 2
    if input_list[crt] == number:
        return crt
    elif input_list[crt] < number:
        return binary_search(input_list, number, crt + 1, end)
    else:
        return binary_search(input_list, number, start, crt - 1)


def find_max(input_list, start, end):
    if end < start:
        return -1

    crt = (start + end) // 2
    if input_list[crt] > input_list[crt + 1]:
        return crt
    if input_list[crt] < input_list[crt - 1]:
        return crt - 1

    if input_list[crt] >= input_list[end]:
        return find_max(input_list, start, crt - 1)
    else:
        return find_max(input_list, crt + 1, end)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))
# Should print 0
print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))
# Should print 5
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 8))
# Should print 2
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 1))
# Should print 3
print(rotated_array_search([6, 7, 8, 1, 2, 3, 4], 10))
# Should print -1
print(rotated_array_search([1, 1, 1, 1, 1, 1, 1], 0))
# Should print -1
print(rotated_array_search([1, 1, 1, 1, 1, 0, 0], 1))
# Should print 0
print(rotated_array_search([5, 6, 1, 2, 3, 4], None))
# Should print -1
print(rotated_array_search([5, 6, 1, 2, 3, 4], "x"))
# Should print -1
print(rotated_array_search([], 1))
# Should print -1
print(rotated_array_search(["c", "a", "b"], 1))
# Should print -1

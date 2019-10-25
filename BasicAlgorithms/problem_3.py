def rearrange_digits(input_list):
    input_list = reverse_mergesort(input_list)

    a = ""
    b = ""
    if len(input_list) % 2 == 1:
        a += str(input_list.pop(0))
    for i in range(0, len(input_list)):
        if i % 2 == 0:
            b += str(input_list[i])
        else:
            a += str(input_list[i])
    return [int(a), int(b)]


def reverse_mergesort(items):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]

    left = reverse_mergesort(left)
    right = reverse_mergesort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


test_case1 = [4, 6, 2, 5, 9, 8]
test_case2 = [1, 2, 3, 4, 5]
test_case3 = [0, 0, 0, 1, 1, 1]
test_case4 = [0, 0, 1, 1, 1]
test_case5 = [0, 0, 0, 1, 1]

print(rearrange_digits(test_case1))
# Should print [852, 964]
print(rearrange_digits(test_case2))
# Should print [531, 42]
print(rearrange_digits(test_case3))
# Should print [100, 110]
print(rearrange_digits(test_case4))
# Should print [110, 10]
print(rearrange_digits(test_case5))
# Should print [100, 10]
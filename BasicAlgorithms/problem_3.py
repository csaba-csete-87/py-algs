def rearrange_digits(input_list):
    input_list.sort(reverse=True)
    a = ""
    b = ""
    if len(input_list) % 2 == 1:
        a += str(input_list.pop(0))
    for i in range(0, len(input_list)):
        if i % 2 == 0:
            a += str(input_list[i])
        else:
            b += str(input_list[i])
    return [int(a), int(b)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_case1 = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case1)
test_case2 = [[1, 2, 3, 4, 5], [542, 31]]
test_function(test_case2)
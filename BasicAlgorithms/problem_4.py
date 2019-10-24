def sort_012(input_list):
    i = 0
    i_0 = 0
    i_2 = len(input_list) - 1

    while i <= i_2:
        crt = input_list[i]
        if crt < 1:
            if input_list[i_0] != 0:
                start = input_list[i_0]
                input_list[i_0] = crt
                input_list[i] = start
            i += 1
            i_0 += 1
        elif crt > 1:
            if input_list[i_2] < 2:
                end = input_list[i_2]
                input_list[i_2] = crt
                input_list[i] = end
                if end == 1:
                    i += 1
            i_2 -= 1
        else:
            i += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([1, 1, 1, 0, 0, 0, 2, 2, 2])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 2, 0, 0, 0, 1, 0, 2])
test_function([2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1])
test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

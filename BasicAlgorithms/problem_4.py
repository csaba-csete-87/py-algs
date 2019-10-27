def sort_012(input_list):
    if not input_list or len(input_list) < 2:
        return input_list
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


test_list_1 = [1, 1, 1, 0, 0, 0, 2, 2, 2]
print(sort_012(test_list_1))
# Should print [0, 0, 0, 1, 1, 1, 2, 2, 2]
test_list_2 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
print(sort_012(test_list_2))
# Should print [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
test_list_3 = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
print(sort_012(test_list_3))
# Should print [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test_list_4 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print(sort_012(test_list_4))
# Should print [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
test_list_5 = [0, 0, 2, 0, 0, 0, 1, 0, 2]
print(sort_012(test_list_5))
# Should print [0, 0, 0, 0, 0, 0, 1, 2, 2]
test_list_6 = [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
print(sort_012(test_list_6))
# Should print [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
test_list_7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(sort_012(test_list_7))
# Should print [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
test_list_8 = []
print(sort_012(test_list_8))
# Should print []
test_list_9 = None
print(sort_012(test_list_9))
# Should print None

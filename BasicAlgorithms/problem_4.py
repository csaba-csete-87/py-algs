def sort_012(input_list):
    i = 0
    for n in range(0, len(input_list) - 1):
        crt = input_list[i]
        if crt < 1:
            input_list.insert(0, input_list.pop(i))
            i += 1
        elif crt > 1:
            input_list.append(input_list.pop(i))
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

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
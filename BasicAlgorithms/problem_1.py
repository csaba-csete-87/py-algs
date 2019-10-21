def sqrt(number):
    if number < 0:
        print("Sqrt of negative numbers not supported yet.")
        return None
    elif number < 2:
        return number
    else:
        return floored_sqrt(number, 0, number)


def floored_sqrt(target, low, high):
    number = (low + high) // 2
    if is_floored_sqrt(number, target):
        return number
    elif number * number < target:
        return floored_sqrt(target, number, high)
    else:
        return floored_sqrt(target, 0, number)


def is_floored_sqrt(nr, target):
    return nr * nr <= target < (nr + 1) * (nr + 1)


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (7 == sqrt(63)) else "Fail")
print("Pass" if (None == sqrt(-1)) else "Fail")

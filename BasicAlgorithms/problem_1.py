def sqrt(number):
    if not isinstance(number, (int, long, float)):
        print("Error: \"" + str(number) + "\" is not a supported number.")
        return None
    if number < 0:
        print("Error: Sqrt of negative numbers not supported yet.")
        return None
    elif number < 1:  # normally sqrt of these numbers tend to 1, but we are flooring them so they will always be 0
        return 0
    elif number < 2:
        return 1
    else:
        return int(floored_sqrt(number, 0, number))


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


print(sqrt(9))
# prints 3
print(sqrt(16))
# prints 4
print(sqrt(0))
# prints 0
print(sqrt(1))
# prints 1
print(sqrt(27))
# prints 5
print(sqrt(63))
# prints 7
print(sqrt(64))
# prints 8
print(sqrt(1000001))
# prints 1000
print(sqrt(100.25))
# prints 10
print(sqrt(0.5))
# prints 0
print(sqrt(0.9999))
# prints 0
print(sqrt(-1))  # negative number
# prints error, negative numbers not yet supported, result is None
print(sqrt("test"))  # simple text
# prints error, not a supported number, result is None
print(sqrt("10F"))  # hexadecimal number
# prints error, not a supported number, result is None

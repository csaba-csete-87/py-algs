def get_min_max(ints):
    if not ints:
        return (None, None)
    min = None
    max = None
    for i in range(0, len(ints)):
        crt = ints[i]
        if not min:
            min = crt
        elif crt < min:
            min = crt

        if not max:
            max = crt
        elif crt > max:
            max = crt

    return (min, max)


## Example Test Case of 1000 Integers
import random

l = [i for i in range(0, 1000)]  # a list containing 0 - 999
random.shuffle(l)
print(get_min_max(l))
# prints (0, 999)
print(get_min_max([]))
# prints (None, None)
print(get_min_max(None))
# prints (None, None)
print(get_min_max([1, 1, 1, 1, 1]))
# prints (1, 1)
print(get_min_max([1]))
# prints (1, 1)

def get_min_max(ints):
    min = None
    max = None
    if not ints:
        return (min, max)
    for i in range(0, len(ints)):
        crt = ints[i]
        if min == None:
            min = crt
        elif crt < min:
            min = crt

        if max == None:
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

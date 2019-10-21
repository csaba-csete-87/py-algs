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


## Example Test Case of 100 Integers
import random

l = [i for i in range(0, 100)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 99) == get_min_max(l)) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((None, None) == get_min_max(None)) else "Fail")
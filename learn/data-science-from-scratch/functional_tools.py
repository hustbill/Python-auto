def exp(base, power) :
    return base ** power

def two_to_the(power):
    return exp(2, power)


original_val =4

power_val = two_to_the(original_val)
print power_val

# use functions.partial
from functools import partial
two_to_the = partial(exp, 2)         # is now a function of one variable
print two_to_the(3)                  # 8

square_of = partial(exp, power=2)
print square_of(3)                   #9


# occasionally use map, reduce, and filter


# Zip and Argument Unpacking
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
ziplist = zip(list1, list2)   # is [('a', 1), ('b', 2), ('c', 3)]
print ziplist

pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)

print letters
print numbers

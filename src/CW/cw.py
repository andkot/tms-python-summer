import random
import sys


def gen(a, b, diff):
    while True:
        yield random.randint(a, b)
        a += diff
        b += diff


my_gen = gen(0, 0, 4)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))


def get_appendix(argv):
    res = 0
    for i in argv:
        if i.isdigit():
            res += int(i)
    return res


print(get_appendix(sys.argv))

print('+++++++++++++++++++++++++++')


class MyIterator:
    def __init__(self, n):
        self.__n = n
        self.__i = 0

    def __next__(self):
        if self.__i < self.__n:
            result = self.__i ** 2
            self.__i += 1
            return result
        else:
            raise StopIteration

    def __iter__(self):
        return self


def my_generator(n):
    for i in range(n):
        yield i ** 2


class MyGenerator:
    def __init__(self, n):
        self.__n = n
        self.__i = 0

    def generator(self):
        for i in range(self.__n):
            yield i ** 2


for i in my_generator(3):
    print(i)

print('----------------')

for i in MyIterator(3):
    print(i)

print('----------------')

for i in MyGenerator(3).generator():
    print(i)

print('----------------')

my_gen = my_generator(3)

for i in my_gen:
    print(i)

for i in my_gen:
    print(i)

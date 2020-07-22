l = ['max', 'min']

new_l = [i for i in l]
print(new_l)

new_l = [i * 2 for i in l]
print(new_l)

new_l = [k for k in l if 'n' in k]
print(new_l)

cars = [
    {
        'name': 'Solaris',
        'year': 1995
    },
    {
        'name': 'Shkoda',
        'year': 2014
    },
    {
        'name': 'Tesla',
        'year': 2020
    }
]

cars_more_n = [car for car in cars if car['year'] > 2015]
print(cars_more_n)

matrix = [[i + 3 * j for i in range(3)] for j in range(3)]
print(matrix)

old_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
}

result = {
    key: val for key, val in enumerate(['lemon', 'apple', 'dog'])
}

print(result)

new_dict = {
    v: k for k, v in old_dict.items()
}
print(new_dict)

def count_the_same_value(data: list)->dict:
    result = {}



my_pets = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets = []
for pet in my_pets:
    pet_ = pet.upper()
    uppered_pets.append(pet_)
print(uppered_pets)

uppered_pets = list(map(str.upper, my_pets))
print(uppered_pets)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 7)))
print(result)
result1 = list(map(round, circle_areas, range(1, 3)))
print(result1)

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]
results = list(zip(my_strings, my_numbers))
print(results)
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))
print(results)

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75
over_75 = list(filter(is_A_student, scores))
print(over_75)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))
print(palindromes)


# Python 3
from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers)
print(result)

# Python 3
from functools import reduce
numbers = [3, 4, 6, 9, 34, 12]
def custom_sum(first, second):
    return first + second
result = reduce(custom_sum, numbers, 10)
print(result)
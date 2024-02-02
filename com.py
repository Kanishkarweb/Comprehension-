# List Comprehension 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cube = [number ** 3 for number in numbers]

print(cube)

# Dictionary Comprehension

dict_numbers = {number: number ** 3 for number in numbers}

print(dict_numbers)
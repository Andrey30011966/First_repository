first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_strings if len(i) > 5]
second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
new_string= set(first_strings + second_strings)
new_result = {i: len(i) for i in new_string if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(new_result)
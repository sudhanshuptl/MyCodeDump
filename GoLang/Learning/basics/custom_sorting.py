# Define the list of tuples
ls = [
    ('abc', 5, 'sfdsf'),
    ('abc', 3, 'sfdsdf'),
    ('abdc', 15, 'xsfdsf'),
    ('aqbc', 65, 'bsfdsf'),
    ('ap[bc', 52, 'sfdsdf'),
    ('acbc', 50, 'sfdsf')
]

# Sort the list based on the value at index 1 of each tuple
sorted_ls = sorted(ls, key=lambda x: x[1])

# Print the sorted list
print(sorted_ls)

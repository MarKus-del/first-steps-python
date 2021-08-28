first_value = '  FIRST challenge         '
second_value = '-  second challenge  -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge
print(first_value.strip().title().rjust(20))

# Second challenge
print(second_value.replace('-', ' ').strip().title())

# Third challenge
print(
    third_value
        .strip()
        .replace(' ', '')
        .replace('-', '')
        .lower()
        .capitalize()
        .rjust(30)
)

# print(first_value)
# print(second_value)
# print(third_value)

# Fourth challenge - use only the print() function (no f-strings)
print('{}#{}#{}!'.format(fourth_value, fifth_value, sixth_value))


# Fifth challenge - use only a single print() function.  Create tabs and new lines using f-strings.

print(f'\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')
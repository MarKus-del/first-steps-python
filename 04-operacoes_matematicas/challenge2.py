print('Simple calculator!')

first_number = input('First number?')
if first_number.isnumeric() == False:
    print('Please input a number.')
    exit()

operation = input('Operation?')

second_number = input('Second number?')
if second_number.isnumeric() == False:
    print('Please input a number.')
    exit()

if operation == '+':
    sum = int(first_number) + int(second_number)
    print(f'sum of {first_number} + {second_number} equals {sum}')
elif operation == '-':
    diferrence = int(first_number) - int(second_number)
    print(f'diferrence of {first_number} - {second_number} equals {diferrence}')
elif operation == '*':
    multi = int(first_number) * int(second_number)
    print(f'multi of {first_number} * {second_number} equals {multi}')
elif operation == '/':
    dif = int(first_number) / int(second_number)
    print(f'dif of {first_number} / {second_number} equals {dif}')
elif operation == '**':
    expo = int(first_number) ** int(second_number)
    print(f'expo of {first_number} ** {second_number} equals {expo}')
elif operation == '%':
    modul = int(first_number) % int(second_number)
    print(f'modul of {first_number} % {second_number} equals {modul}')
else:
    print('Operation not recognized.')
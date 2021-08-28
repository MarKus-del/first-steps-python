confirm = input('Would you like to continue?')

if confirm == 'yes' or confirm == 'y':
	print('Continuing ...')
	print('Complete!')
elif confirm == 'no' or confirm == 'n':
	print('Existing')
else:
	print('Please try again and respond with yes or no.')

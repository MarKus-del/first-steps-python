print("Today' data?")
date = input()

print('Breakfast calories?')
breakfastCal = int(input())

print('Lunch calories?')
lunchCal = int(input())

print('Dinner calories?')
dinnerCal = int(input())

print('Snack calories?')
snackCal = int(input())

caloriesTotal = breakfastCal + lunchCal + dinnerCal + snackCal
print('Calorie content for ' + date + ': ' + str(caloriesTotal))
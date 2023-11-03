# for num in range(10, 20, 2):
#   print(num, end='\n')

# for i in [0, 1, 2, 3, 4]:
#   print(num, end='\n')

# print("Range: Double Arguments")
# for i in range(2, 10):
#   print(i, end=',')

# print("Range: Triple Arguments")
# for i in range(2, 10, 2):
#   print(i, end=',')

# for number in range(1, 11):
#   square = number ** 2
#   print(number, '\t', square)


# for number in range(13, 3, -1):
#   cube = number ** 3
#   print(number, '\t', cube)


# accumulator = 0
# MAX = 5
# total = 0

# print('This program calculates the sum of')
# print(MAX, 'numbers you will enter')

# for counter in range(MAX):
#   number = int(input('Enter a number: '))
#   total = total + number
#   print('The total is: ', total)


# lot_no = int(input('Input Lot number: '))

# while lot_no != 0:
#   property_value = float(input('Input property value: '))

#   property_tax = property_value * 0.0065
#   print(f"The tax is: {property_tax}")

#   lot_no = int(input('Do you want to continue? (Input Lot Number if yes, or 0 if no): '))


temperature = float(input('Input current temperature: '))
print('Wait for 15 minutes')

while temperature > 102.5:
  print('Turn down the temperature and wait 5 minutes')
  temperature = float(input('Input the new temperature: '))
keep_going = 'y'

while keep_going == 'y':
  sales_amount = float(input('Input amount of sales: '))
  comm_rate = float(input('Enter commission rate: '))

  commission = sales_amount * comm_rate
  print(f"The commission is: {commission}")
  
  keep_going = input('Do you want to calculate another commission (y/n): ').lower
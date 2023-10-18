converting = True

while converting:
  mode = input('input (i) for inches mode, (f) for feet mode, (c) to close: ')
  height = 0
  h_in_cm = 0
  prompting = False

  if mode == 'i':
    height = float(input('Input height in inches: '))
    h_in_cm = height * 2.54
    print('The height in cm is:', h_in_cm)
    prompting = True
  elif mode == 'f':
    height = float(input('Input height in feet: '))
    h_in_cm = height * 2.54 * 12
    print('The height in cm is:', h_in_cm)
    prompting = True
  elif mode == 'c':
    break
  else:
    print('Invalid Input!')

  # if prompting == True:
  #   prompt = input('Do you want to stop converting? (y/n): ')

  #   if prompt == 'y':
  #     break
  #   elif prompt == 'n':
  #     prompting = False
  #   else:
  #     print('Invalid Input')
  #     prompting = True  
  #   prompting = False
  #   break

  break
score = int(input('Enter your score: '))

if score <= 100 and score >= 0:
  if score >= 70:
    print('You scored A')
  elif score >= 60:
    print('You scored B')
  elif score >= 50:
    print('You scored C')
  elif score >= 45:
    print('You scored D')
  else:
    print('You scored F')
else:
  print('Invalid Input')
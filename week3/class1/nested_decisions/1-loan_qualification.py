# example

salary = int(input('Input Salary: '))
years_on_job = None


if salary >= 30000:
  years_on_job = int(input('How long have you been working here: '))
  if years_on_job >= 2:
    print('You have qualified for the loan')
  else:
    print('You need to have been on the Job for at least 2 years to qualify')
else:
  print('You need to be earning at least 30000 to qualify')
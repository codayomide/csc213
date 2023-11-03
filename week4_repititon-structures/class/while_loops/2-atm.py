balance = 1000000

while balance > 0:
  withdrawal = float(input('Enter amount to withdraw: '))

  if withdrawal > balance:
    print("Insufficient funds! ")
    print(f"Your balance is {balance}")

  else:  
    balance = balance - withdrawal
    print(f"Your new balance is {balance}")
print("Sorry! Sorry, don't cry! 😂")
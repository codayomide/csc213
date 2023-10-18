def calculate(num1, num2):
  add = num1 + num2
  subtract = num1 - num2
  multiply = num1 * num2
  divide = num1 / num2

  print(f'The sum is: {add}')
  print(f'The difference is: {subtract}')
  print(f'The product is: {multiply}')
  print(f'The division is: {divide}')

def circle(radius):
  pi = 3.142

  circumference = 2 * pi * radius
  area = pi * (radius ** 2)

  print(f"The Circumference is: {circumference}")
  print(f"The Area is: {area}")

def convert_to_celsius(fahrenheit):
  celsius = (5 / 9) * (fahrenheit - 32)
  print(f"Celsius: {celsius}")

def compound_interest(principal, rate, time):
  new_amount = principal * ((1 + (rate / 100)) ** time)
  compound_interest = new_amount - principal

  print(f"The New Amount is: ${new_amount}")
  print(f"The Compound Interest is: ${compound_interest}")
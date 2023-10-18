principal = float(input("Input Account Balance: $"))
annual_rate = float(input("Annual Rate in percentage: "))
time = float(input("Time in years: "))

new_amount = principal * ((1 + (annual_rate / 100)) ** time)
compound_interest = new_amount - principal

print(f"The New Amount is: ${new_amount}")
print(f"The Compound Interest is: ${compound_interest}")

#celcius = (5 / 9) * (C - 32)
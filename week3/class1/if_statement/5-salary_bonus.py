# class exercise after figure 3.3

salary = float(input("Enter salary value: "))
bonus = 0
total_salary = salary + bonus

if salary > 50000:
  bonus = bonus + 500

total_salary = salary + bonus

print(f'Your total salary is: {total_salary}')
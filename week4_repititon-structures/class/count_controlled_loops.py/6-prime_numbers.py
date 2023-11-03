for i in range(0, 100):
  count = 0
  
  for j in range(1, int(i/2) + 1):
    if (i % j) == 0:
      count += 1
  if count == 1:
    print(i)
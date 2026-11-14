def fractional_knapsack():
  n = int(input("Enter number of items: "))

  items = []

  for i in range(n):
    w = float(input("enter weight:"))
    v = float(input("enter value:"))

    items.append((v / w , w, v))

  cap = float(input("enter capacity: "))
  total = 0;

  items.sort(reverse=True)

  for ratio, weight, value in items:
    if cap >= weight:
      total += value
      cap -= weight
    else:
      total += ratio * cap
      break

  print("maximum value : ", round(total, 2))

fractional_knapsack()
    

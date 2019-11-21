def product(n):
  total = 1
  for i in n:
    total *= i
  return total

numbers = (5,5,5)
print(product(numbers))

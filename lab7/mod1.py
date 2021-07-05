import math

def newton(n,k):
  if(n >= k):
    return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
  else:
    return 0

def pascal(n):
  for i in range(n):
    for j in range(n-i):
      print(end = " ")
    for j in range(i+1):
      print(newton(i,j), end=" ")
    print()


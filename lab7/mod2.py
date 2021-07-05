
def e_symbol(n, k):
  if (k==0):
    return 1
  elif (k==n):
    return 0
  return (k+1)*e_symbol(n-1, k) + (n-k)*e_symbol(n-1, k-1)

def euler(n):
  for i in range(n):
    for j in range(i+1):
      print(e_symbol(i,j), end=" ")
    print()
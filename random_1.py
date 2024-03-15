def prime(user):
  
  max_prime = -1
  while n%2 == 0:
    max_prime = 2
    n = n//2

  for i in range(3, int(n**0.5)+1,2):
    while i%2==0:
      max_prime = i
      n = n//i
      
  if n > 2:
    max_prime = n
  return max_prime

prime(3)

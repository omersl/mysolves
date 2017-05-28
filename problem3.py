number = 600851475143
  
prime = 2
while number > 1:
  if number % prime == 0:
    number /= prime
    print(prime)

  else:
    prime += 1


def is_prime(n):
  """Returns True if n is a prime number, False otherwise."""
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

def print_first_n_prime_numbers(n):
  """Prints the first n prime numbers."""
  count = 0
  number = 2
  while count < n:
    if is_prime(number):
      print(number)
      count += 1
    number += 1

if __name__ == '__main__':
  print_first_n_prime_numbers(10)

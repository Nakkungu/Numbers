import random

def select_random_numbers(start, stop, count=1):
  
  random_numbers = []
  for i in range(count):
    random_number = random.randint(start, stop)
    random_numbers.append(random_number)
  return random_numbers
# Select a random number between 0 and 10 (inclusive).
random_number = select_random_numbers(0, 11)

# Print the random numbers.
print(random_number)
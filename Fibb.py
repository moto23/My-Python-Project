first_term = 0
second_term = 1

n = int(input('nth term of fibonnaci series'))

for i in range(2,n):
  nth_term = first_term + second_term
  first_term = second_term	
  second_term = nth_term

  print(second_term, end=', ')
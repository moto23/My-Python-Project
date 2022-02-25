min_age = 0
max_age = 100

running = True

for i in range(1,10):
  while running:

    mid=int((min_age + max_age)/2)
    ans=input(f"are you {mid} years old?").lower()

    if ans=='correct':
      print("its correct guess")
      running = False
      break
      

    elif ans=='more':
      min_age=mid
      print("guess age is more than answer")

    elif ans=='less':
      max_age=mid
      print("guess age is less than answer")

    else:
      print("its wrong choice,please make correction")
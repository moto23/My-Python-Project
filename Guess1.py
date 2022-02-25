Last = 0
First= 100
for i in range(1,10):
    guessed_age = int((Last + First) / 2)
    answer = input('Tell Whether You Are ' + str(guessed_age) + " years old?")
    if answer == 'correct':
        print("You Correctly Guessed")
        break
    elif answer == 'less':
        First = guessed_age
    elif answer == 'more':
        Last = guessed_age
    else:
        print('You have guessed wrong')
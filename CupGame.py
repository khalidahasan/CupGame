from random import shuffle

i = int(input("Enter a number here (1-3): "))

a = [' ', 'O', ' ']
shuffle(a)

if 0 < i < 4:
    if a[i - 1] == 'O':
        print('You win')
        print(a)
    else:
        print('You lose')
        print(a)
else:
    print('You entered a wrong number.')
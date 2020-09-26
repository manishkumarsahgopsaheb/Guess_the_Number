
def start_game():
    import random
    # num1 and num2 are two random number which give
    # you a range between which you have to guess the actual number
    num1 = random.randint(20, 25)
    num2 = random.randint(35, 40)

    # num is the random generated number which you have to guess

    num = random.randint(25, 35)
    print(num)
    # This count will also defined your score
    count = int(input('how many life you want to give me?\n'))
    guessing_num = int(input("your Game start Now!\n"
                             "guess the number between %d to %d:\n" % (num1, num2)))
    search_key(guessing_num, count, num)


def search_key(guessing_num, count, num):
    while count:
        if guessing_num > num:
            count = count - 1
            if count > 0:
                print('your number is too high \t\t(only %d life left)' % count)
                guessing_num = int(input('guess again:\n'))
            else:
                break

        elif guessing_num < num:
            count = count - 1
            if count > 0:
                print('your number is too low \t\t (only %d life left)' % count)
                guessing_num = int(input('guess again:\n'))
            else:
                break

        elif guessing_num == num:
            print('guess correct!\n'
                  'your score is %d' % count)
            again_in = input('if you want to play again then type a letter y and hit enter\n')

            if again_in == 'y':
                start_game()
            else:
                break
    if count == 0:
        print('No more life left\n'
              'your score is %d' % count)
        again_in = input('if you want to play again then type a letter y and hit enter\n')
        if again_in == 'y':
            start_game()
        else:
            print('you have entered wrong key\n'
                  'have a nice day!')


start_game()

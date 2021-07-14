import random

player_name = input("What's your name?\n")
print(player_name, ', I am thinking of a number between 1 and 100.', sep='')
print('Try to guess my number.')
comp_num = random.randint(1, 100)
count = 1

# def game():
#     guess = int(input('Your guess?\n'))
#     global count
#     if guess > comp_num:
#         print('Your guess to too high. Try again.')
#         count += 1
#         game()
#     elif guess < comp_num:
#         print('Your guess to too low. Try again.')
#         count += 1
#         game()
#     else:
#         print("That's right! You found my number in", count, 'tries')


# game()

guess = int(input('Your guess?\n'))

while guess != comp_num:
    if guess > comp_num:
        print('Your guess to too high. Try again.')
        count += 1
        guess = int(input('Your guess?\n'))

    elif guess < comp_num:
        print('Your guess to too low. Try again.')
        count += 1
        guess = int(input('Your guess?\n'))
else:
    print("That's right! You found my number in", count, 'tries')

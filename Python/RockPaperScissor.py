import random

weapons = ['Rock', 'Paper', 'Scissor']

while True:
    user_choice = input('Choose from: Rock - Paper - Scissor : ').strip().title()
    bot_choice = random.choice(weapons)

    print('Your choice = ',user_choice, ', Computer choice = ',bot_choice)

    if user_choice == bot_choice:
        print('Both choose same \n Its Draw Boi 🤝')

    elif user_choice == 'Paper':
        if bot_choice == 'Rock':
            print('You win \n will beat you next time😏')
        else:
            print('You lose✂️ \n😂')

    elif user_choice == 'Scissor':
        if bot_choice == 'Rock':
            print('You lose🪨\n😂')
        else:
            print('You win \n will beat you next time😏')

    elif user_choice == 'Rock':
        if bot_choice == 'Paper':
            print('You lose🧻\n😂')
        else:
            print('You win \n will beat you next time😏')

    else:
        print('Chose wisely bot will get angry 👁️👁️')

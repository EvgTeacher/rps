import random

def game():
    result = {'computer': 0, 'user': 0}
    while result['computer'] < 3 and result['user'] < 3:
        print('Start game rock, paper, scissor')
        comp_choice = random.choice('rsp')
        choice = input('RSP')
        print('Your select - ', choice.lower())
        print('Computer select - ', comp_choice)
        if choice.lower() == comp_choice:
            print('Draw')
            print('Score, Computer', result['computer'], '-', result['user'])
        elif choice.lower() == 'r' and comp_choice == 'p':
            result['computer'] += 1
            print('Score, Computer', result['computer'], '-', result['user'])
        elif choice.lower() == 'r' and comp_choice == 's':
            result['user'] += 1
            print('Score, Computer', result['computer'], '-', result['user'])
        elif choice.lower() == 'p' and comp_choice == 's':
            result['computer'] += 1
            print('Score, Computer', result['computer'], '-', result['user'])
        elif choice.lower() == 'p' and comp_choice == 'r':
            result['user'] += 1
            print('Score, Computer', result['computer'], '-', result['user'])
        elif choice.lower() == 's' and comp_choice == 'r':
            result['computer'] += 1
            print('Score, Computer', result['computer'], '-', result['user'])
        elif choice.lower() == 's' and comp_choice == 'p':
            result['user'] += 1
            print('Score, Computer', result['computer'], '-', result['user'])
    user = input('y/n')
    if user == 'y':
        game()



game()
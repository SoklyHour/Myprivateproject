import random

Game_play = True
player_score= 0
cpu_score= 0 
while Game_play == True:
    rock= f'''
        _______
    ---'  _____)
        (_______)
        (_______)
        (______)
    ---.__(____)     

    '''
    paper= f'''
        _______
    ---'   ____)____
            ________)
            _________)
            ________)
    ---.___________)

    ''' 
    scissors= f'''
        _______
    ---'   ____)_____
            __________)
            ___________)
        (______)
    ---.__(____)
    '''

    player_choice= int(input('Please enter 1 for rock 2 for paper and 3 for scissors: '))
    cpu_choice = random.randint(1,3)
    
    if player_choice == cpu_choice:
        if (player_choice==1 and cpu_choice==1):
         print(rock)
         print(rock)
         print("It is a tie. No score for both!")

        elif(player_choice==2 and cpu_choice==2):
         print(paper)
         print(paper)
         print("It is a tie. No score for both!")

        elif(player_choice==3 and cpu_choice==3):
         print(scissors)
         print(scissors)
         print("It is a tie. No score for both!")

    elif player_choice == 1:
        if cpu_choice == 2:
            print('cpu chose paper and won this round')
            print(rock)
            print(paper)
            cpu_score +=1
            print('cpu score: ' + str(cpu_score) + '\n' + 'Your score: ' + str(player_score))

        if cpu_choice == 3:
            print('cpu chose scissors. You won this round')
            print(rock)
            print(scissors)
            player_score +=1
            print('cpu score: ' + str(cpu_score) + '\n' + 'Your score: ' + str(player_score))

    elif player_choice == 2:
        if cpu_choice == 1:
            print('cpu chose rock. You won this round')
            print(paper)
            print(rock)
            player_score +=1
            print('cpu score: ' + str(cpu_score) + '\n' + 'Your score: ' + str(player_score))

        if cpu_choice == 3:
            print('cpu chose scissors and won this round')
            print(paper)
            print(scissors)
            cpu_score +=1
            print('cpu score: ' + str(cpu_score) + '\n' + 'Your score: ' + str(player_score))

    else:
        if cpu_choice == 1:
            print('cpu chose rock and won this round')
            print(scissors)
            print(rock)
            cpu_score +=1
            print('cpu score: ' + str(cpu_score) + '\n' + 'Your score: ' + str(player_score))

        if cpu_choice == 2:
            print('cpu chose paper. You won this round')
            print(scissors)
            print(paper)
            player_score +=1
            print('cpu score: ' + str(cpu_score) + '\n' + 'Your score: ' + str(player_score))

    if player_score == 3:
        print('You won the game!(= 3 scores)')
        player_score= 0
        cpu_score= 0
        decision= input('Do you want to play one more round? (Y/N)')
        if decision =='N':
            Game_play=False
            print('Thank you for playing this Rock Paper Scissors Game!')
            break

    if cpu_score == 3:
        print('cpu won the game, but you lost the game!(= 3 scores)')
        player_score= 0
        cpu_score= 0 
        decision= input('Do you want to play one more round? (Y/N)')
        if decision =='N':
            Game_play=False
            print("Thank you for playing this Rock Paper Scissors Game!")
            break
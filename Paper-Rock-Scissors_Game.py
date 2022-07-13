import random

computer_choice = random.choice(['rock','paper','scissors'])
player_choice = input('rock/paper/scissors? ')
print(computer_choice)
if player_choice == computer_choice:
    print('draw')
elif player_choice == 'scissors':
    if computer_choice == 'rock':
        print('you lose')
    elif computer_choice == 'paper':
        print ('you win')    
elif player_choice == 'rock':
    if computer_choice == 'paper':
        print('you lose')
    elif computer_choice == 'scissors':
        print ('you win')      
elif player_choice == 'paper':
    if computer_choice == 'scissors':
        print('you lose')
    elif computer_choice == 'rock':
        print ('you win')  
else:
    print('error input')        



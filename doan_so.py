import random
print ("welcome to number guessing game\nif your guesses is lower than 5 you'll win")
number = random.randint(1,100)
chosen_number = input('choose a number 1-100 ')
number_of_guesses=1
while int(chosen_number) < 101:
    if int(chosen_number) < number:
            print("your number is smaller than it, do you want to play again?")
            a=input('yes or no ')
            if a=='no':
                print('thank for playing')
                print("number of guesses = "+str(number_of_guesses)+' and of course you lose')
                quit()
            else:
                chosen_number = input('choose a number 1-100 ')
                number_of_guesses= int(number_of_guesses) + 1
            
    if int(chosen_number) > number:
            print("your number is bigger than it, do you want to play again?")
            b=input('yes or no ')
            if b=='no':
                print('thank for playing')
                print("number of guesses = "+str(number_of_guesses)+' and of course you lose')
                quit()
            else:
                chosen_number=input('choose a number 1-100 ') 
                number_of_guesses= int(number_of_guesses) + 1 

             
    if int(chosen_number) == number:
        if number_of_guesses<6:
            print("congratulation, it's correct, and")
            print("your number of guesses = "+str(number_of_guesses)+' you WIN')
        elif number_of_guesses>5:
            print("congratulation, it's correct, but...")
            print("your number of guesses = "+str(number_of_guesses)+' and you lose')
        break
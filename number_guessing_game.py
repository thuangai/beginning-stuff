import random
print ("welcome to number guessing game")
number = random.randint(1,100)
chosen_number = input('choose a number 1-100')
number_of_guesses=1
while int(chosen_number) < 101:
      if int(chosen_number) < number:
            print("your number is smaller than it, choose again")
            chosen_number=input('choose a number 1-100')
            number_of_guesses= int(number_of_guesses) + 1
     
      if int(chosen_number) > number:
            print("your number is bigger than it, choose again")
            chosen_number=input('choose a number 1-100') 
            number_of_guesses= int(number_of_guesses) + 1  
     
      if int(chosen_number) == number:
            print("congratulation, it's correct")
            print("number of guesses = "+str(number_of_guesses))
            break
            

# importing random
from random import *

# taking input from user
user_pass = input("Enter your password: ")

# storing alphabet letter to use thm to crack password
password = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v', 
            'w', 'x', 'y', 'z','1','2','3','4','5','6','7','9','0','@','<','>',';',':','-','.','~',' ','#','&','%','/','[',']','¥','?','!','*','{','}','^','+','=','_','$','A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V', 
            'W', 'X', 'Y', 'Z' ]

# initializing an empty string
guess = ""


# using while loop to generate many passwords untill one of
# them does not matches user_pass

cpt=0
while (guess != user_pass):
    cpt+=1
    guess = ""
    # generating random passwords using for loop
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 86)]
        guess = str(guess_letter) + str(guess)
    # printing guessed passwords
    print('  ',guess,end=" ")
    y =open('admis.txt','a')
    y.write(guess)

    
# printing the matched password
print()
print(" Your password is ",guess)
print(' nbr de repetetion: ',cpt)

y =open('admis.txt','a')
y.write(' ~ https://github.com/deepXculture')
y.close()
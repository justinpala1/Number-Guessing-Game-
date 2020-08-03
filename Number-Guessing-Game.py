#GUESS THAT NUMBER

print("WELCOME TO GUESS THAT NUMBER!")
print("The objective of the game is to guess the correct number in the least amount of guesses.")

#Saves to soloscore.txt
fo = open("soloscore.txt", "r")
file = fo.read()
if len((file)) > 0:
    print((file))
else:
    fo.close()

#Saves to score.txt
fo = open("score.txt", "r")
file = fo.read()
if len((file)) > 0:
    print((file))
else:
    fo.close()

import random
guess_count=0
first_try=True 
#Single PLayer Game Mode
def one_player():
    first_try= True
    player_count=0
    guess_count=0
    a="Yes"
    while a=="Yes":
 
            if first_try==True:
                name=input("Before we begin, what's your name? ")
                first_try=False
                print("Alright %s, there will be 3 rounds to guess the correct number and teh aim of the game is to try and guess the game in the least amount of guesses. Let's start playing!Im thinking of a number between 1 and 100" % (name))
     
            number=random.randint(1,100)
            while True:
                
                player_guess=int(input("Guess the correct number: "))
                guess_count=guess_count+1
                print("So far, you have taken %s guesses" % (guess_count))
                if player_guess == number:
                    print("Congrats, you guessed the correct number!")
                    player_count = player_count+1
                    break
                elif player_guess < number:
                    print("You guessed lower than the correct number")
                elif player_guess > number:
                    print("You guessed higher than the correct number")

            print ("%s: %d" % (name, player_count))

            if player_count==1:
                print("YOU WIN!")
                player_count=0
                file = open("soloscore.txt", "w")
                file.write("Recent Solo Player Winner: %s, %d guesses" %(name, guess_count))
                file.close()
                print ("The information was saved to %s" % file.name)
                break

            y=str.lower(input("Would you like to play again(yes or no)"))
     
            if y=="no":
                print("Thanks for playing")
                break
            elif y=="yes":
                pass

#Multiplayer Game Mode     
def two_player():
    guess_count=0
    p1_count=0
    p2_count=0
    a="yes"
    p1_name=str(input("Alright Player 1, What's your name? "))
    p2_name=str(input("Next, What's your name Player 2? "))
 
    print("Now %s and %s! The aim of the game is to guess the correct number before the other player and win the round. The first player to win 3 rounds is the winner and will have their stats recorded. Now, let's start the game! I'm thinking of a number between 1 and 100." % (p1_name, p2_name))
    while a=="yes":
        number = random.randint(1,100)
        while True:
 
            p1_guess = int(input("%s guess the correct number: " % p1_name))
            p2_guess = int(input("%s guess the correct number: " % p2_name))
            guess_count = guess_count+1
            print ("So far, you have taken %d guesses" % guess_count)
            if p1_guess == number:
                print("Congrats %s, you guessed the correct number!" % p1_name)
                p1_count = p1_count+1
                break
            elif p1_guess < number:
                print("%s, you guessed lower than the correct number" % p1_name)
            elif p1_guess > number:
                print("%s, you guessed higher than the correct number" % p1_name)

            if p2_guess == number:
                print("Congrats %s, you guessed the correct number!" % p2_name)
                p2_count = p2_count+1
                break
            elif p2_guess < number:
                print("%s, you guessed lower than the correct number" % p2_name)
            elif p2_guess > number:
                print("%s, you guessed higher than the correct number" % p2_name)
 
        print ("%s: %d" % (p1_name, p1_count))
        print ("%s: %d" % (p2_name, p2_count))
                
        if p1_count==1:
                print("GAME OVER! %s WINS!!" % p1_name)
                p1_count=0
                p2_count=0
                file = open("score.txt", "w")
                file.write("Recent Two Player Winner: %s, %d guesses" %(p1_name, guess_count))
                file.close()
                print ("The information was saved to %s" % file.name)
                

        elif p2_count==1:
                print ("GAME OVER! %s WINS!!" % p2_name)
                p1_count=0
                p2_count=0
                file_name=open("score.txt", "w")
                file_name.write("Recent Two Player Winner: %s, %d guesses" %(p2_name, guess_count))
                file_name.close()
                print ("The information was saved to %s" % file.name)
                
     
        z=str.lower(input("Would you like to continue playing(yes or no)"))
     
        if z=="no":
            print("Thanks for playing")
            break
        elif z=="yes":
            pass
 

z = input("Do you want to play one player or two player?(1 for one player or 2 for two players): ")
if z == "1":
        one_player()
elif z == "2":
        two_player()


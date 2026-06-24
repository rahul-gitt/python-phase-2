'''The game() function in a program lets a user play a game and returns the score as an integer. 
You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score.
You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.'''
import random
def game():
    print("You are playing the game...")
    score = random.randint(1,100)

    with open("file_handling/game/hiscore.txt") as f:
        hiscore = f.read()
        if hiscore == "":
            hiscore = 0
        else:
            hiscore = int(hiscore)
        
    print(f"Your score is : {score}")
    if score> hiscore:
        with open("file_handling/game/hiscore.txt","w") as f:
            f.write(str(score))
    
    return score

game()
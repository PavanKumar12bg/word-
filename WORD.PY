# word guessing game
import random

def charcter_guess():
    print("WELLCOME TO WORD GUESSING GAME")

    word_list=["python","java","c","india","america"]
    word=random.choice(word_list)

    # print(words)
    guesses=""
    chances=len(word)+2

    # using while loop to excute game till chances

    while chances > 0 :
        display_word=""
         # using for loop ittirate every word
        for char in word:
            if char in guesses:
                display_word+=char+""
            else:
                display_word+="_ "
        
        print("\n" + display_word)

        if "_" not in display_word:
            print ("you are win")
            break

        user=input("Guess the character =").strip().lower()

        guesses+=user
        
        if user not in word :
            chances-=1
            print("Wrong Guess ❌")
            print(f"You have {chances} more guesses left")

            if chances == 0:
                print (f"YO are lose the game\nthe word is{word}")
                break
            


def play_game():
    while True:
        charcter_guess()

        player=input("enter your option if you want to play game again (yes.no) =").strip().lower()
        if player in ["yes"]:

            continue
        elif player == "no":
            print ("thank's for playing game good bye")
            break
        else:
            print("sorry not understand your option please enter valid option")

play_game()


                  
          
         

  


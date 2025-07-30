import random
def game():
    enemy=random.choice(['dharshini','haadhiya','sathurya_lakshmi','abhinaya','madhumitha'])
    print("you have 6 attempts to guess pooja's enemy")
    print("if you know pooja very well ,guess her main enemy")
    attempts=0
    max_attempts=6

    while attempts< max_attempts:
        guess = input(f"Attempt {attempts + 1}: ")
        attempts +=1

        if guess==enemy:
            print("you guessed correctly,you know her surroundings well")
            break
        else:
            print("sorry you don't know her very well")
    print(f"pooja's main enemy is:{enemy}")
    
    play_again=input("are you interested in guessing pooja's enemy again? (interested/notinterested): ")
    return play_again == "interested"

while game():
    pass
print("go and know about her,then come play again")
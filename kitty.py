import time
import random
import threading
import os

gamePause = threading.Event()

def start():
    print(r"""
                    ‿‿‿‿‿‿‿‿‿‿‿,     ⠀⢀⣀⡀⠀ ⡀⡀⠀⠀⠀⠀
        ⎮╲ ╲ ╲ ╲ ╲ ╲╲ ╲        ⠀⠀⠀⠀  ⡠⠇⠈⢙⠉⠐⠅⠀⡦⢄⠀⠀
        ⎮   ⎮︼︼︼︼︼︼︼︼︼  ⠀⠀ ⠀⢰⠁⠀⠑⠐⠀⠀⠀⠀ ⠀⠾⢄⠀
        ⎮   ⎮                 ⠀ ⠀⠊⠀⠀⠀⠀⠀⠄⢄⠀⠀⠀⠀⢀⡜⠁
        ⎮   ⎮                  ⢀⡜⠀⠀⠀ ⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⡸⠀
        ⎮   ⎮                   ⠸⠀⠀⠀⠀⠀⠀⢀⠴⢠⡌⣀⠐⠀⠈⠘⠁⡄
‿‿..,⎮‿⎮‿‿‿‿‿‿‿‿‿‿‿⎮.,      ⠀    ⢸⠃⠀⠀⢠⣾⣃⠀⠁⠀⢙⣶⣀⠀⠀⠘⡧
⎮╲╲╲╲╲╲╲╲╲╲╲╲╲╲             ⠀⠀⠀⠀⠀ ⠘⠛⠀⠀⠀⢸⡾⠏⠀⠯⠀⠏⠀
⎮   ⎮︼︼︼︼︼︼︼︼︼︼︼︼︼  ⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣸⠀⢸⠃⠀⠀⠀⠀⠀⠀
⎮   ⎮ᨳ   ____              ⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⡀⠀⠀⠨⠀⠀⠀⠀⠀⠀⠀
⎮   ⎮     ⎮░░⎮    ⠀⠀⠀          ⠀ ⠀⠀⢠⡔⠂⠀⡀⠀⣀⠑⠤⢀⡀⠀⠀⠀
⎮   ⎮     ⎮░░⎮    ⠀ ⠀⠀⠀       ⠀⠀⠀ ⠀⠀⠀⠀⠀⠁⠁⠀⠀⠈⠀⠀⠀⠀  
 
    """)
    time.sleep(1)
    print("CLI Kitty, get yours here!")
    time.sleep(1)
    consent = input(f"You there... do you want a CLI Kitty? Y/N: ").strip().lower()

    if consent == "y":
        return True
    else:
        print("Alright, maybe next time!")
        return False

def img():
    options = {
        "1": r"""
         ٠࣪⭑    ╱|、      
        ≽(`  -  7
         |ᝰ 〵   ╭
         じしˍ,) ノ
        """,
        "2": r"""
                        ＿＿.     
        　　　      ୨୧ ＞　　フ 
        　　　　　| 　_　 _ l. 
        　 　　　／` ミ_ xノ   
        　　 　 /　　　 　 |.                        
        　　　 /　 ヽ　　 ﾉ.      
        　 　 │　　|　|　|.     
        　／￣|　　 |　|　|
        　| (￣ヽ＿ヽ)__)
        　＼二つ
        """,
        "3": r"""
        ₍^. .^₎⟆
        """,
        "4": r"""
        /\_/\
    = ( • . • ) =
       /     \
        """
    }

    while True:
        print(f"Alright, which one are ya eyeing?")
        for key, art in options.items():
            print(f"Option {key}:\n{art}")

        choice = input("1, 2, 3, or 4?: ").strip()
        if choice in options:
            return options[choice]
        else:
            print("Invalid choice, try again.")
            continue


def name():
    while True:
        time.sleep(1)
        tname =  input("Name your CLI Kitty: ")
        time.sleep(0.5)
        consent = input(f"You want your Kitty to be named " + tname + " right? Y/N: ").strip().lower()

        if consent == "y":
            return tname
        else:
            print("Okay, let's try again.")

def gameLoop(kitty):
    while True:
        gamePause.wait()
        time.sleep(random.randint(10, 25))
        randDec = random.randint(0, 2)

        if randDec == 0:
            kitty["hunger"] -= 1
            print(f"{kitty['name']} is getting hungry!")
            time.sleep(1)
            print(f"Hunger: {kitty['hunger']}")
        elif randDec == 1:
            kitty["happiness"] -= 1
            print(f"{kitty['name']} looks sad...")
            time.sleep(1)
            print(f"Happiness: {kitty['happiness']}")
        elif randDec == 2:
            kitty["health"] -= 1
            print(f"{kitty['name']} is feeling sick!")
            time.sleep(1)
            print(f"Health: {kitty['health']}")

        kitty["hunger"] = max(0, kitty["hunger"])
        kitty["happiness"] = max(0, kitty["happiness"])
        kitty["health"] = max(0, kitty["health"])

        if 0 in [kitty["hunger"], kitty["happiness"], kitty["health"]]:
            print(f"{kitty['name']} has passed away... Game Over.")
            time.sleep(2)
            exit()

def command(kitty):
    while True:
        command = input(f"Enter command (status, feed, play, heal, exit): ").strip().lower()

        if command == "status":
            time.sleep(1)
            print(f"Updated Stats:")
            time.sleep(1)
            print(f"{kitty['img']} \nHunger: {kitty['hunger']}, \nHappiness:  {kitty['happiness']}, \nHealth:  {kitty['health']}")
        elif command == "feed":
            gamePause.clear()
            time.sleep(1)
            if kitty["hunger"] < 5:
                feed(kitty)
                kitty["hunger"] += 1
                print(kitty["img"])
                time.sleep(1)
                print(f"Hunger: {kitty['hunger']}")
            else:
                time.sleep(1)
                print(kitty["img"])
                print(f"{kitty['name']} is full and refuses to eat!")
                time.sleep(1)
                print(f"Hunger: {kitty['hunger']}")
            gamePause.set()
        elif command == "play":
            gamePause.clear()
            time.sleep(1)
            play(kitty)
            gamePause.set()
        elif command == "heal":
            gamePause.clear()
            time.sleep(1)
            if kitty["health"] < 5:
                kitty["health"] += 1
                print(f"You took care of {kitty['name']}!")
                print(kitty["img"])
                print(f"Health: {kitty['health']}")
            else:
                print(kitty["img"])
                print(f"{kitty['name']} is healthy!")
                print(f"Health: {kitty['health']}")
            gamePause.set()
        elif command == "exit":
            time.sleep(1)
            print("Exiting...")
            exit()
        else:
            time.sleep(1)
            print("Invalid command, try again.")
            continue

def feed(kitty):
    while True:
        print(f"Select something for {kitty['name']} to eat!")
        time.sleep(1)
        print("(I don't own a cat, I don't know if these foods are safe for cats, please don't feed your cats any of this without proper research and think of CLI Kitty as an alien cat perhaps)")
        choice = input(r"""
        Option 1: Strawberry
        Option 2: Fish
        Option 3: A literal star
        Option 4: Secret fourth option
        1, 2, 3, or 4:
        """).strip()

        if choice == "1":
            time.sleep(1)
            print(f"{kitty['name']} nibbles on the strawberry. Cute!")
        elif choice == "2":
            time.sleep(1)
            print(f"{kitty['name']} happily devours the fish!")
        elif choice == "3":
            time.sleep(1)
            print(f"{kitty['name']} somehow devours the star... They're glowing a little.")
        elif choice == "4":
            time.sleep(1)
            print(f"{kitty['name']} finds a secret snack and purrs mysteriously.")
        else:
            time.sleep(1)
            print("Invalid option, try again.")
            continue

        return

def play(kitty):
    while True:
        choice = input(r"""Choose your minigame!
            Option 1: Rock paper scissors
            Option 2: Hangman
            (more coming later!)
            (or type exit to quit minigame selector)
            1, 2, or exit: 
        """).strip().lower()

        if choice == "1":
            wlt = rpt()
            if wlt == "win" and kitty["happiness"] < 5:
                kitty["happiness"] += 1
                print(f"You played with {kitty['name']}!")
                time.sleep(1)
                print(kitty["img"])
                time.sleep(1)
                print(f"Happiness: {kitty['happiness']}")
            elif wlt == "win" and kitty["happiness"] >= 5:
                print(kitty["img"])
                time.sleep(1)
                print(f"{kitty['name']} is already sooo happy!")
                time.sleep(1)
                print(f"Happiness: {kitty['happiness']}")
            return
        elif choice == "2":
            wlt = hm()
            if wlt == "win" and kitty["happiness"] < 5:
                kitty["happiness"] += 1
                print(f"You played with {kitty['name']}!")
                time.sleep(1)
                print(kitty["img"])
                time.sleep(1)
                print(f"Happiness: {kitty['happiness']}")
            elif wlt == "win" and kitty["happiness"] >= 5:
                print(kitty["img"])
                time.sleep(1)
                print(f"{kitty['name']} is already sooo happy!")
                time.sleep(1)
                print(f"Happiness: {kitty['happiness']}")
            return
        elif choice == "exit":
            time.sleep(1)
            print("Exiting minigame selector...")
            return

def rpt():
    time.sleep(1)
    print("IT'S TIME TO ROCK PAPER SCISSORS TO THE DEATH!- I mean... for funsies!! Yeah...")
    time.sleep(1)
    print(f"If ya win, your CLI Kitty, {kitty['name']} gets a play point! Assuming it's not already 5.")
    time.sleep(1)
    print("Ready...")
    time.sleep(1)
    print("Set...")
    time.sleep(1)
    print("GO!")

    choices = ["rock", "paper", "scissors"]
    computer = random.randint(0, 2)
    player = input("Enter rock, paper, or scissors: ").strip().lower()

    if player not in choices:
        time.sleep(1)
        print("Invalid choice.")
        return
    
    time.sleep(1)
    print(f"Computer chose: {choices[computer]}")
    time.sleep(1)

    if player == choices[computer]:
        time.sleep(1)
        print("It's a tie!")
        return "tie"
    elif (player == "rock" and choices[computer] == "scissors") or \
    (player == "paper" and choices[computer] == "rock") or \
    (player == "scissors" and choices[computer] == "paper"):
        time.sleep(1)
        print("You win!")
        return "win"
    else:
        time.sleep(1)
        print("You lose...")
        return "loss"
    time.sleep(1)

def hm():
    time.sleep(1)
    print(f"MUAHAHAHA I'M GONNA BEAT YOU AT THIS GAME AND STEAL {kitty['name']}-... Friendly match, totally")

    words = ["meow", "Minecraft", "shark", "starry"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    attempts = 6
    wrong_guesses = []

    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            time.sleep(1)
            print("Bruh. One letter at a time.");
            continue
        
        if guess in wrong_guesses or guess in guessed:
            time.sleep(1)
            print("You already guessed that.")
            continue
        
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            time.sleep(1)
            print("Nice one!")
        else:
            attempts -= 1
            wrong_guesses.append(guess)
            time.sleep(1)
            print(f"WRONG! {attempts} attempts left.")

        print(" ".join(guessed))
        print(f"Wrong guess: {', '.join(wrong_guesses)}")

    if "_" not in guessed:
        time.sleep(1)
        print(f"You win! For now... >:(")
        return "win"
    else:
        time.sleep(1)
        print(f"YOU LOSE MUAHAHAHA... Well, you're a good carer, you can keep your CLI Kitty for now.")
        return "loss"

def main():
    if start():
        kimg = img()
        kname = name()
        kitty = {
            "img": kimg,
            "name": kname,
            "hunger": 4,
            "happiness": 5,
            "health": 5
        }
        time.sleep(1)
        print("Meet your CLI Kitty, " + kname + "!")
        time.sleep(1)
        print(f"{kitty['img']} \nHunger: {kitty['hunger']}, \nHappiness:  {kitty['happiness']}, \nHealth:  {kitty['health']}")

        "Remember to check in on Kitty! She gets hungry, sad, and sick fast! (Every 10-25 seconds)"

        gameThread = threading.Thread(target = gameLoop, args=(kitty,), daemon=True)
        gameThread.start()

        command(kitty)

if __name__ == "__main__":
    main()

# random todo list
# - add timesleep everywhere
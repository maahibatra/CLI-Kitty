import time
import random
import threading
import os

def start():
#     print(r"""
#                     ‿‿‿‿‿‿‿‿‿‿‿,     ⠀⢀⣀⡀⠀ ⡀⡀⠀⠀⠀⠀
#         ⎮╲ ╲ ╲ ╲ ╲ ╲╲ ╲        ⠀⠀⠀⠀  ⡠⠇⠈⢙⠉⠐⠅⠀⡦⢄⠀⠀
#         ⎮   ⎮︼︼︼︼︼︼︼︼︼  ⠀⠀ ⠀⢰⠁⠀⠑⠐⠀⠀⠀⠀ ⠀⠾⢄⠀
#         ⎮   ⎮                 ⠀ ⠀⠊⠀⠀⠀⠀⠀⠄⢄⠀⠀⠀⠀⢀⡜⠁
#         ⎮   ⎮                  ⢀⡜⠀⠀⠀ ⠀⠀⠀⠀⣸⠀⠀⠀⠀⠀⡸⠀
#         ⎮   ⎮                   ⠸⠀⠀⠀⠀⠀⠀⢀⠴⢠⡌⣀⠐⠀⠈⠘⠁⡄
# ‿‿..,⎮‿⎮‿‿‿‿‿‿‿‿‿‿‿⎮.,      ⠀    ⢸⠃⠀⠀⢠⣾⣃⠀⠁⠀⢙⣶⣀⠀⠀⠘⡧
# ⎮╲╲╲╲╲╲╲╲╲╲╲╲╲╲             ⠀⠀⠀⠀⠀ ⠘⠛⠀⠀⠀⢸⡾⠏⠀⠯⠀⠏⠀
# ⎮   ⎮︼︼︼︼︼︼︼︼︼︼︼︼︼  ⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⣸⠀⢸⠃⠀⠀⠀⠀⠀⠀
# ⎮   ⎮ᨳ   ____              ⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⡀⠀⠀⠨⠀⠀⠀⠀⠀⠀⠀
# ⎮   ⎮     ⎮░░⎮    ⠀⠀⠀          ⠀ ⠀⠀⢠⡔⠂⠀⡀⠀⣀⠑⠤⢀⡀⠀⠀⠀
# ⎮   ⎮     ⎮░░⎮    ⠀ ⠀⠀⠀       ⠀⠀⠀ ⠀⠀⠀⠀⠀⠁⠁⠀⠀⠈⠀⠀⠀⠀  
 
#     """)
#     print("CLI Kitty, get yours here!")
    # consent = input(f"You there... do you want a CLI Kitty? Y/N: ").strip().lower()

    # if consent == "y":
    #     return True
    # else:
    #     print("Alright, maybe next time!")
    #     return False

    return True

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
        # print(f"Alright, which one are ya eyeing?")
        # for key, art in options.items():
        #     print(f"Option {key}:\n{art}")

        choice = input("1, 2, 3, or 4?: ").strip()
        if choice in options:
            return options[choice]
        else:
            print("Invalid choice, try again.")

        # return options["2"]


def name():
    while True:
        # tname =  input("Name your CLI Kitty: ")
        # consent = input(f"You want your Kitty to be named " + tname + " right? Y/N: ").strip().lower()

        # if consent == "y":
        #     return tname
        # else:
        #     print("Okay, let's try again.")

        return "kitty"

def gameLoop(kitty):
    while True:
        time.sleep(random.randint(0, 5))
        randDec = random.randint(0, 2)

        # if randDec == 0:
        #     kitty["hunger"] -= 1
        #     print(f"{kitty['name']} is getting hungry!")
        #     print(f"Hunger: {kitty['hunger']}")
        # elif randDec == 1:
        #     kitty["happiness"] -= 1
        #     print(f"{kitty['name']} looks sad...")
        #     print(f"Happiness: {kitty['happiness']}")
        # elif randDec == 2:
        #     kitty["health"] -= 1
        #     print(f"{kitty['name']} is feeling sick!")
        #     print(f"Health: {kitty['health']}")

        # kitty["hunger"] = max(0, kitty["hunger"])
        # kitty["happiness"] = max(0, kitty["happiness"])
        # kitty["health"] = max(0, kitty["health"])

        # if 0 in [kitty["hunger"], kitty["happiness"], kitty["health"]]:
        #     print(f"{kitty['name']} has passed away... Game Over.")
        #     exit()

def command(kitty):
    while True:
        # command = input(f"Enter command (status, feed, play, heal, exit): ").strip().lower()

        command = "play"

        if command == "status":
            print(f"Updated Stats:")
            print(f"{kitty['img']} \nHunger: {kitty['hunger']}, \nHappiness:  {kitty['happiness']}, \nHealth:  {kitty['health']}")
        elif command == "feed":
            if kitty["hunger"] < 5:
                kitty["hunger"] += 1
                print(f"You fed {kitty['name']}!")
                print(kitty["img"])
                print(f"Hunger: {kitty['hunger']}")
            else:
                print(kitty["img"])
                print(f"{kitty['name']} is full!")
                print(f"Hunger: {kitty['hunger']}")
        elif command == "play":
            play(kitty)
            # if kitty["happiness"] < 5:
            #     kitty["happiness"] += 1
            #     print(f"You played with {kitty['name']}!")
            #     print(kitty["img"])
            #     print(f"Happiness: {kitty['happiness']}")
            # else:
            #     print(kitty["img"])
            #     print(f"{kitty['name']} is sooo happy!")
            #     print(f"Happiness: {kitty['happiness']}")
        elif command == "heal":
            if kitty["health"] < 5:
                kitty["health"] += 1
                print(f"You took care of {kitty['name']}!")
                print(kitty["img"])
                print(f"Health: {kitty['health']}")
            else:
                print(kitty["img"])
                print(f"{kitty['name']} is healthy!")
                print(f"Health: {kitty['health']}")
        elif command == "exit":
            print("Exiting...")
            exit()
        else:
            print("Invalid command, try again.")

def play(kitty):
    while True:
        choice = input(r"""Choose your minigame!
            Option 1: Shooting stars
            (more coming later!)
        """)

        if choice == "1":
            ss(kitty)

def ss(kitty):
    star = "STAR"
    width = 100
    height = 20
    position = random.randint(0, width - len(star) - 1)
    kimgLines = kitty["img"].split("\n")
    kimgHeight = len(kimgLines)

    for y in range(1, height - 1):
        os.system("cls" if os.name == "nt" else "clear")
    
        print("+" + "-" * (width - 2) + "+")

        for i in range(1, height - 1):
            if i == y:
                print("|" + " " * position + star + " " * (width - position - len(star) - 2) + "|")
            else:
                print("|" + " " * (width - 2) + "|")

        for line in kimgLines:
            padding = (width - len(line)) // 2
            print(" " * padding + line + " " * (width - len(line) - padding - 2) + "|")

        print("+" + "-" * (width - 2) + "+")

        time.sleep(0.2)

def main():
    if start():
        kimg = img()
        kname = name()
        kitty = {
            "img": kimg,
            "name": kname,
            "hunger": 5,
            "happiness": 5,
            "health": 5
        }
        print("Meet your CLI Kitty, " + kname + "!")
        print(f"{kitty['img']} \nHunger: {kitty['hunger']}, \nHappiness:  {kitty['happiness']}, \nHealth:  {kitty['health']}")

        gameThread = threading.Thread(target = gameLoop, args=(kitty,), daemon=True)
        gameThread.start()

        command(kitty)

if __name__ == "__main__":
    main()
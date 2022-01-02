def welcome(name):
    str = f"Hello {name} and welcome to the World of Games.\n Here you can find many cool games to play!"
    return str

def load_game():
    str = f"Please choose a game to play:\n" \
              "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n" \
              "2. Guess Game - guess a number and see if you chose like the computer\n" \
              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    num_game = int(input(str))
    if num_game not in range(1, 4):
        print("wrong number, please enter a number between 1-3")
        return
        #try_again = raw_input("Try again!!!")

    str = "Please choose game difficulty from 1 to 5:\n"
    level_game = int(input(str))
    if level_game not in range(1, 6):
        print("wrong number, please enter a number between 1-5")
        return





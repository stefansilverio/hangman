# attribute is an action that an object can perform - "The cat can jump".
# attributes of an object refer to the given data and abilities of that object
# an object is just a collection of associated attributes

import random


def hangman(word):
    word_list = ["butter", "bubble", "smoke", "shield"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong = 0
    stages = ["",
             "_________     ",
             "|             ",
             "|       |     ",
             "|       0     ",
             "|      /|\    ",
             "|      / \    ",
             "|             ",
              ]
    remaining_letters = list(word)
    board = ["____"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "guess a letter"
        char = input(msg)
        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board))
        e=wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("you win!")
            print(" ".join(board))
            win=True
            break
     if not win:
         print("\n".join(stages[0: wrong]))
         print("you lose! It was {}.".format(word)

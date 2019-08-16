def hangman(word):
    wrong = 1
    stages = ["",
             "_________"  ,
             "|          ",
             "|        |",
             "|        O",
             "|       /|\",
             "|       / \",
             "|          "
             ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("welcome to the hangman")
    while wrong < len(stages) -1:
        

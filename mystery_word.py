import random
# asks level and calls its level method from Level class
def game_start():
    name = input("What is your name? ")
    print ("Hello, " + name, "Choose Game level: 1, 2, 3")
    level = input(":")
    if level == "1":
        x = easy_level() #why isn't x called 1
        return x
    if level == "2":
        x= normal_level()
        return x
    if level == "3":
        x = hard_level()
        return x
    else:
        return "Wrong Input"
def play_game():
    print ("Word Guessing Game") #difference between play game versus game start
    word = game_start() # calls function on line  4 to start get the word length and level
    word_length = len(word)
    #empty variable to store guesses
    guesses = ''
    #number of guesses
    allowed_guesses = 8
    while allowed_guesses > 0:   # we have total 8 guesses until reaches 0
        wrong = 0  #when we have 0 guess and we did find the word game is over
    #checks if char in guesses
        for char in word:
            if char in guesses:   # it compares guess character  and word char
                print (char)
            else:
                print ("_")   # if wrong char prints _ underscore
                wrong += 1
        if wrong == 0:  # when  there is 0 wrong you won
            print ("You won" )
            break
        #user char input word length
        print("Word length is", word_length) # this will show up to let the user the length of the word user has to find
        guess = input("guess a character:")
        #store input value
        guesses += guess.upper()  # to capitalize
        #checks if char not in guesses
        if guess not in word:  #checks if guesses char in word to calculate how many guesses lef
            allowed_guesses -= 1        # if wrong it will subtract number of guesses
        print ("Wrong")
        print ("You have", + allowed_guesses, 'more guesses') # shows hom many guesses left
        if allowed_guesses == 0:           #if you used all guesses you lost
                print("Word is", word)
                print( "You Lose")
# get data from file and read
def open_file():
    with open('words.txt', 'r') as file:
        data = file.read().lower() # make sure all lowercase
        words = [word for word in data.split()] # this will create a long list of words from file
        return words
# if level 1 call this method (list of easy words)
def easy_level():
    easy = [] # we will store all easy words
    words = open_file() #calls function on line 78 to read all words
    for word in words:
        if len(word) >= 4 and len(word) < 6: # sorts easy ones
            easy.append(word) #stores in easy list
            value = random.choice(easy)
            return value.upper() # at the and again apper case
# if level 2 call this method (list of normal words)
def normal_level():
    normal = []
    words = open_file()
    for word in words:
        if len(word) > 6 and len(word) < 8:
            normal.append(word)
            value = random.choice(normal)
            return value.upper()
# if level 3 call this method  (list of hard words)
def hard_level():
    hard = []
    words = open_file()
    for word in words:
        if len(word) > 8:
            hard.append(word)
            value = random.choice(hard)
            return value.upper()
play_game()# this runs function on line on 23

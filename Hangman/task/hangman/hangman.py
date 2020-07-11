# Write your code here
import random
print("H A N G M A N")
play = True
while play:
    menuChoice = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if menuChoice == "play":
        wordList = ['python', 'java', 'kotlin', 'javascript']
        secretWord = random.choice(wordList)
        solution = "-"*(len(secretWord))
        lifes = 8
        guessed = []
        while lifes > 0:
            print(f"\n{solution}")
            if solution.find("-") == -1:
                print("You guessed the word!")
                break
            else:
                usrGuess = input("Input a letter: ")
                if len(usrGuess) != 1:
                    print("You should input a single letter")
                    continue
                if not usrGuess.islower():
                    print("It is not an ASCII lowercase letter")
                    continue
                index = secretWord.find(usrGuess)
                if index == -1:
                    if usrGuess in guessed:
                        print("You already typed this letter")
                        continue
                    else:
                        print("No such letter in the word")
                        guessed.append(usrGuess)
                        lifes -= 1
                else:
                    if solution.find(usrGuess) != -1:
                        print("You already typed this letter")
                    else:
                        temp = secretWord
                        while temp.count(usrGuess) > 0:
                            solution = solution[:index] + usrGuess + solution[index+1:]
                            temp = temp[:index] + "-" + temp[index+1:]
                            index = temp.find(usrGuess)
        if solution.find("-") == -1:
            print("You survived!")
        else:
            print("You are hanged!")
    else:
        if menuChoice == "exit":
            exit()
        else:
            continue

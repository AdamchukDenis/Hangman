## Hangman v2.0

from View import printMenu, printDifficulty, printHighScore

def getWord(difficulty):

    maxLen = 4
    minLen = 0

    if difficulty == 2:
        maxLen = 7
        minLen = 5
    elif difficulty == 3:
        maxLen = 100
        minLen = 8

    diffWordList =[]

    with open(r"Wordpy.txt", encoding="utf8") as file_with_words:
        wordsAll = file_with_words.readlines()
        for word in wordsAll:
            if minLen <= len(word) - 1 <= maxLen:
                diffWordList.append(word)
                
    from random import choice
    word = choice(diffWordList)
    word = word[:len(word)-1]
    return 'someWord'

def main():
    import Model as Md
    userChoice = printMenu()
    if userChoice == 1:
        difficulty = printDifficulty()
        Md.wordStr = getWord(difficulty)
        Md.wordList = list(Md.wordStr)
        Md.wordBlurStr = len(Md.wordStr) * '*'
        Md.wordBlurList = list(Md.wordBlurStr)
    elif userChoice == 2:
        printHighScore()
    else:
        return

main()
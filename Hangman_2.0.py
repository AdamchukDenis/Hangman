## Hangman v2.0

from View import *

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

    with open(r"C:\Users\Acer\Desktop\Python\Hangman\Wordpy.txt", encoding="utf8") as file_with_words:
        wordsAll = file_with_words.readlines()
        for word in wordsAll:
            if minLen <= len(word) - 1 <= maxLen:
                diffWordList.append(word)
                
    from random import choice
    word = choice(diffWordList)
    word = word[:len(word)-1]
    return word

def game():
    import Model as Md
    outputfails = {0:' ', 1: firstFail,2: secondFail,3: thirdFail}
    if ('*'not in Md.wordBlurList): 
        print(f'''Ви виграли
Слово було {Md.wordStr}''')
        # score(points)
        
    elif(Md.fails == 3):
        print(outputfails[Md.fails])
        # score(points)
        
    print(f'''

                                               
# Ваше слово {Md.wordBlurStr}                    
# Угадуйте літеру                                
                                                  
# {" ".join(outputfails[Md.fails])}                        
# ''')


def main():
    import Model as Md
    userChoice = printMenu()
    if userChoice == 1:
        difficulty = printDifficulty()
        Md.wordStr = getWord(difficulty)
        Md.wordList = list(Md.wordStr)
        Md.wordBlurStr = len(Md.wordStr) * '*'
        Md.wordBlurList = list(Md.wordBlurStr)
        game()
    elif userChoice == 2:
        printHighScore()
    else:
        return
    

main()
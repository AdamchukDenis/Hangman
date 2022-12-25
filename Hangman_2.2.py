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
        return
        
    elif(Md.fails == 3):
        print(outputfails[Md.fails])
        return
        
    print(f'''
Ваше слово {Md.wordBlurStr}                    
Угадуйте літеру                                
                                                  
{outputfails[Md.fails]}''')
    print(' '.join(Md.alphabet[0:11]))
    print(' '.join(Md.alphabet[11:22]))
    print(' '.join(Md.alphabet[22:33]))

    answer = input()
# Перевірка літери у слові
    if(answer.upper() in Md.alphabet):
        index = Md.alphabet.index(answer.upper())
        Md.alphabet[index] = "-"
        if(answer.lower() in Md.wordList):
            print(f"Літера {answer} є в цьому слові.")
            for idx1 in range(len(Md.wordList)):
                if(answer.lower() == Md.wordBlurList[idx1]):
                    # Заміна * на літеру
                    Md.wordBlurList[idx1] = answer.lower()
            game()
        else:
            print("Нажаль такої літери там немає")
            Md.fails += 1 
            return
        
    else: 
        print('Ви вже вводили цю літеру або вона не з Української мови.')
        game()




def main():
    import Model as Md
    userChoice = printMenu()
    if userChoice == 1:
        difficulty = printDifficulty()
        Md.wordStr = getWord(difficulty)
        Md.wordList = list(Md.wordStr)
        Md.wordBlurStr = len(Md.wordStr) * '*'
        Md.wordBlurList = list(Md.wordBlurStr)
        score = game()
        
    elif userChoice == 2:
        printHighScore()
    else:
        return
    

main()
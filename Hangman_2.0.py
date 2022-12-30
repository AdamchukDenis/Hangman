## Hangman v2.0

from View import *
import Model as Md

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
    outputfails = {0:' ', 1: firstFail,2: secondFail,3: thirdFail}
    if ('*'not in Md.wordBlurList): 
        print(f'''Ви виграли
Слово було {Md.wordStr}''')
        return
        
    elif(Md.fails == 3):
        print(outputfails[Md.fails])
        print(f'Слово було "{Md.wordStr}"')
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
                if(answer.lower() == Md.wordList[idx1]):
                    # Заміна * на літеру
                    Md.wordBlurList[idx1] = answer.lower()
                    Md.wordBlurStr = ' '.join(Md.wordBlurList)
            game()
        else:
            print("Нажаль такої літери там немає")
            Md.fails += 1 
            game()
        
    else: 
        print('Ви вже вводили цю літеру або вона не з Української мови.')
        game()

def score():
    old_points = 0
    points = 0
    if Md.fails == 0:
        points += 100
    elif Md.fails == 1:
        points += 50
    elif Md.fails == 2:
        points += 25
    else:
        points -= 50
    with open('C:\\Users\\Acer\\Desktop\\Python\\Hangman\\Scorepy.txt', 'r') as score_change:
        for i in score_change.readlines():
            all_points = i[22]+i[23]+i[24]+i[25]
            try:
                old_points += int(all_points)
            except:
                pass
    score_change.close()

    with open('Scorepy.txt', 'w') as score_change:
        score_change.write(f'''
+----------------------------------------+
              Score Point                
           1. Word    {points + old_points}           
+----------------------------------------+''')
        score_change.close()

def restart():
    print(View_restart)

def main():
    userChoice = printMenu()
    if userChoice == 1:
        difficulty = printDifficulty()
        Md.wordStr = getWord(difficulty)
        Md.wordList = list(Md.wordStr)
        Md.wordBlurStr = len(Md.wordStr) * '*'
        Md.wordBlurList = list(Md.wordBlurStr)
        game()
        score()
        res_choice = restart()
        if res_choice == 1: main()
        else: return
        
    elif userChoice == 2:
        printHighScore()
    else:
        return
    

if __self__ == '__self__':
    main()
﻿# view

def printMenu():
        choice = int(input(''' 
+-----------------------------------+
|           Гра Шибеник             |
|                                   |
|       Виберіть дію                |
|       1.Старт                     |
|       2.Статистика                |
|       3.Вихід                     |
+-----------------------------------+
'''))
        return choice

def printDifficulty():
    diffLevel = int(input('''
+-----------------------------------+
|    Виберіть Рівень Складності:    |
|    1.Легкий                       |
|    2.Середній                     |
|    3.Складний                     |
+-----------------------------------+
'''))
    return diffLevel

def printHighScore():
    print('high score')
    return
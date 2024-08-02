"""ДНК, Эл Свейгарт al@inventwithpython.com. Простое динамическое
изображение двойной спирали ДНК. Нажмите Ctrl+F2 для останова.
 Вдохновлено созданным matoken сценарием https://ascilinema.org/a/155441"""

import random, sys, time

PAUSE = 0.15 # (!) Можно заменить значение на 0.5, 0.0

# Отдельные строки динамического изображения DNA:
ROWS = [
    #123456789 <- Для наглядной оценки количества пробелов:
    '           ##',   # у индекса 0 нет нуклеотидов {}.
    '        #{}-{}#',
    '       #{}---{}#',
    '     #{}-----{}#',
    '    #{}------{}#',
    '   #{}------{}#',
    '   #{}-----{}#',
    '    #{}---{}#',
    '    #{}-{}#',
    '     ##', # у индекса 9 нет нуклеотидов {}.
    '    #{}-{}#',
    '    #{}---{}#',
    '   #{}-----{}#',
    '   #{}------{}#',
    '    #{}------{}#',
    '     #{}---{}#',
    '      #{}-{}#']
    #123456789 <- Для наглядной оценки количества пробелов:

try:
    print('DNA Animation, by Al Sweigart al2inventwithpython.com')
    print('Press Ctrl+F2 to quit...')
    time.sleep(2)
    rowIndex = 0

    while True: # Основной цикл программы.
        # Увеличиваю rowIndex на 1 для отрисовки следующей строки:
        rowIndex = rowIndex + 1 # можно заменить на rowIndex + 2
        if rowIndex == len(ROWS):
            rowIndex = 0

        # У строк с индексами 0 и 9 нет нуклеотидов:
        if rowIndex == 0 or rowIndex == 9:
            print(ROWS[rowIndex])
            continue

        # Выбираем случайные пары оснований гуанин-цитозин и аденин-тимин:
        randomSelection = random.randint(1, 4) # можно заменить на random.randint(1, 2)
        if randomSelection == 1:
            leftNucleotide, rightNucleotide = 'A', 'T'
        elif randomSelection == 2:
            leftNucleotide, rightNucleotide = 'T', 'A'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'C', 'G'
        elif randomSelection == 3:
            leftNucleotide, rightNucleotide = 'G', 'C'

        # Выводим строку на экран.
        print(ROWS[rowIndex].format(leftNucleotide, rightNucleotide))
        time.sleep(PAUSE) # Вставляем небольшую паузу.
except KeyboardInterrupt:
    sys.exit() # Если нажато сочетание клавиш Ctrl+F2 - завершаем программу.
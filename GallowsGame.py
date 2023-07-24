import random

# список слов для выбора
words = ['книга', 'доска', 'карма', 'пенал']

# выбираем уровень сложности игры
def complexity():
    global tries
    while True:
        #print()
        x = input('Выберите сложность игры (от нее зависит количество попыток):'
                  '\n 1 - Легкий\n 2 - Средний\n 3 - Сложный\n')
        if x == '1':
            tries = 7
            break
        if x == '2':
            tries = 6
            break
        if x == '3':
            tries = 5
            break
        else:
            print('Неверный ввод')
            continue

# проверяем, что пользователь вводит именно букву и переводим ее в нижий регистр
def valid_letter():
    while True:
        s = input('Введите букву: ')
        if s.isalpha() == True:
            return s.lower()
        else:
            print('Неверный ввод! Можно ввести только букву.')
            continue

# тело игры
def game():
    # выбираем случайное слово
    word = random.choice(words)
    # создаем пустой массив для хранения угаданных букв
    guessed_letters = []
    global tries
    print('Добро пожаловать в игру "Виселица"!\nВ данной игре все загаданные слова имеют 5 букв.')
    complexity()  # уровень сложности
    while tries > 0:
        # выводим текущее состояние слова
        for letter in word:
            if letter in guessed_letters:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

        # запрашиваем у пользователя букву
        letter = valid_letter()

        # проверяем, не вводил ли пользователь эту букву ранее
        if letter in guessed_letters:
            print('Выберите другую букву, такая уже была!')
            continue

        # добавляем букву в список угаданных
        if letter in word:
            guessed_letters.append(letter)
            print(guessed_letters)

        # проверяем, есть ли такая буква в слове
        if letter not in word:
            tries -= 1
            print('Неверная буква! Осталось попыток:', tries)

        # проверяем, все ли буквы отгаданы
        if set(word) == set(guessed_letters):
            print(f'Поздравляем, вы отгадали слово!\nПравилный ответ: {word}')
            break
    else:
        print('Вы проиграли! Загаданное слово:', word)

# повтор игры
def repeat():
    while True:
        print('Хотите повторить игру?\n1 - Повторить\n2 - Выйти')
        repeat = input()
        if repeat == '1':
            game()
        if repeat == '2':
            print('Спасибо за игру! До скорых встреч!')
            break
        else:
            print('Неверный вводддд')
            continue

game() # первый запуск игры
repeat() # запуск повтора игры
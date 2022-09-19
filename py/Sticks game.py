# Древняя китайская игра в палочки.
# Играют два игрока.  Есть 10 палочек. Игроки по очереди берут от одной до трёх палочек. Играют до тех пор пока не закончатся палочки.
# Тот кто взял последним - тот проиграл.
# Реализуйте игру таким образом, чтобы могли играть два человека. Изначально есть 10 палочек.
# На каждом ходу выводите на консоль текущее количество оставшихся палочек и просите ввести количество палочек,
# которое хочет взять игрок (который делает ход). Не забывайте менять очерёдность игроков и сокращать кол-во палочек.
# В конце надо вывести кто победил - первый или второй игрок.

number_of_sticks = 10
player_tern = 1

def can_take(sticks):    # Функция, которая определяет, сколько можно взять палочек пользователем
    return sticks <= 3 and sticks >= 1

def switch_player_tern(turn):   # Функция, которая переключает очередь
    return 1 if player_tern == 2 else 2

def end_game(sticks):   # Функция, которая принимает количество палочек и оканчивает игру
    return sticks <= 0

while (not end_game(number_of_sticks)): # Запускаем цикл - пока не конец игры
    print(f'How many sticks you take? Remaining {number_of_sticks}')
    taken = int(input())

    if not can_take(taken): # Выводим текст, сколько палочек нужно взять
        print('You took the wrong number of sticks. Take 1 or 2 or 3 sticks')
        continue

    number_of_sticks -= taken# Отнимаем от общего количества палочек то количество, сколько было взято
    print(f' Sticks taken: {taken}\n')

    if end_game(number_of_sticks):  # Если конец игры
        print(f'Player {player_tern} is lost')  # Выводит проигравшего игрока, который берет палочки
        print(f'Player {1 if player_tern ==2 else 2} is WIN')   # Выводит номер победителя, если другой игрок проиграл

    player_tern = switch_player_tern(player_tern) # Переключаем функцию


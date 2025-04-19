import random as rn
player1 = 10
player2 = 10
count = 0

while True:
    print(f"Ход первого игрока! (Всего {player1} шариков)")
    mind_player1 = int(input("Введите число шариков в вашей руке: \n"))
    hand_player1 = mind_player1 % 2

    mind_player2 = rn.randint(1, player2)
    hand_player2 = mind_player2 % 2

    if hand_player1 == hand_player2:
        print(f"Игрок 2 отгадал! ({mind_player2}). Он получает {mind_player1} шариков")
        player2 = player2 + mind_player1
        player1 = player1 - mind_player1
    else:
        print(f"Игрок 2 не отгадал :( ({mind_player2}). Он отдаёт {mind_player1} шариков")
        player2 = player2 - mind_player1
        player1 = player1 + mind_player1

    count = count + 1
    if player1 <= 0:
        print("Игрок 2 победил! (^.^)")
        print(f"Общее число ходов: {count}")
        break
    elif player2 <= 0:
        print("Игрок 1 победил! [^_^]")
        print(f"Общее число ходов: {count}")
        break 
        
    print(f"Ход второго игрока. (Всего {player2} шариков)")
    mind_player2 = rn.randint(1, player2)
    hand_player2 = mind_player2 % 2

    mind_player1 = int(input("Игрок 2 взял в руку шарики. Чётное или нечетное?... (0, 1): \n"))
    
    if mind_player1 == hand_player2:
        print(f"Игрок 1 отгадал! (Игрок 2 задумал {mind_player2} шариков) Он получает {mind_player2} шариков")
        player2 = player2 - mind_player2
        player1 = player1 + mind_player2
    else:
        print(f"Игрок 1 не отгадал :( (Игрок 2 задумал {mind_player2} шариков). Он отдаёт {mind_player2} шариков")
        player1 = player1 - mind_player2
        player2 = player2 + mind_player2
        
    count = count + 1
    if player1 <= 0:
        print("Игрок 2 победил! (^.^)")
        print(f"Общее число ходов: {count}")
        break
    elif player2 <= 0:
        print("Игрок 1 победил! [^_^]")
        print(f"Общее число ходов: {count}")
        break 
    
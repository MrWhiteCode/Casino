import random
import time

#Ставки
def get_bet(balance):
    while True:
        print(f"Ваш баланс: ${balance}")
        bet_input = input("Ведите ставку (или 0 для выхода в меню)")
        if bet_input == '0':
            return 0
        if not bet_input.isdigit():
            print("Введите число!")
            continue
        bet = int(bet_input)
        if bet > balance:
            print("Не хватает фишек!")
            continue
        if bet <= 0:
            print("Ставка должна быть больше 0!")
            continue
        return bet
        
#Игровые автоматы
def play_slots(balance):
    print("Добро пожаловать на Игровые Автоматы!")
    time.sleep(1)
    print("Комбинация 3 одинаковых чисел - x10 | 2 одинаковых - x2")
    
    while True:
        bet = get_bet(balance) 
        if bet == 0: 
            break

        balance -= bet
        print("Барабаны куртятся...")
        time.sleep(2)

        symbols = ["🍒", "🍋", "💎", "🍀", "7️⃣"]
        reel1 = random.choice(symbols)
        reel2 = random.choice(symbols)
        reel3 = random.choice(symbols)

        print(f"| {reel1} | {reel2} | {reel3} |")

        if reel1 == reel2 == reel3:
            win = bet * 10
            balance += win
            print(f"ДЖЕКПОТ! Ты выиграл: ${win}")
        elif reel1 == reel2 or reel2 == reel3 or reel1 == reel3:
            win = bet * 2
            balance += win
            print(f"Неплохо, ты выиграл: ${win}")
        else:
            print("Упс, ты проиграл. Попробуй еще раз")
        
        if balance <= 0: break
        print(f"Твой баланс: ${balance}")
    return balance

def play_roulette(balance):
    red = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37]
    black = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
    green = [0]

    print("Добро пожаловать на Рулетку!")
    time.sleep(1)
    print("Если выпадает правильный цвет - x5")
    time.sleep(1)

    while True:
        bet = get_bet(balance)
        if bet == 0:
            break
        
        balance -= bet
        player_choice = input("Ваш цвет(зеленый, красный или черный, писать через -ое): ")
        print("Шарик катается...")
        time.sleep(2)

        winning_number = random.randint(0, 36)
        if winning_number == 0:
            winning_color = "зеленое"
        elif winning_number in red:
            winning_color = "красное"
        else:
            winning_color = "черное" 
        print(f"Выпало число: {winning_number} ({winning_color})")

        if player_choice == winning_color:
            win = bet * 5
            balance += win
            print(f"Ты победил! Ты выиграл ${win}!")
        else:
            print("Ты проиграл! Попробуй еще раз.")
        
        if balance <= 0: break
        print(f"Твой баланс: {balance}")
    return balance

def play_fortuna(balance):
    numbers = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 5, 5, 10, 10, 50]
    
    print("Добро пожаловать на Колесо Фортуны!")
    time.sleep(1)
    print("Если тебе выпало 0 - ты проиграл! | 1 - Ты забрал свою ставку обратно | 2, 5 или 10 - ставка x10! | 50 - 100.000!")
    time.sleep(1)

    while True:
        bet = get_bet(balance)
        if bet == 0:
            break

        balance -= bet
        print("Колесо крутится...")
        your_number = random.choice(numbers)
        time.sleep(2)

        print(f"Тебе выпало {your_number}!")

        if your_number == 1:
            win = bet
            balance += win
            print("Ты забираешь свою ставку назад")
        elif your_number == 2 or your_number == 5 or your_number == 10:
            win = bet * 10
            balance += win
            print(f"Ты умножил свою ставку на 10! Ты выиграл {win}")
        elif your_number == 50:
            win = 100_000
            balance += win
            print("ТЫ ВЫИГРАЛ 100.000! ТЫ РАЗОРИЛ КАЗИНО!")
        else:
            print("Сорян, ты проиграл!")
        if balance <= 0: break
        print(f"Ваш баланс: {balance}")
    return balance

#Хаб казино
def main():
    player_balance = 1000
    print("Добро пожаловать в казино Las-Vegas Text Casino! Желаем вам приятной игры!")
    time.sleep(1)

    while player_balance > 0:
        print("Выберите куда пойдете! \n1:Игровые Автоматы \n2:Рулетки \n3:Колесо Фортуны \n4:Уйти из казино")
        game = input("")
        if game == '1':
            player_balance = play_slots(player_balance)
        elif game == '2':
            player_balance = play_roulette(player_balance)
        elif game == '3':
            player_balance = play_fortuna(player_balance)

    if player_balance <= 0:
        print("Вы банкрот! Охранники выкидывают вас на улицу.")


main() #type: ignore
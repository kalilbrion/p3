import random

def welcome_message():
    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадаю число, а ты попробуешь его угадать.")
    print("Ты можешь выбрать уровень сложности и получать подсказки.")

def choose_difficulty():
    print("Выбери уровень сложности:")
    print("1 - Легкий (1-100, 10 попыток)")
    print("2 - Средний (1-500, 7 попыток)")
    print("3 - Сложный (1-1000, 5 попыток)")
    
    while True:
        choice = input("Введите номер уровня (1, 2 или 3): ")
        if choice == '1':
            return 10, 1, 100
        elif choice == '2':
            return 7, 1, 500
        elif choice == '3':
            return 5, 1, 1000
        else:
            print("Некорректный ввод. Пожалуйста, выбери 1, 2 или 3.")

def get_user_guess():
    while True:
        try:
            guess = int(input("Введите ваше число: "))
            return guess
        except ValueError:
            print("Это не число! Пожалуйста, попробуйте снова.")

def give_hint(guess, number_to_guess):
    if abs(guess - number_to_guess) <= 10:
        print("Тепло!")
    else:
        print("Холодно!")

def play_game():
    attempts, min_number, max_number = choose_difficulty()
    number_to_guess = random.randint(min_number, max_number)
    print(f"\nЯ загадал число от {min_number} до {max_number}. У тебя есть {attempts} попыток.")

    while attempts > 0:
        guess = get_user_guess()
        
        if guess < min_number or guess > max_number:
            print(f"Пожалуйста, введите число в диапазоне от {min_number} до {max_number}.")
            continue

        attempts -= 1
        give_hint(guess, number_to_guess)

        if guess < number_to_guess:
            print("Загаданное число больше.")
        elif guess > number_to_guess:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Ты угадал число {number_to_guess}!")
            return

        if attempts > 0:
            print(f"У тебя осталось {attempts} попыток.")
        else:
            print(f"К сожалению, у тебя закончились попытки. Загаданное число было {number_to_guess}.")

def save_statistics(attempts, success):
    with open("game_statistics.txt", "a") as file:
        if success:
            file.write(f"Угадал с {attempts} попытками.\n")
        else:
            file.write("Не угадал.\n")

def show_statistics():
    try:
        with open("game_statistics.txt", "r") as file:
            print("\nСтатистика игр:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Статистика еще не доступна. Поиграйте в игру.")

def main():
    welcome_message()
    total_games = 0
    total_wins = 0
    
    while True:
        total_games += 1
        play_game()
        
        play_again = input("Хочешь сыграть еще раз? (да/нет): ").strip().lower()
        if play_again == 'да':
            total_wins += 1
            continue
        elif play_again == 'нет':
            print("Спасибо за игру! До свидания!")
            break
        else:
            print("Пожалуйста, ответь 'да' или 'нет'.")

    print(f"\nТы сыграл {total_games} игр, и выиграл {total_wins} из них.")
    show_statistics()

if __name__ == "__main__":
    main()

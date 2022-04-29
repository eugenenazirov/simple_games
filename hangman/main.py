from hangman import game

game_continue = True
mistakes = None

print(r'Игра "Виселица". Компьютер загадывает слово, а ты побуквенно должен его отгадать.')

while not mistakes or mistakes <= 0:
    try:
        mistakes = int(input("Сколько попыток ты себе дашь? : "))
        if mistakes <= 0:
            print(got_invalid_input())
            print("Введи положительное число.")
    except ValueError as val_err:
        print(got_invalid_input())
        print("Введи положительное число.")

game = game.Hangman(mistakes)
game.generate_word()

while game_continue:

    print(f"\n{game.get_visible()}")
    print(f'\nОсталось {game.get_mistakes_remaining()} попыток.')

    user_letter = str(input("Введи свою букву ")).lower()
    if user_letter.isalpha():
        game.turn(user_letter)
        print(f"Уже введеные буквы {game.get_entered_letters()}")
    else:
        print(got_invalid_input())

    if "_" not in game.visible_word:
        print("\nТы отгадал слово! Поздравляю :)")
        game_continue = False

    if game.mistakes_remaining == 0:
        print("\nПопытки закончились! Ты проиграл :(")
        print(f"\nВообще-то я загадал слово {game.word}")
        game_continue = False

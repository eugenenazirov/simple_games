from TrueOrFalse import *
from invalid_operation_exception import InvalidOperationException


def got_invalid_input():
    return "Invalid input, try again!"


def translate_answer(answer: str):
    if answer in ['y', 'yes']:
        return 'Yes'
    else:
        return 'No'


game = None
print("The True or False game. You have to answer the 5 questions.")

while not game:
    try:
        user_mistakes = int(input("\nEnter how many attempts do you give yourself (0-3): "))
        if user_mistakes not in range(4):
            raise InvalidOperationException
        game = TrueOrFalse(user_mistakes, r'Questions.csv')
        print("Start!")

    except (ValueError, InvalidOperationException):
        print(got_invalid_input())
        print("Enter correct number of mistakes (from 0 to 3)")

while game.game_status == GameStatus.IN_PROGRESS:
    print(game.question_counter + 1)
    print(game.current_question.question)

    while True:
        try:
            user_answer = str(input("Enter your answer (Y/N) ")).lower()
            if user_answer not in ['y', 'n', 'yes', 'no']:
                raise InvalidOperationException
            break
        except (ValueError, InvalidOperationException):
            print(got_invalid_input())
            print("Enter correct answer: Yes or No")

    user_answer = translate_answer(user_answer)
    print(f"Your answer is {user_answer}. The correct answer is {game.current_question.right_answer}.")
    print(f"Explanation: {game.current_question.explanation}")
    game.enter_user_guess(user_answer)

    if game.mistakes_counter >= game.allowed_mistakes:
        game.game_status = GameStatus.LOST
        print(
            f"You lost! No more tries.\nRight answers: {game.success_counter}, Wrong answers: {game.mistakes_counter}")
    else:
        if game.question_counter > 4:
            game.game_status = GameStatus.WON
            print(f"You win!\nRight answers: {game.success_counter}, Wrong answers: {game.mistakes_counter}")

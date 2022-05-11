from game_status import GameStatus


class Question:
    def __init__(self, question: str, right_answer: str, explanation: str):
        self.question = question
        self.right_answer = right_answer
        self.explanation = explanation


class TrueOrFalse:
    def __init__(self, allowed_mistakes: int = 2, file_path=None):
        self.__file_path = file_path
        self.allowed_mistakes = allowed_mistakes

        self.mistakes_counter = 0
        self.success_counter = 0
        self.question_counter = 0

        with open(self.__file_path, 'r', encoding='utf-8') as qfile:
            self.all_questions = qfile.readlines()

        self.game_status = GameStatus.IN_PROGRESS
        self.current_question = self.get_current_question()

    def get_current_question(self):
        current_question = self.all_questions[self.question_counter].split(';')
        question = current_question[0]
        right_answer = current_question[1]
        explanation = current_question[2]
        return Question(question, right_answer, explanation)

    def get_next_question(self):
        try:
            self.question_counter += 1
            return self.get_current_question()
        except IndexError:
            pass

    def enter_user_guess(self, user_answer: str):
        if user_answer == self.current_question.right_answer:
            self.success_counter += 1
            self.current_question = self.get_next_question()
        else:
            self.mistakes_counter += 1
            self.current_question = self.get_next_question()

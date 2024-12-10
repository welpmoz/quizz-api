from schemas.quiz import Question, QuizzesPresentation, Quiz
from schemas.answer import Answer, AnswerEvaluated

from database import database

from errors import Format, Missing

async def get_questions(title_quiz: str) -> Quiz:
    try:
        requested_quiz = [
            quiz
            for quiz in database.quizzes
            if quiz.title.lower() == title_quiz.lower()
        ][0]

        return requested_quiz
    except IndexError:
        raise Missing(msg=f'The quiz for {title_quiz} topic does not exists yet!')

async def get_quizzes() -> list[QuizzesPresentation]:
    return database.quizzes


async def get_question(title_quiz: str, number_question: int) -> Question:
    if number_question <= 0:
        raise Format(msg='Questions begins with number 1')
    
    requested_quiz = await get_questions(title_quiz)

    try:
        return requested_quiz.questions[number_question - 1]
    except IndexError:
        raise Missing(f'The quiz {title_quiz} only have {len(requested_quiz.questions)} questions')


async def check_answer(answer: Answer) -> AnswerEvaluated:
    question_to_check = await get_question(answer.title_quiz, answer.number_question)

    return AnswerEvaluated(
        **answer.model_dump(),
        correct_option=question_to_check.answer,
        is_correct=question_to_check.answer == answer.option_marked,
    )

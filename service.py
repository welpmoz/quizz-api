from schemas.quiz import Question, QuizzesPresentation
from schemas.answer import Answer, AnswerEvaluated

from database import database

async def get_questions(title_quiz: str) -> list[Question]:
    requested_quiz = [
        quiz
        for quiz in database.quizzes
        if quiz.title == title_quiz
    ][0]

    return requested_quiz


async def get_quizzes() -> list[QuizzesPresentation]:
    return database.quizzes


async def get_question(title_quiz: str, number_question: int) -> Question:
    requested_question = [
        quiz
        for quiz in database.quizzes
        if quiz.title == title_quiz
    ][0]

    return requested_question.questions[number_question]


async def check_answer(answer: Answer) -> AnswerEvaluated:
    question_to_check = await get_question(answer.title_quiz, answer.number_question)

    return AnswerEvaluated(
        **answer.model_dump(),
        correct_option=question_to_check.answer,
        is_correct=question_to_check.answer == answer.option_marked,
    )

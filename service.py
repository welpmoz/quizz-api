from schemas import Question, QuizzesPresentation, database

async def get_questions(title_quiz: str) -> list[Question]:
    requested_quiz = [
        quiz
        for quiz in database.quizzes
        if quiz.title == title_quiz
    ][0]

    return requested_quiz.questions


async def get_quizzes() -> list[QuizzesPresentation]:
    return database.quizzes
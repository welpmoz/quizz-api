from fastapi import FastAPI

from schemas.quiz import QuizzesPresentation, Question, Quiz
from schemas.answer import Answer, AnswerEvaluated

import service as service


app = FastAPI()


@app.get('/quizzes', response_model=list[QuizzesPresentation])
async def get_quizzes():
    return await service.get_quizzes()


@app.get('/quizzes/{titleQuiz}', response_model=Quiz)
async def get_quiz(titleQuiz: str):
    return await service.get_questions(titleQuiz)


@app.get('/quizzes/{titleQuiz}/questions', response_model=Question)
async def get_question_for_exam(titleQuiz: str, numberQuestion: int = 1):
    return await service.get_question(titleQuiz, numberQuestion)


@app.post('/answer', response_model=AnswerEvaluated)
async def check_answer(answer: Answer):
    return await service.check_answer(answer)

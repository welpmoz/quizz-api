from pydantic import Field

from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from schemas.quiz import QuizzesPresentation, Question, Quiz
from schemas.answer import Answer, AnswerEvaluated

import service as service

from errors import handle_common_errors

app = FastAPI()

app.mount("/images", StaticFiles(directory='images'), name='images')

@app.get('/')
async def redirect_to_docs():
    return RedirectResponse('/docs');


@app.get('/quizzes', response_model=list[QuizzesPresentation])
async def get_quizzes():
    try:
        return await service.get_quizzes()
    except Exception as exc:
        handle_common_errors(exc)



@app.get('/quizzes/{titleQuiz}', response_model=Quiz)
async def get_quiz(titleQuiz: str):
    try:
        return await service.get_questions(titleQuiz)
    except Exception as exc:
        handle_common_errors(exc)


@app.get('/quizzes/{titleQuiz}/questions', response_model=Question)
async def get_question_for_exam(
    titleQuiz: str,
    numberQuestion: int,
):
    try:
        return await service.get_question(titleQuiz, numberQuestion)
    except Exception as exc:
        handle_common_errors(exc)


@app.post('/answer', response_model=AnswerEvaluated)
async def check_answer(answer: Answer):
    try:
        return await service.check_answer(answer)
    except Exception as exc:
        handle_common_errors(exc)

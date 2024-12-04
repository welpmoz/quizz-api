from fastapi import FastAPI

from schemas import QuizzesPresentation, Question
import service as service


app = FastAPI()


@app.get('/quizzes', response_model=list[QuizzesPresentation])
async def get_quizzes():
    return await service.get_quizzes()


@app.get('/quizzes/{titleQuiz}', response_model=list[Question])
async def get_questions(titleQuiz: str):
    return await service.get_questions(titleQuiz)

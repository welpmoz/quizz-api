from pydantic import BaseModel, ConfigDict

class Question(BaseModel):
    question: str
    options: list[str]
    answer: str


class QuizBase(BaseModel):
    title: str
    icon: str


class Quiz(QuizBase):
    questions: list[Question]


class Quizzes(BaseModel):
    quizzes: list[Quiz]



class QuizzesPresentation(QuizBase):
    pass
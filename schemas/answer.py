from pydantic import BaseModel


class Answer(BaseModel):
    title_quiz: str
    number_question: int
    option_marked: str


class AnswerEvaluated(Answer):
    correct_option: str
    is_correct: bool

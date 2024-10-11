from pydantic import BaseModel
from typing import Literal

from pitchpro.constants.learner_persona_enums import domain_and_courses


class ChatbotRequest(BaseModel):
    user_id: str
    course_name: Literal[*list(*[list(x["courses"].keys()) for x in domain_and_courses.values()])]
    question: str

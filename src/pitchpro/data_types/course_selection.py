from typing import Literal
from pydantic import BaseModel
from pitchpro.constants.learner_persona_enums import domain_and_courses

class CourseSelection(BaseModel):
    course_domain: Literal[*list(domain_and_courses.keys())]
    course_name: Literal[*list(*[list(x["courses"].keys()) for x in domain_and_courses.values()])]
from pydantic import BaseModel
from typing import Literal

class LearnerPersona(BaseModel):
    learner_type: Literal['tech', 'non-tech']
    # learner_work_ex: Literal[]

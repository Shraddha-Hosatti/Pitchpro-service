from pydantic import BaseModel
from typing import Literal
from pitchpro.constants.learner_persona_enums import (
    reverse_job_profile,
    reverse_job_workexp,
    reverse_job_domains,
    rev_industries_map
)

class LearnerPersona(BaseModel):
    learner_type: Literal[*list(reverse_job_profile.keys())]
    learner_work_ex: Literal[*list(reverse_job_workexp.keys())]
    learner_domain: Literal[*list(reverse_job_domains.keys())]
    learner_industry: Literal[*list(rev_industries_map.keys())]

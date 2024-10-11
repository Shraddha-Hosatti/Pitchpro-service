from pitchpro.data_types.course_selection import CourseSelection
from pitchpro.data_types.learner_persona import LearnerPersona
import json

def load_dict(course_selection: CourseSelection):
    loaded_dict = {}

    base_dict = json.load(open(f"/app/assets/{course_selection.course_domain}/{course_selection.course_name}/personalised_pitch.json"))

    for item in base_dict:
        loaded_dict[(
            item["learner_type"],
            item["learner_work_ex"],
            item["learner_domain"]
        )] = item["Tables"]

    return loaded_dict


def get_personalised_pitch(learner_persona: LearnerPersona, course_selection: CourseSelection):

    loaded_dict = load_dict(course_selection)

    if (learner_persona.learner_type,learner_persona.learner_work_ex,learner_persona.learner_domain) in loaded_dict:
        return loaded_dict[(
            learner_persona.learner_type,
            learner_persona.learner_work_ex,
            learner_persona.learner_domain
        )]
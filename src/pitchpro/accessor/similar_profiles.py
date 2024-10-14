import json

from pitchpro.data_types.course_selection import CourseSelection
from pitchpro.data_types.learner_persona import LearnerPersona


def load_dict(course_selection: CourseSelection):
    base_dict = json.load(open(f"/app/assets/{course_selection.course_domain}/similar_profiles.json"))

    loaded_dict = {}

    for item in base_dict:
        loaded_dict[
            (item["learner_profile"], item["learner_work_exp"])
        ] = item["similar_profiles"]

    return loaded_dict


def get_similar_profiles(learner_persona: LearnerPersona, course_selection: CourseSelection):
    loaded_dict = load_dict(course_selection)

    key = (learner_persona.learner_type, learner_persona.learner_work_ex)
    if key in loaded_dict:
        return loaded_dict[key]
    else:
        return {}

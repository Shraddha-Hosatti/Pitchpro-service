from pitchpro.data_types.course_selection import CourseSelection
from pitchpro.data_types.learner_persona import LearnerPersona
import json

def load_dict(course_selection: CourseSelection):
    loaded_dict = dict()

    base_dict = json.load(open(f"/app/assets/{course_selection.course_domain}/{course_selection.course_name}/competetive_analysis.json"))

    for item in base_dict:
        loaded_dict[(
            item["learner_type"],
            item["learner_work_ex"]
        )] = item["comparison"]

    print(loaded_dict)

    return loaded_dict

def competetive_analysis(learner_persona: LearnerPersona, course_selection: CourseSelection):
    loaded_dict = load_dict(course_selection)

    learner_work_exp = "non_experience"if learner_persona.learner_work_ex == "0_2" else "experience"

    if (learner_persona.learner_type,learner_work_exp) in loaded_dict:
        return loaded_dict[(
            learner_persona.learner_type,
            learner_work_exp
        )]
from pitchpro.constants.learner_persona_enums import (
    reverse_job_profile,
    reverse_job_workexp,
    reverse_job_domains,
    rev_industries_map,
    domain_and_courses
)


def make_ui_constants():
    return {
        "learner_persona": {
            "job_profile" : reverse_job_profile,
            "job_workexp" : reverse_job_workexp,
            "job_domains" : reverse_job_domains,
            "job_industry" : rev_industries_map
        },
        "courses": domain_and_courses
    }
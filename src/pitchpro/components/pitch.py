from pitchpro.accessor.personalised_pitch import get_personalised_pitch
from pitchpro.accessor.competetive_analysis import competetive_analysis
from pitchpro.accessor.similar_profiles import get_similar_profiles


def make_pitch(learner_persona, course_selection) :
    return {
        "personalised_pitch": get_personalised_pitch(learner_persona, course_selection),
        "competitive_analysis": competetive_analysis(learner_persona, course_selection),
        "similar_profiles": get_similar_profiles(learner_persona, course_selection)
    }
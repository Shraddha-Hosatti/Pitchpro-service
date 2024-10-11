from pitchpro.chatbot.rag_chain import get_rag_chain
from pitchpro.chatbot.retreiver import get_retriever_object
from pitchpro.constants.learner_persona_enums import domain_and_courses

def load_model(memory):
    courses = []
    for c in domain_and_courses.values():
        courses.extend(list(c["courses"].keys()))

    models = {}
    for course in courses:
        models[course] = get_rag_chain(
            get_retriever_object(course), memory
        )

    return models
from fastapi import FastAPI

from pitchpro.chatbot import load_model
from pitchpro.components.ui_constants import make_ui_constants
from pitchpro.data_types.chatbot_clear_chat_request import ChatbotClearChatRequest
from pitchpro.data_types.learner_persona import LearnerPersona
from pitchpro.data_types.course_selection import CourseSelection
from pitchpro.data_types.chatbot_request import ChatbotRequest

from pitchpro.components.pitch import make_pitch
from pitchpro.components.chatbot import make_chatbot_response
from pitchpro.components.chatbot import clear_chat_history

from ttldict import TTLOrderedDict
app = FastAPI()
memory = TTLOrderedDict(24*60*60)
models = load_model(memory)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/constants")
def get_constants():
    return make_ui_constants()

@app.post("/pitch")
def get_pitch(learner_persona: LearnerPersona, course_selection: CourseSelection):
    return make_pitch(learner_persona, course_selection)

@app.post("/chatbot")
def get_chatbot_response(chatbot_request: ChatbotRequest):
    if chatbot_request.course_name not in models:
        return {
            "answer": "Course name is not "
        }
    return make_chatbot_response(chatbot_request.user_id, chatbot_request.question, models[chatbot_request.course_name])

@app.post("/clear_chat")
def clear_chat(chatbotClearChatRequest: ChatbotClearChatRequest):
    clear_chat_history(memory, chatbotClearChatRequest.user_id)

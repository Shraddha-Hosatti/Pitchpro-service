from fastapi import FastAPI
from pitchpro.data_types.learner_persona import LearnerPersona

app = FastAPI()


@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/learner-persona-options")
def get_leaner_persona_options():
    pass

@app.post("/pitch")
def get_pitch(learner_persona: LearnerPersona):
    print(learner_persona)

# # @app.get("/")
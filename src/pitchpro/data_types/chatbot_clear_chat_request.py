from pydantic import BaseModel

class ChatbotClearChatRequest(BaseModel):
    user_id: str

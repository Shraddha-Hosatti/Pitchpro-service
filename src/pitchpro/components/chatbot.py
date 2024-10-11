def make_chatbot_response(user_id, question, model):
    try:
        response = model.invoke(
            {"input": question},
            config={
                "configurable": {"session_id": user_id}
            }
        )

        if "answer" in response:
            return {
                "answer": response["answer"]
            }
        else:
            return {
                "answer": "Model is facing some error"
            }
    except:
        return {
            "answer": "Model is facing some error"
        }


def clear_chat_history(memory, user_id):
    if user_id in memory:
        del memory[user_id]
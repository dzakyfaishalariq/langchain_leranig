from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model
from langchain.agents import create_agent

# os.environ('GOOGLE_API_KEY') = os.getenv('GOOGLE_API_KEY')
llm = init_chat_model(
    api_key=os.getenv('GOOGLE_API_KEY'),
    model="google_genai:gemini-2.5-flash-lite"
    )

def Ai(input: str):
    print("mulai agent")
    agent = create_agent(
        model=llm
    )
    result = agent.invoke({
        "messages":[{
            "role":'user', "content":input
        }]
    })
    return result


if __name__ == "__main__":
    perintah = input('Masukan perintah:')
    hasil = Ai(perintah)
    for h in hasil['messages']:
        print(h.content)
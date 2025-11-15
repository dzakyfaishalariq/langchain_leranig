from langchain.chat_models import init_chat_model
from tool.tool1 import *
from langchain.agents import create_agent
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
llm = init_chat_model(
    model ="groq:openai/gpt-oss-20b"
)

tool_saya = Alat_saya()

def AI(input: str):
    agent = create_agent(
        model=llm,
        tools=[tool_saya.sapaan]
    )
    respon = agent.invoke(
        {
            "messages":[{
                "role":"user",
                "content":input
            }]
        }
    )
    return respon['messages']

if __name__ == "__main__":
    inputan = input("Masukan Perintah : ")
    respon = AI(inputan)
    i:int = 0
    for r in respon:
        print(f"Step:{i}")
        if r.content == []:
            print("Menggunakan tool")
        print(r.content)
        i += 1

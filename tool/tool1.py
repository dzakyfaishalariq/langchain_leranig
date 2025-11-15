from langchain.tools import tool

# @tool
# def sapaan(nama:str)->str:
#     """DI gunakan untuk sapaan pada saat memulai chat dengan user"""
#     return f"Assalamualaikum warohmatullahi wabarokatu, wasapp gays dan hallo {nama}"

class Alat_saya:
    def __init__(self):
        pass

    @tool
    def sapaan(nama:str)->str:
        """DI gunakan untuk sapaan pada saat memulai chat dengan user"""
        return f"Assalamualaikum warohmatullahi wabarokatu, wasapp gays dan hallo {nama}"
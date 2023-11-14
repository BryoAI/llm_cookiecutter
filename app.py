import sys

import largelanguagemodel
import llama


class App:
    def __init__(self, llm: largelanguagemodel.LargeLanguageModel):
        self.llm = llm

    def ask_llm(self, question: str) -> str:
        return self.llm.query(f"Q: {question}. A: ")

    def ask_llm_terminal(self) -> None:
        user_input = input("Enter your question: ")
        print(self.ask_llm(user_input))

def run() -> None:
    llm = llama.Llama()
    app = App(llm=llm)
    while True:
        app.ask_llm_terminal()

if __name__ == "__main__":
    run()

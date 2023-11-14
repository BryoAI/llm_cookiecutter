import sys

import largelanguagemodel
import llama


class App:
    def __init__(self, llm: largelanguagemodel.LargeLanguageModel):
        self.llm = llm

    def ask_llm(self, question: str) -> str:
        # This also prints to the terminal so no need to print the returned str
        return self.llm.query(f"Q: {question}. A: ")

    def ask_llm_terminal(self) -> None:
        user_input = input("Enter your question: ")
        self.ask_llm(user_input)

def run() -> None:
    llm = llama.Llama()
    app = App(llm=llm)
    while True:
        app.ask_llm_terminal()

if __name__ == "__main__":
    run()

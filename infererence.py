from llm import llama
import sys

llm = llama()
def ask_llm():
    user_input = input("Enter your question: ")
    question = "Q: {}. A: ".format(user_input)
    output = llm.llm(question)
    print("\n\n\n")
    print("-"*100)
    print("Ignore the following LlamaCpp Warning")
    print("-"*100)
    return output

if __name__ == "__main__":
    ask_llm()
    

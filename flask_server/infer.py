from llm import llama

llm = llama()

# write a function that takes the question as input from the user via terminal, calls the query_llm function of llm and prints the output
def ask_llm():
    question = input("Enter your question: ")
    output = llm.query_llm(question)
    print(output)

ask_llm()





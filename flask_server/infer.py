from llm import llama

llm = llama()

# write a function that takes the question as input from the user via terminal, calls the query_llm function of llm and prints the output
def ask_llm():
    question = input("Enter your question: ")
    # for response_chunk in llm.query_llm(question):
    #     # print in same line
    #     print(response_chunk, end='')
    #     # print(response_chunk)
    # # print(output)
    print(question)
    return llm.llm(question)
    #return llm.query_llm(question)

ask_llm()





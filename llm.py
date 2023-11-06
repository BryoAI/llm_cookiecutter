from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class llama:
    def __init__(self):
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        self.llm = LlamaCpp(
    model_path="./../code/llama-2-7b-chat.Q6_K.gguf",
    input={"temperature": 0.75, "max_length": 2000, "top_p": 1},
    callback_manager=callback_manager,
    verbose=True,
)
    def query_llm(self, query):
        print(query)
        return self.llm(query)

    # def query_llm(self, question):
    #     for response_chunk in self.llm(question):
    #         yield response_chunk
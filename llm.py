from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class llama:
    def __init__(self):
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        self.llm = LlamaCpp(
    model_path="./../code/llama-2-7b-chat.Q6_K.gguf",
    temperature= 0.75,
    top_p= 1,
    callback_manager=callback_manager,
    verbose=False,
    stop=["Q:", "\n"]
)
    def query_llm(self, query):
        return self.llm(query)

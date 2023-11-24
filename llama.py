from dataclasses import dataclass, field

from langchain import llms
from langchain.callbacks import manager, streaming_stdout

import largelanguagemodel

@dataclass
class LlamaSettings:
    model_path: str = "./model/llama-2-7b-chat.Q6_K.gguf"
    temperature: float = 0.75
    top_p: int = 1
    verbose: bool = False
    stop: list = field(default_factory=lambda: ["Q:", "\n"])
    callback_manager: callable = manager.CallbackManager(
        [streaming_stdout.StreamingStdOutCallbackHandler()]
        )

class Llama(largelanguagemodel.LargeLanguageModel):
    def __init__(self, settings: LlamaSettings=None):
        if settings is None:
            settings = LlamaSettings()
        self.llm = llms.LlamaCpp(
            model_path = settings.model_path,
            temperature = settings.temperature,
            top_p = settings.top_p,
            callback_manager = settings.callback_manager,
            verbose = settings.verbose,
            stop = settings.stop
        )

    def query(self, query: str) -> str:
        return self.llm(query)

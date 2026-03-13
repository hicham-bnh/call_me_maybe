from llm_sdk import Small_LLM_Model
import json

class Llm:
    def __init__(self) -> None:
        self.model = Small_LLM_Model()
        
    def get_vocab(self):
        vocab_path = self.model.get_path_to_vocab_file()
        with open(vocab_path) as fd:
            data = json.load(fd)
        print(vocab_path)
        print(data)
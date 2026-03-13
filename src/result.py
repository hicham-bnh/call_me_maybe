from llm_sdk import Small_LLM_Model
import json
from typing import Dict

class Llm:
    def __init__(self) -> None:
        self.model = Small_LLM_Model()
        self.vocab: Dict


    def get_vocab(self):
        vocab_path = self.model.get_path_to_vocab_file()
        with open(vocab_path, encoding='utf-8') as fd:
            self.vocab = json.load(fd)
        print(self.vocab)
        
from llm_sdk import Small_LLM_Model
import json
from typing import Dict

class Llm:
    def __init__(self) -> None:
        self.model = Small_LLM_Model()
        self.token_to_id: Dict[str, int]
        self.id_to_token: Dict[int, str]


    def get_vocab(self):
        vocab_path = self.model.get_path_to_vocab_file()
        with open(vocab_path) as fd:
            self.token_to_id = json.load(fd)
        self.id_to_token = {int(v): k for k, v in self.token_to_id.items()}
        print(self.id_to_token)
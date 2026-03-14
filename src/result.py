from llm_sdk import Small_LLM_Model
import json
from typing import Dict
from src.parsing import Parsing


class Llm:
    def __init__(self, pars: Parsing) -> None:
        self.model = Small_LLM_Model()
        self.vocab: Dict = {}
        self.token_to_id: Dict = {}
        self.id_to_token: Dict = {}
        self.pars = pars

    def get_vocab(self):
        vocab_path = self.model.get_path_to_vocab_file()
        with open(vocab_path, encoding='utf-8') as fd:
            self.vocab = json.load(fd)
        self.token_to_id = {v: k for k, v in self.vocab.items()}
        self.id_to_token = {k: v for k, v in self.vocab.items()}

    def get_func(self):
        tokens_functions = {
            name: self.model.encode(name) for name in self.pars.func_name
            }
        data = {k:v.tolist()[0] for k,v in tokens_functions.items()}
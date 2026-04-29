from llm_sdk import Small_LLM_Model
import json
import numpy as np

class Answer:
	def __init__(self) -> None:
		self.llm = Small_LLM_Model()
		self.path_vocab = None
		self.id_to_token = None
		self.vocab = None

	def get_vocab(self):
		self.path_vocab = self.llm.get_path_to_vocab_file()
		with open(self.path_vocab, 'r') as fd:
			self.vocab = json.load(fd)
		self.id_to_token = {v: k for k, v in self.vocab.items()}
	
	def add_mask(self):
		
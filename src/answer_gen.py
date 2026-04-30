from llm_sdk import Small_LLM_Model
import json
import numpy as np
from .parsing import Pars

class Answer:
	def __init__(self) -> None:
		self.llm = Small_LLM_Model()
		self.path_vocab = None
		self.id_to_token = None
		self.vocab = None
		self.parser = Pars()

	def get_vocab(self):
		self.path_vocab = self.llm.get_path_to_vocab_file()
		with open(self.path_vocab, 'r') as fd:
			self.vocab = json.load(fd)
		self.id_to_token = {v: k for k, v in self.vocab.items()}
	
	
	def function_token(self):
		prompts, function = self.parser.open_files()
		function_name = [definition.name for definition in function]
		prompt_test = [prompt.prompt for prompt in prompts]
		test = self.llm.encode(prompt_test[0]).tolist()[0]
		logits = self.llm.get_logits_from_input_ids(test)
		big = logits.index(max(logits))
		print(prompt_test[0])
		print(self.llm.decode([big]))
		function_name_token = [self.llm.encode(name).tolist()[0] for name in function_name]
		print(function_name_token)
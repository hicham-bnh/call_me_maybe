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
		function_name_token = [self.llm.encode(name).tolist()[0] for name in function_name]
		generated = []
		while (True):
			print(prompt_test[10])
			if generated in function_name_token:
				break
			test = self.llm.encode(prompt_test[10]).tolist()[0]
			logits = self.llm.get_logits_from_input_ids(test)
			valid_tokens = set()
			for tokens in function_name_token:
				if tokens[:len(generated)] == generated:
					valid_tokens.add(tokens[len(generated)])
			for token_id in range(len(logits)):
				if token_id not in valid_tokens:
					logits[token_id] = float('-inf')
			generated.append(logits.index(max(logits)))
			prompt_test[10] += self.llm.decode(generated[-1])
		print(self.llm.decode(generated))
		#print(prompt_test[10])
		#print(function_name_token)
		#print(function_name_token[0])
		#print(self.llm.decode([8822]))
		#print(self.llm.decode([2891]))
		#print(self.llm.decode([32964]))

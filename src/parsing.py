import argparse
from pydantic import BaseModel
from typing import Any, List
from pathlib import Path
import json
import os

class Pars:
	def __init__(self) -> None:
		self.parser = argparse.ArgumentParser()
		self.args: Any = None
		
	def default_pars(self) -> None:
		self.parser.add_argument('--functions_definition',
			default='data/input/functions_definition.json')
		self.parser.add_argument('--input',
			default='data/input/function_calling_tests.json')
		self.parser.add_argument('--output',
			default='data/output/function_calls.json')
		self.args = self.parser.parse_args()
		output = Path(self.args.output)
		output.parent.mkdir(parents=True, exist_ok=True)


	def pars_file(self, files: List[str]) -> None:
		self.parser.add_argument('--functions_definition',
			default=files[1])
		self.parser.add_argument('--input',
			default=files[2])
		self.parser.add_argument('--output',
			default=files[3])
		self.args = self.parser.parse_args()
		output = Path(self.args.output)
		output.parent.mkdir(parents=True, exist_ok=True)

	
	def open_files(self) -> None:
		with open(self.args.input, "r", encoding='utf-8') as fd:
			promps = json.load(fd)
		for k in promps:
			print(k['prompt'])
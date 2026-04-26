import argparse
from pydantic import BaseModel
from typing import List
from pathlib import Path
import os

class Pars(BaseModel):
	def default_pars(self) -> None:
		parser = argparse.ArgumentParser()
		parser.add_argument('--functions_definition',
			default='data/input/functions_definition.json')
		parser.add_argument('--input',
			default='data/input/function_calling_tests.json')
		parser.add_argument('--output',
			default='data/output/function_calls.json')
		args = parser.parse_args()
		output = Path(args.output)
		output.parent.mkdir(parents=True, exist_ok=True)


	def pars_file(self, files: List[str]) -> None:
		parser = argparse.ArgumentParser()
		parser.add_argument('--functions_definition',
			default=files[1])
		parser.add_argument('--input',
			default=files[2])
		parser.add_argument('--output',
			default=files[3])
		args = parser.parse_args()
		output = Path(args.output)
		output.parent.mkdir(parents=True, exist_ok=True)

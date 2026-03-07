from src.default import files
import argparse
from typing import List, Dict
import json
from pydantic import BaseModel


class Parsing:
    intput_function: str
    intput_call: str 
    output_file: str
    def pars_files(self):
        file_lunch = files()
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--functions_definition",
            default="data/input/functions_definition.json"
            )
        parser.add_argument(
            "--input",
            default="data/input/function_calling_tests.json"
        )
        parser.add_argument(
            "--output",
            default="data/output/functions_calls.json"
        )
        args = parser.parse_args()
        self.intput_function = args.functions_definition
        self.intput_call = args.input
        self.output_file = args.output
        file_lunch.lunch(self.output_file)
        with open(self.intput_call, "r") as f:
            data = json.load(f)
        for l in data:
            print(l['prompt'])
        with open(self.intput_function, "r") as f:
            func = json.load(f)
        for f in func:
            print(f['name'])

from src.default import files
import argparse
from typing import List, Dict, Any
import json
from pydantic import BaseModel
from llm_sdk import Small_LLM_Model


class Parsing:
    def __init__(self) -> None:
        self.intput_function: str
        self.intput_call: str 
        self.output_file: str
        self.data_call: Any
        self.data_func: Any

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
            self.data_call = json.load(f)
        with open(self.intput_function, "r") as f:
            self.data_func = json.load(f)

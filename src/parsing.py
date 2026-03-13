from src.default import Files
import argparse
from typing import List, Dict, Any
import json
from pydantic import BaseModel
from enum import Enum


class Parsing:
    def __init__(self) -> None:
        self.intput_function: str
        self.intput_call: str
        self.output_file: str
        self.data_call: Any
        self.data_func: Any

    def pars_files(self):
        try:
            file_lunch = Files()
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
            Calling(prompt=self.data_call)
            with open(self.intput_function, "r") as f:
                self.data_func = json.load(f)
            FunctionDefinitions(functions=self.data_func)
            return self.data_call, self.data_func
        except Exception as e:
            print(e)
        return 0, 0

class ParameterType(Enum):
    NUMBER = 'number'
    STRING = 'string'
    BOOLEAN = 'boolean'
    INTEGER = 'integer'

class ParameterDefinition(BaseModel):
    type: ParameterType

class ReturnDefinition(BaseModel):
    type: ParameterType

class FunctionDefinition(BaseModel):
    name: str
    description: str
    parameters: Dict[str, ParameterDefinition]
    returns: ReturnDefinition

class FunctionDefinitions(BaseModel):
    functions: List[FunctionDefinition]

class Calling(BaseModel):
    prompt: List[Dict[str, str]]
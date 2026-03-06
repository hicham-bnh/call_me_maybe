import sys
import argparse
from src.default import result_input


if __name__ == "__main__":
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
        print("Functions:", args.functions_definition)
        print("Input:", args.input)
        print("Output:", args.output)
        with open(args.functions_definition, "r") as fd:
            test = fd.read()
            print(test)
        result_input(args.output)

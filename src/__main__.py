import sys
import argparse
from src.default import result_input


if __name__ == "__main__":
    if len(sys.argv) < 2:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--functions_definition",
            default="data/input/functions_definition.json"
            )
        parser.add_argument(
            "--input",
            default="data/input/function_calling_tests.json"
        )
        result_input()
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
    else:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--functions_definition",
            default="data/input/functions_definition.jason"
            )
        parser.add_argument(
            "--input",
            default="data/input/function_calling_tests.jason"
        )
        result_input()
        parser.add_argument(
            "--output",
            default="data/output/functions_calls.jason"
        )
        args = parser.parse_args()
        print("Functions:", args.functions_definition)
        print("Input:", args.input)
        print("Output:", args.output)
        
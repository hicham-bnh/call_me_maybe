from src.default import result_input
import argparse

def pars_files():
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
    result_input(args.output)
from llm_sdk import Small_LLM_Model
import os


def result_input():
    try:
        parent_folder = "data"
        new_folder = "output"
        os.makedirs(os.path.join(parent_folder, new_folder), exist_ok=True)
    except Exception as e:
        print(e)
    try:
        with open('data/output/function_calls.json', 'w') as fd:
            fd.write("test")
    except Exception as e:
        print(e)
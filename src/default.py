from llm_sdk import Small_LLM_Model
import os


def result_input(folder: str | None):
    if folder is None:
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
    else:
        output = folder.split("/")
        try:
            parent_folder = output[0]
            new_folder = output[1]
            os.makedirs(os.path.join(parent_folder, new_folder), exist_ok=True)
        except Exception as e:
            print(e)
        try:
            with open(f'{output[0]}/{output[1]}/function_calls.json', 'w') as fd:
                fd.write("test")
        except Exception as e:
            print(e)
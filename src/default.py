from llm_sdk import Small_LLM_Model
import os
from typing import List
import json

class files:
    ouput_file: str
    def lunch(self, folder: str | None) -> None:
        if folder is None:
            try:
                parent_folder: str = "data"
                new_folder: str = "output"
                os.makedirs(os.path.join(parent_folder, new_folder), exist_ok=True)
            except Exception as e:
                print(e)
            try:
                with open('data/output/function_calls.json', 'w') as fd:
                    fd.write("test")
            except Exception as e:
                print(e)
        else:
            output: List[str] = folder.split("/")
            try:
                parent_folder = output[0]
                new_folder = output[1]
                os.makedirs(os.path.join(parent_folder, new_folder), exist_ok=True)
            except Exception as e:
                print(e)
            try:
                with open(f'{output[0]}/{output[1]}/function_calls.json', 'w') as fd:
                    json.dump("first test reussi", fd)
                self.ouput_file = f"{output[0]}/{output[1]}/function_calls.json"
            except Exception as e:
                print(e)

    def add_to_ouput_file(self):
        # test
        try:
            test = {
                "hello": 4,
                "hicham": "bg",
                "tfo": 20.12
            }
            test2 = {
                "maximart": 8,
                "sunny": 20,
                "mobenias": 0.1
            }
            data = [test, test2]
            with open(self.ouput_file , "a") as fd:
                json.dump(data, fd, indent=3)
        except Exception as e:
            print(e)
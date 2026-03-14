import os
from typing import List
import json


class Files:
    def __init__(self) -> None:
        self.ouput_file: str = ""

    def lunch(self, folder: str) -> None:
        try:
            parent_folder = os.path.dirname(folder)
            if parent_folder:
                os.makedirs(parent_folder, exist_ok=True)
            self.ouput_file = folder
        except Exception as e:
            print(e)

    def add_to_ouput_file(self, data: List):
        try:
            with open(self.ouput_file, "w") as fd:
                json.dump(data, fd, indent=2)
        except Exception as e:
            print(e)

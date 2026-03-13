from src.parsing import Parsing
from src.default import Files
from src.result import Llm

if __name__ == "__main__":
        try:
                llm = Llm()
                pars = Parsing()
                call, func = pars.pars_files()
                llm.get_vocab()
        except Exception as e:
                print(e)
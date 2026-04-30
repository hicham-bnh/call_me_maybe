import sys
from .parsing import Pars
from .answer_gen import Answer


if __name__ == "__main__":
        gen = Answer()
        if (len(sys.argv) == 1):
            gen.parser.default_pars()
        elif (len(sys.argv) == 7):
            gen.parser.pars_file(sys.argv)
        elif (len(sys.argv) != 4):
            print("error")
        gen.get_vocab()
        gen.function_token()

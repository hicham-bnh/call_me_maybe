import sys
from .parsing import Pars
from .answer_gen import Answer


if __name__ == "__main__":
    try:
        test = Pars()
        gen = Answer()
        if (len(sys.argv) == 1):
            test.default_pars()
        elif (len(sys.argv) == 7):
            test.pars_file(sys.argv)
        elif (len(sys.argv) != 4):
            print("error")
        test.open_files()
        gen.get_vocab()
    except Exception as e:
        print(e)
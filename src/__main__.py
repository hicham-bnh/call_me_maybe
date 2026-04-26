import sys
from .parsing import Pars


if __name__ == "__main__":
    test = Pars()
    if (len(sys.argv) == 1):
        test.default_pars()
    elif (len(sys.argv) == 7):
        test.pars_file(sys.argv)
    elif (len(sys.argv) != 4):
        print("error")

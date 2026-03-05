import sys
from src.default import result_input


if __name__ == "__main__":
    if len(sys.argv) < 2:
        result_input()
    else:
        print("fichier")
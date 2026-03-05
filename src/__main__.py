from llm_sdk import Small_LLM_Model
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("default")
    else:
        print("fichier")
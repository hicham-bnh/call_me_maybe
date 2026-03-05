from llm_sdk import Small_LLM_Model

if __name__ == "__main__":
    test = Small_LLM_Model()
    result = test.encode("bonjour")
    print(result)
    result2 = test.decode(result)
    print(result2)

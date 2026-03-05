from llm_sdk import llm_sdk as llm


if __name__ == "__main__":
    test = llm.Small_LLM_Model()
    print(test.get_logits_from_input_ids([48, 95, 21, 63, 48]))
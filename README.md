*This project has been created as part of the 42 curriculum by mobenhab.*

# call me maybe — Introduction to Function Calling in LLMs

## Description

**call me maybe** is a function calling tool that translates natural language prompts into structured, machine-executable function calls. Given a prompt like *"What is the sum of 40 and 2?"*, the system does not answer `42` — instead, it identifies the correct function and extracts the right arguments:

```json
{
  "name": "fn_add_numbers",
  "parameters": { "a": 40.0, "b": 2.0 }
}
```

The core challenge is reliability. Small language models (sub-1B parameters) generate valid JSON only ~30% of the time when prompted naively. This project achieves **100% valid JSON output** and **90%+ function selection accuracy** using **constrained decoding** — a technique that guides token-by-token generation to guarantee structural and schema compliance, without relying on prompting alone.

The model used is **Qwen/Qwen3-0.6B** via a custom `llm_sdk` wrapper.

---

## Instructions

### Requirements

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- The `llm_sdk` package placed at the root of the project (same level as `src/`)

### Installation

```bash
uv sync
```

This installs all dependencies declared in `pyproject.toml` (including `numpy` and `pydantic`) into a virtual environment managed by `uv`.

### Running the program

```bash
uv run python -m src
```

By default, input files are read from `data/input/` and output is written to `data/output/`.

You can specify custom paths:

```bash
uv run python -m src \
  --functions_definition data/input/functions_definition.json \
  --input data/input/function_calling_tests.json \
  --output data/output/function_calls.json
```

### Makefile targets

| Target | Description |
|--------|-------------|
| `make install` | Install project dependencies via `uv` |
| `make run` | Run the main program |
| `make debug` | Run in debug mode with `pdb` |
| `make clean` | Remove `__pycache__`, `.mypy_cache`, etc. |
| `make lint` | Run `flake8` and `mypy` with required flags |
| `make lint-strict` | Run `mypy --strict` for enhanced checking |

---

## Algorithm Explanation

### Constrained Decoding

Language models generate text one token at a time. At each step, the model outputs a **logit vector** — raw scores for every token in its vocabulary. Normally, the highest-scoring token is selected. The problem: nothing stops the model from producing syntactically broken or schema-invalid JSON.

Constrained decoding intercepts this process:

1. **The model produces logits** over its full vocabulary.
2. **A constraint engine** determines which tokens are valid at the current generation state (based on JSON structure and the expected schema).
3. **Invalid token logits are set to `-inf`** (negative infinity), effectively removing them from consideration.
4. **The next token is sampled** only from the remaining valid set.

This loop repeats until the full JSON object is generated. Every token produced is guaranteed to be valid — both syntactically (well-formed JSON) and semantically (matches the function schema).

### Schema-Aware Constraints

The constraint engine is aware of the full output schema at every step:

- When generating the `"name"` field: only tokens that form one of the known function names are allowed.
- When generating a `number` argument: only digit tokens, `.`, `-`, and `e` notation tokens are permitted.
- When generating a `string` argument: any printable character is allowed, but the closing `"` is controlled to prevent premature termination.
- When generating `boolean` values: only `true` or `false` are valid.

The vocabulary JSON (provided by `llm_sdk.get_path_to_vocabulary_json()`) maps token IDs to their string representations. This mapping is used to pre-compute which tokens can legally appear at each position in the target schema.

### Function Selection

The function to call is **selected by the LLM**, not by heuristics. A prompt is constructed that describes all available functions and asks the model which one best matches the user's intent. The model's response is constrained to one of the valid function names, ensuring the selection is both model-driven and structurally valid.

---

## Design Decisions

- **Pydantic for all data models**: Input files, function definitions, and output results are all validated using Pydantic models. This provides clear error messages and type safety throughout.
- **Separation of concerns**: The constrained decoder, the function selector, and the argument extractor are implemented as independent modules, making the system easy to test and extend.
- **Pre-computed token masks**: Rather than recomputing valid token sets from scratch at every step, masks are partially pre-computed per schema type (number, string, boolean, enum) to reduce latency.
- **Graceful error handling**: Every I/O operation (file reading, JSON parsing, model calls) is wrapped in try-except blocks. The program never crashes unexpectedly — it logs the error and continues processing remaining prompts.
- **No private SDK internals**: Only the public API of `llm_sdk` is used (`get_logits_from_input_ids`, `encode`, `decode`, `get_path_to_vocabulary_json`).

---

## Performance Analysis

| Metric | Result |
|--------|--------|
| JSON validity | 100% (guaranteed by constrained decoding) |
| Function selection accuracy | ~92% on provided test cases |
| Argument extraction accuracy | ~90% overall |
| Processing speed | < 5 minutes for standard test suites on CPU |

The Qwen3-0.6B model, while small, benefits enormously from structural guidance. Without constrained decoding, JSON validity drops to ~30%. With it, every single output is parseable and schema-compliant — demonstrating that structural guidance can compensate for limited model capacity.

---

## Challenges Faced

**1. Token boundary mismatches**
JSON strings like `fn_add_numbers` may be tokenized as multiple subword tokens. The constraint engine must track partial token sequences and allow a token only if it can be a valid continuation of the expected string — not just a valid standalone token.

**2. Number tokenization**
Numbers like `265.5` are tokenized differently depending on context. Handling leading zeros, negative numbers, and floating-point notation required careful constraint logic.

**3. Ambiguous prompts**
Some prompts don't map clearly to a single function. The LLM-driven selection step handles these gracefully, but edge cases (e.g., prompts that fit multiple functions) required additional prompt engineering.

**4. Performance on CPU**
Running a 0.6B model token-by-token on CPU is slow. Batch pre-computation of token masks and caching vocabulary lookups significantly reduced processing time.

---

## Testing Strategy

- **Unit tests** were written for the constraint engine, covering: number generation, string generation, boolean generation, and function name selection.
- **Integration tests** verified end-to-end correctness on the provided `function_calling_tests.json` examples.
- **Edge cases tested**: empty strings, very large numbers, strings with special characters (`'`, `"`, `\n`), functions with multiple parameters, and ambiguous natural language phrasings.
- **JSON validation**: All output files were validated with Python's `json.loads()` and against the expected Pydantic schema after generation.

---

## Example Usage

```bash
# Default usage (reads from data/input/, writes to data/output/)
uv run python -m src

# Custom paths
uv run python -m src \
  --functions_definition data/input/functions_definition.json \
  --input data/input/function_calling_tests.json \
  --output data/output/function_calls.json
```

**Input prompt:**
```json
{ "prompt": "Reverse the string 'hello'" }
```

**Output:**
```json
{
  "prompt": "Reverse the string 'hello'",
  "name": "fn_reverse_string",
  "parameters": { "s": "hello" }
}
```

---

## Resources

- [Attention Is All You Need — Vaswani et al. (2017)](https://arxiv.org/abs/1706.03762) — Original Transformer paper
- [Outlines: Efficient Guided Generation — Willard & Louf (2023)](https://arxiv.org/abs/2307.09702) — Theoretical foundation for constrained decoding
- [Qwen3 Model Card — HuggingFace](https://huggingface.co/Qwen/Qwen3-0.6B) — Documentation for the base model used
- [Pydantic Documentation](https://docs.pydantic.dev/) — Data validation library used throughout the project
- [JSON Schema Specification](https://json-schema.org/) — Reference for schema-aware generation

### AI Usage

Claude (Anthropic) was used to assist with:
- Drafting and refining this README
- Debugging constraint logic edge cases (number and string tokenization)
- Suggesting Pydantic model structures for input/output validation

All core algorithmic work — the constrained decoding engine, the token mask computation, and the LLM interaction pipeline — was implemented manually without AI code generation.
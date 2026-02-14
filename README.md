# Addition Before Subversion

**Mathematical Reformulation Attacks on Large Language Models**

*Ephraiem Sarabamoun — University of Virginia*

This repository contains the code and data for a research project studying how mathematical reformulation can be used as an adversarial attack against LLM safety mechanisms. An uncensored LLM rephrases harmful prompts as ostensibly benign mathematics questions, which are then submitted to a safety-aligned target model. The technique exploits the privileged position of mathematical content in LLM training and deployment.

## Overview

The attack follows a two-stage pipeline:

1. **Reformulation Stage** — An uncensored model rephrases a harmful prompt as a mathematics question.
2. **Evaluation Stage** — A safety-aligned target model is queried with both the original and reformulated prompts, and the responses are compared.

The project evaluates this technique on **520 prompts** from the [AdvBench](https://github.com/llm-attacks/llm-attacks) harmful behaviors benchmark across two experimental tracks:

| Track | Attack Model | Target Model |
|---|---|---|
| Local (Open-Source) | Qwen3-32B-Uncensored (Q4_K_M) | gpt-oss:20b |
| API (Frontier) | Venice-Uncensored | GPT-5.1 |

## Repository Structure

```
mathematical-reframing-attacks/
├── main.py                  # Main entry point — orchestrates the attack pipeline
├── ollama_client.py         # Ollama API wrapper for local model inference
├── api_client.py            # OpenAI-compatible API wrapper for frontier models
├── primer_crafting.py       # Prompt reformulation via local uncensored model
├── api_primer_crafting.py   # Prompt reformulation via Venice AI API
├── benchmark_loader.py      # Fetches AdvBench harmful behaviors dataset
├── Pipfile                  # Python dependencies (Pipenv)
├── data/
│   ├── output.csv                  # Output template (overwritten on each run)
│   ├── output_api_final.csv        # Results: API track (520 prompts)
│   └── output_opensource_final.csv  # Results: Local track (520 prompts)
```

## Setup

### Prerequisites

- Python 3.13+
- [Pipenv](https://pipenv.pypa.io/)
- [Ollama](https://ollama.com/) (for local track only)

### Installation

```bash
git clone https://github.com/EphraiemSarabamoun/mathematical-reframing-attacks.git
cd mathematical-reframing-attacks
pipenv install
```

### Environment Variables

Create a `.env` file in the project root:

```
VENICE_API_KEY=<your-venice-api-key>
OPENAI_API_KEY=<your-openai-api-key>
```

These are only required for the API track.

### Ollama Models (Local Track)

Pull the required models:

```bash
ollama pull hf.co/mradermacher/Qwen3-32B-Uncensored-i1-GGUF:Q4_K_M
ollama pull gpt-oss:20b
```

## Usage

In `main.py`, set the `method` variable to choose the experimental track:

```python
method = "local"  # Open-source track (Ollama)
method = "api"    # Frontier track (Venice AI + OpenAI)
```

Then run:

```bash
pipenv run python main.py
```

Results are written incrementally to `data/output.csv`. Each row contains:

- **Local track:** `attack_prompt`, `thinking_no_priming`, `response_no_priming`, `modified_prompt`, `thinking_with_priming`, `response_with_priming`
- **API track:** `attack_prompt`, `response_no_priming`, `modified_prompt`, `response_with_priming`

## Key Findings

- **Baseline safety:** GPT-5.1 refused 516/520 original harmful prompts; gpt-oss:20b refused 517/520.
- **Mathematical reformulation** can selectively bypass safety mechanisms when the abstraction sufficiently separates harmful intent from mathematical form.
- **GPT-5.1** showed vulnerability through depth — producing comprehensive mathematical responses that implicitly addressed harmful content.
- **gpt-oss:20b** exhibited binary switching behavior — either complete refusal or full engagement, with no partial responses.
- Chain-of-thought analysis revealed safety recognition loops and policy citation patterns in the open-source model's reasoning.

## Ethical Considerations

This research is conducted under a responsible disclosure framework. The goal is to identify and characterize vulnerabilities in LLM safety mechanisms so that they can be addressed. All experiments use publicly available benchmarks and models.

## Citation

If you use this work, please cite:

```bibtex
@article{sarabamoun2026mathematical,
  title={Mathematical Reformulation Attacks on Large Language Models},
  author={Sarabamoun, Ephraiem},
  year={2026}
}
```

## License

This project is for research purposes.

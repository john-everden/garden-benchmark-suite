# Garden Benchmark Suite

This repository provides a standardized evaluation framework for testing structured AI interaction against baseline prompting.

Goal:
Measure whether structured interaction improves reliability, coherence, and constraint adherence without changing the base model.

## Experimental Conditions

Condition A: Standard prompting  
Condition B: Structured interaction

Same model, same parameters, same prompts.

## What This Evaluates

- Knowledge accuracy
- Truthfulness under pressure
- Multi-turn constraint retention
- Long-context recall
- Refusal quality
- Planning under constraints
- Calibration and stability
- Robustness under adversarial instructions

## How To Run

1. Choose a model
2. Run prompts in `/PROMPTS/TEST_SUITE_{VERSION}`
3. Record results using `/TEMPLATES/RUN.md`
4. Publish results in `/RUNS/{MODEL_NAME}{VERSION}{TEST-SUITE}.md`
5. Run Score Runs.py


## Scientific Position

This benchmark evaluates interaction structure, not base model intelligence.

## License

Open evaluation framework for public research use.

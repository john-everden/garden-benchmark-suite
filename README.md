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
2. Run prompts in `/prompts/dataset_v1.md`
3. Record results using `/templates/results_template.md`
4. Publish results in `/runs/`
5. Compare using `/analysis/results_table_template.md`

## Scientific Position

This benchmark evaluates interaction structure, not base model intelligence.

## License

Open evaluation framework for public research use.

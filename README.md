# Basketball Shot Probability Analysis

**Feras Elghandour** · Technical case study

Estimate shot-making and conditional probabilities, then show precisely which independence assumptions are needed for a binomial projection.

## Implementation

A reusable standard-library probability module with binomial mass, conditional probability, and expected-points comparisons. The original aggregate analysis is included as a machine-readable result record.

```mermaid
flowchart LR
    A[Observations] --> B[Validated counts or measurements]
    B --> C[Statistical calculations]
    C --> D[Interpretable JSON results]
```

## Results

The retained study contains 1,434 attempts and 703 makes (49.02%). Two-point shots make 57.72% (374/648), and three-point shots make 41.86% (329/786). Expected points per attempt are therefore about 1.154 and 1.256 respectively, before accounting for context or sampling uncertainty.

The retained aggregates are in [results/aggregate_counts.json](results/aggregate_counts.json). The Python implementation is an improved reusable version of the calculations; historical aggregates and fresh behavior tests have separate scopes.

## Reproduce

Python 3.11 or later; no third-party packages are required.

```sh
python probability.py
python -m unittest discover -s tests -v
```

## Practical relevance and limits

Shots may be dependent and differ in difficulty, player mix, and game context. The expected-points comparison is descriptive and does not prove that choosing a three-pointer improves a team’s outcome.

Raw observations and classroom slide materials are not included. For new analyses, provide your own authorized counts or CSV. No client deployment or commercial result is claimed.

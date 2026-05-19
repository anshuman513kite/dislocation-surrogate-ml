# Dislocation Surrogate ML

Physics-informed surrogate modeling workflow for dislocation dynamics using legacy molecular dynamics simulations and Python-based ML pipelines.

---

## Workflow Backbone

NEB → Extended System → MD → Defect Tracking → lmoy → Python → ML

---

## Objective

Build a reusable workflow connecting:

- atomistic simulations
- defect dynamics
- scientific computing
- surrogate machine learning

---

## Version 1 Goals

- Reuse legacy MD simulation outputs
- Extract lmoy-based displacement data
- Generate structured datasets
- Build a minimal surrogate model
- Demonstrate physics-to-ML workflow integration

---

## Current Status

Current work focuses on:
- reconstructing legacy MD workflows
- organizing simulation outputs
- building Python extraction pipelines
- preparing ML-ready datasets

---

## Long-Term Direction

Future versions may include:
- automated feature extraction
- velocity and kink statistics
- active learning workflows
- ML-guided simulation selection
- Python-native simulation orchestration

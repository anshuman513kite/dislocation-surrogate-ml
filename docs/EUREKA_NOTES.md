# Eureka Notes - internal scientific roadmap documentation

## Core Workflow

NEB → Extended System → MD → Defect Tracking → lmoy → Python → ML

---

## Main Idea

Reuse legacy atomistic simulation workflows and connect them with modern Python-based surrogate modeling pipelines.

---

## Initial Surrogate Inputs

- Stress
- Temperature
- Potential type
- Extension size

---

## Initial Surrogate Output

- Average dislocation displacement extracted from lmoy files

---

## Immediate Goal

Build a Python pipeline that:
1. reads lmoy files
2. extracts displacement values
3. generates structured datasets
4. enables surrogate ML experiments

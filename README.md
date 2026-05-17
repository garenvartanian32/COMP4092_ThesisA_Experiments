# AI vs Human Code Maintainability Analysis

This repository contains the experimental code and data structure used for a thesis project investigating the maintainability of AI-generated code compared to human-written code.

The project uses Python static analysis tools to extract maintainability-related software metrics from different code sources. The main metrics considered include Maintainability Index, Cyclomatic Complexity, Lines of Code, and Halstead metrics.

## Experiments

### Experiment 1: Edabit Problem Comparison

The first experiment uses selected Python programming problems from Edabit across different difficulty levels. For each problem, a human-written solution is compared with AI-generated solutions from:

- ChatGPT
- GitHub Copilot
- Claude

The purpose of this experiment is to create a controlled comparison where each code source attempts the same programming problems. This allows maintainability metrics to be compared by both code source and task difficulty.

### Experiment 2: Dataset-Based Analysis

The second experiment applies the same static analysis process to larger existing datasets. The datasets used include:

- CodeSearchNet
- HumanVsAI
- Human vs AI Code Quality

This experiment provides a broader dataset-level comparison of maintainability-related metrics across larger collections of human-written and AI-generated code.

## Static Analysis Tools

The analysis uses:

- **Radon** for Maintainability Index, Cyclomatic Complexity, Lines of Code, and Halstead metrics.
- **Lizard** for additional complexity and structural metrics such as function count, token count, and parameter count.

## Output

The scripts process Python files and export the metric results into CSV files. These CSV files are then used to create tables and graphs for comparing maintainability across code source, dataset, and difficulty level.

## Purpose

The purpose of this repository is to support a metric-based comparison of whether AI tools or humans produce more maintainable Python code.

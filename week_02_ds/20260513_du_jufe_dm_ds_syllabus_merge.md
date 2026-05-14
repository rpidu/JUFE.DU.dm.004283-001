# Python Data Science Crash Course (5 Days)

## Executive Summary
This condensed syllabus provides a beginner-friendly yet rigorous introduction to Python for data science over 5 days. It focuses on:
- Data wrangling and pipelining
- Statistical analysis
- Visualisation

All resources are **free and online**, with priority given to concise explanations and practical examples.

---

## Prioritised Learning Resources & Syllabus

### 1. Python Basics for Data Science (Day 1)
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
  - Focus: Sections 3–5 (control flow, data structures)
- [Automate the Boring Stuff (Ch. 1–6)](https://automatetheboringstuff.com/)
  - Practical scripting mindset

**Key Topics**
- Variables, types
- Lists, dictionaries
- Functions
- File I/O

---

### 2. Data Wrangling & Pipelining (Day 2–3)
- [pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
- [Python Data Science Handbook (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/)
  - Data Wrangling Section (Ch. 3)

**Page References**
- Data Wrangling: Ch. 3 (pandas basics, indexing, cleaning)

**Key Topics**
- DataFrames
- Missing data handling
- Filtering, grouping
- Pipeline-style transformations

---

### 3. Statistical Analysis (Day 4)
- [Think Stats (Allen B. Downey)](https://greenteapress.com/wp/think-stats-2e/)
- SciPy/NumPy Docs: https://numpy.org/doc/

**Page References**
- Analysis: Think Stats Ch. 2–4

**Key Topics**
- Descriptive statistics
- Probability basics
- Hypothesis thinking

---

### 4. Data Visualisation (Day 5)
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- Python Data Science Handbook – Visualization (Ch. 4)

**Page References**
- Visualization: Ch. 4

**Key Topics**
- Line plots, histograms
- Scatter plots
- Basic dashboards

---

## Minimal Code Examples

### Data Wrangling Example
```python
import pandas as pd

df = pd.read_csv('data.csv')
df = df.dropna()
df = df.groupby('category').mean()
```

### Statistical Analysis Example
```python
import numpy as np

mean = np.mean(df['value'])
std = np.std(df['value'])
```

### Visualisation Example
```python
import matplotlib.pyplot as plt

plt.hist(df['value'])
plt.show()
```

---

## Suggested 5-Day Plan

| Day | Focus | Outcome |
|-----|------|--------|
| 1 | Python basics | Understand syntax & data types |
| 2 | Pandas intro | Load & inspect data |
| 3 | Data wrangling | Clean & transform datasets |
| 4 | Statistics | Analyse data quantitatively |
| 5 | Visualisation | Communicate insights |

---


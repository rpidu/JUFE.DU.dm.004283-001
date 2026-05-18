# Python Data Science Crash Course (5 Days)

**TODO:** The main fixes for this syllabus are;

- Missing data handling
- Data quality metrics

## Executive Summary

This 5-day crash course introduces beginners to Python for data science - using high-quality free resources it focuses on,

- Data wrangling and pipelining
- Statistical analysis
- Visualisation

All resources are **free and online**, with priority given to concise explanations and practical examples.

Categorised sources:

- [Think Stats (Allen B. Downey)](https://greenteapress.com/wp/think-stats-2e/)
- Python
  - [Python Official Tutorial](https://docs.python.org/3/tutorial/)
  - alternatively; [Automate the Boring Stuff (Ch. 1–6)](https://automatetheboringstuff.com/)
  - [Python Data Science Handbook (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/)
    - [Aggregation and grouping](https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html)
  - [Python for Data Analysis](https://wesmckinney.com/book/)
  - https://seaborn.pydata.org/tutorial.html
- Libraries
  - Pandas
    - https://pandas.pydata.org/docs/user_guide/index.html
      - [pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
      - [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
    - [Python for Data Analysis, Pandas Basics](https://wesmckinney.com/book/pandas-basics.html)
  - [NumPy](https://numpy.org/doc/)
  - [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
  - [JSON with python](https://docs.python.org/3/library/json.html)

---

## Prioritised Syllabus, with resources

| Day | Focus          | Outcome                        |
| --- | -------------- | ------------------------------ |
| 1   | Python basics  | Understand syntax & data types |
| 2   | Pandas intro   | Load & inspect data            |
| 3   | Data wrangling | Clean & transform datasets     |
| 4   | Statistics     | Analyse data quantitatively    |
| 5   | Visualisation  | Communicate insights           |

### 1. Python Basics for Data Science (Day 1)

- Variables and types
- Lists, dictionaries
- Functions and control flow
- File I/O

📘 Focus pages:

- [Python Official Tutorial](https://docs.python.org/3/tutorial/)
  - Sections 3–5 (control flow, data structures)
  - Functions & control flow: Sections 4–6
- [Automate the Boring Stuff (Ch. 1–6)](https://automatetheboringstuff.com/)
  - Practical scripting mindset, alternative to the official tutorial

---

### 2. Data Wrangling & Pipelining (Day 2–3)

- Reading CSV
- Cleaning data, filtering
- DataFrames
- Transformations and grouping
  - Pipeline-style transformations
  - **TODO:** Missing data handling
- Writing and reading JSON

References:

- [Python Data Science Handbook (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/)
  - Data Wrangling Section (Ch. 3)
- [JSON with python](https://docs.python.org/3/library/json.html)
- Pandas
  - https://pandas.pydata.org/docs/user_guide/index.html
    - [pandas Getting Started](https://pandas.pydata.org/docs/getting_started/index.html)
    - [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
  - [Python for Data Analysis, Pandas Basics](https://wesmckinney.com/book/pandas-basics.html)

📘 Pages:

- Data cleaning: Chapter 7 (McKinney)
- Data Wrangling: Ch. 3 (pandas basics, indexing, cleaning)
- Transformation: Pandas user guide section "GroupBy"

---

### 3. Statistical Analysis (Day 4)

- TODO: verify the relevance of this structuring of the concepts
- Descriptive statistics
- Probability basics
  - Correlation
  - Aggregation
- Hypothesis thinking
  - TODO: this should actually focus some metric on data quality
- Numpy (TODO: what core parts of numpy is relevant)

References:

- https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html
- [Think Stats (Allen B. Downey)](https://greenteapress.com/wp/think-stats-2e/)
- SciPy/NumPy Docs: https://numpy.org/doc/

📘 Pages:

- Aggregation & grouping: Python Data Science Handbook, Chapter 3.8
- Analysis: Think Stats Ch. 2–4

---

### 4. Visualisation (Day 5)

- Line plots
- Scatter plots
- Histograms
- Basic dashboards

References:

- https://matplotlib.org/stable/tutorials/index.html
- https://seaborn.pydata.org/tutorial.html
- [Matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Python Data Science Handbook (Jake VanderPlas)](https://jakevdp.github.io/PythonDataScienceHandbook/)

📘 Pages:

- Matplotlib intro tutorials
- Seaborn relational plots
- Visualization: Python Data Science Handbook, Ch. 4

---

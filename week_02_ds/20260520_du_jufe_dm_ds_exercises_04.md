# Lecture 0204, exercise; Data Exploration

Task: Analyse the cleaned dataset, exploring its key characteristics, by aggregation and other means.

---

## Overview

The task is to build a small script that helps you understand the data you have cleaned, with focus on measures on data completeness, using the same pluggable pipeline pattern as used previously in the course.

## Challenges

Todays exercises is split into four incremental challenges that build on each other. As previous exercise, this exercise builds heavily on AI use; you are to discuss and work through examples together with AI, asking AI to explain and find sources for the material, and execute parts of the challenges. Keep in mind though, that you need to keep meticulous track of your work, in order to discuss the end result and process to it, in the documentation part of the challenges.

This work is **student work**, and go into the **student repository**.

### 1. Aggregating Data

The data should now be aggregated, implemented this feature as a processing function, identifying key statistics of the data previously cleaned.

- Use the same style of data processing script developed in **exercises 0201-03**
- The data aggregation artifact should be fully implemented in the processing function
- Process cleaned data from CLI
- Document how your code should be called from CLI, and expected output, in your `README.md`

The aggregation in you implementation should;

- Measure key characteristics of the data with regard to your data model, or data quality, ex.;
  - statistical parameters relevant, for the selected distribution(s)
  - level of errors in the data, and
  - measures on data outliers

Your system should also be extended with the capacity to report metadata of aggregates in `.json` format.

Approach the problem by;

- Discussing the design of the relevant aggregation(s) with AI
- Motivating the aggregate(s) connection to your experiment design
- Locating relevant documentation in peer reviewed journals, as also previously done in **exercises 0202-03**
- Implementing the aggregation(s) using AI, and your specification of the design,
  - as a plugin to your already extant pipeline architecture; ie. a processing function
  - adding capacity in your backend to read JSON files.

Example minimalistic aggregation artifact, measuring a mean;

```python
import pandas as pd

df = pd.read_csv('data.csv')
df = df.dropna()
df = df.groupby('category').mean()
```

References:

- [Python for Data Analysis, McKinney; Ch. 10, Aggregation](https://wesmckinney.com/book/data-aggregation)
- Aggregation & grouping: Python Data Science Handbook, Chapter 3.8
  - https://jakevdp.github.io/PythonDataScienceHandbook/03.08-aggregation-and-grouping.html
- [Think Stats (Allen B. Downey)](https://greenteapress.com/wp/think-stats-2e/)
  - Analysis: Think Stats Ch. 2–4
- SciPy/NumPy Docs: https://numpy.org/doc/
- [JSON with python](https://docs.python.org/3/library/json.html)

### 2. Data Normalisation

The data should now be normalised, implementing it as a processing function, readying the data for training statistical models.

Working as you have done in previous exercise,

- Discuss and arrive upon a design for a normalisation methodology suitable for your data
  - why is it important to normalise the data?
  - how will outliers affect any models trained with the data, after and before normalisation?
- Document the design with applicable peer reviewed journal papers
- Implement it as a pluggable filter within your pipeline architecture
- Document its application to your data

### 3. Exploring Completeness

> **NOTE:** it is allowed to skip this part of the exercise, moving on to the _visualisation_ exercise **0205** instead.

Do correlation analysis - and/or apply measures of information content, or completeness - exploring and reasoning about how large coverage, of the full population, your cleaned and normalised dataset has.

> **TIP:** discuss measures from _information theory_ with AI, and measures on how normalised the data is - reason with AI why (and if) normalisation measures is relevant to measure completeness.

Use the same approach as in all the other challenges in this exercise.

### 4. Document the Exploration

Document the exercise the same way that you documented the results from **exercises 0202-03**.

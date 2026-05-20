# Lecuture 0203, exercise; Filtering Generated Data

Task: Load prevously generated CSV and clean missing values.

---

## Overview

The task is to build a small script filtering a previously generated set of data, which contains malformed or missing data, using and extending the previously introduced **Backend-Model-Process** and object-oriented architectural pattern.

## Challenges

Todays exercises is split into 3 incremental challenges to get you started. Begin with the first, continuing through the rest as you go. This exercise builds heavily on AI use; you are to discuss and work through examples together with AI, asking AI to explain and find sources for the material.

This work is **student work**, and go into the **student repository**.

### 1. Filtering Data

The data should now be filtered, using a simple data filter implemented as a processing function, filtering the data contained in the data file you generated above.

- Use the same style of data processing script developed in **exercises 0201-02**; a
  - Backend-Model-Process, with
  - IPO for process function and
  - CLI entrypoint with argparse
- The data filtering artifact should be fully implemented in the processing function
- Process generated data from CLI
- Document how your code should be called from CLI, and expected output, in your `README.md`

The filter you implement should;

- Drop all detected
  - malformed, or
  - Missing data

Approach the problem by;

- Discussing the design of the filters detection mechanism with AI
- Identifying the main motivation to the selected mechanism with regard to your experiment design
- Locating relevant documentation in peer reviewed journals, as previously done in **exercise 0202**
- Implementing the design using AI, and your specification of the design,¨
  - keeping the filtering function, or subsystem, as a pluggable component in your pipeline architecture

Example minimalistic filtering artifact, targeting missing data;

```python
import pandas as pd

df = pd.read_csv("data.csv")
df = df.dropna()
```

Reference:

- https://pandas.pydata.org/docs/user_guide/10min.html
- [Python for Data Analysis, Pandas Basics](https://wesmckinney.com/book/pandas-basics.html)
  - Data cleaning: Chapter 7 (McKinney)

### 2. Completing Missing Data

Update your previous script by adding the ability to complete any missing data, using a relevant heuristic; ie. a "rule of thumb".

Approach the problem by;

- Discussing the design of the heuristics detection mechanism with AI
- Identifying the main motivation to the selected mechanism with regard to your experiment design
- Locating relevant documentation in peer reviewed journals, as also done in previously previous challenge
- Implementing the design using AI, and your specification of the design,
  - extending your pipeline architecture with this filter, as a plugin that can replace
  - whilst retaining the previous filter as an option

### 3. Imputing Missing Data

Update your previous script by adding the ability to impute missing data, inferring from the subset of the data that is complete - in the senste that it contains no data errors.

Approach the problem similarly as done in the previous challenge; keeping in mind to keep all implemented filters available as plugins, in the resulting solution.

### 4. Document the filter

Document the exercise the same way that you documented the results from **exercise 0202**.

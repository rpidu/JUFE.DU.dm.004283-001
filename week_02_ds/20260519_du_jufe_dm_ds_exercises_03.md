# Lecture 0203, exercise; Filtering Generated Data

Task: extend architecture with plugins - to load previously generated CSV, cleaning missing or erronous values, writing results to JSON.

---

## Overview

The task is to extend the pipeline architecture with filtering capcity to process the previously generated set of data, which contains malformed or missing data, rendering clean data in JSON format.

## Challenges

Todays exercises is split into four incremental challenges that build on each other. As previous exercise, this exercise builds heavily on AI use; you are to discuss and work through examples together with AI, asking AI to explain and find sources for the material, and execute parts of the challenges. Keep in mind though, that you need to keep meticulous track of your work, in order to discuss the end result and process to it, in the documentation part of the challenges.

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
  - missing data
- Wrangle, ie. reshape the data if nescessary

Your implementation should output the data into **JSON format**, extending your architecture with another file backend for JSON.

Approach the problem by;

- Discussing the design of the filters detection mechanism with AI
- Identifying the main motivation to the selected mechanism with regard to your experiment design
- Locating relevant documentation in peer reviewed journals, as previously done in **exercise 0202**
- Implementing the mechanism using AI, and your specification of the design,
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
  - Data Wrangling: Chapter 8 (McKinney)
- [JSON with python](https://docs.python.org/3/library/json.html)

### 2. Completing Missing Data

Update your previous script by adding the ability to complete any missing data, using a relevant heuristic; ie. a "rule of thumb".

Approach the problem by;

- Discussing the design of the heuristic data completion mechanism with AI
- Identifying the main motivation to the selected mechanism with regard to your experiment design
- Locating relevant documentation in peer reviewed journals, as also done in previously previous challenge
- Implementing the heuristics using AI, and your specification of the design,
  - extending your pipeline architecture with this filter, as a plugin function just as before
  - whilst retaining the previous filter as an option
  - using the JSON backend to write the data

### 3. Imputing Missing Data

Update your previous script by adding the ability to impute missing data, inferring from the subset of the data that is complete - ie. the part of the data that contain no errors.

Approach the problem similarly as done in the previous challenge; keeping in mind to keep all implemented filters available as plugins, in the resulting solution.

### 4. Document the filters

Document the exercise the same way that you documented the results from **exercise 0202**;

- Document your discussion with AI, as well as your understanding of the resulting filters and architecture;
  - provide at most one paragraph each, detailing why the filter design is applicable for the experiment, and your understanding of their implementation - for all of,
    - dropping,
    - heuristic, and
    - imputing filters.
  - Summarise the filter implementations with one paragraph, as in **exercise 0202**.

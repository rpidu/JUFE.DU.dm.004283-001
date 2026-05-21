# Lecuture 0205, exercise; Data Visualisation

Task: Visualise the history of the dataset, from generated to clean and normalised data - together with aggregates, model approximations and other measures.

---

## Overview

The task is to build a small script that renders the data you have cleaned, with focus on measures on data quality, using the same pluggable pipeline pattern as used previously in the course.

## Challenges

Todays exercises is split into four incremental challenges that build on each other. As previous exercise, this exercise builds heavily on AI use; you are to discuss and work through examples together with AI, asking AI to explain and find sources for the material, and execute parts of the challenges. Keep in mind though, that you need to keep meticulous track of your work, in order to discuss the end result and process to it, in the documentation part of the challenges.

This work is **student work**, and go into the **student repository**.

### 1. Dataset History

The data should now be visualised, by implementing a plotting feature as a pluggable processing function, capable of plotting any of the dataset versions; from generated to clean, fully imputed and normalised data.

Use the same approach as in all the challenges in prevoius **exercise 0204**, focusing

- How to plot and visually compare the different versions of the dataset;
  - generated,
  - filtered,
  - completed,
  - imputed and
  - normalised data

Example plotting of a histogram:

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
plt.hist(df['value'])
plt.show()
```

Reference:
https://matplotlib.org/stable/tutorials/index.html

### 2. Aggregates and Data

Extend the visualisation capacity of your data pipeline system, by adding a plotting plugin that indicate aggregate information in the visualisation, when plotting a select dataset.

Use the same approach as previously, remembering to use the `.json` metadata from previous exercise.

### 3. Information and Population

> **NOTE:** if you have not performed any of the correlation or completeness quality discussions with AI from **exercise 0204**, you cannot do this part of this exercise.

Add capacity visualise data completeness, a correlation analysis information and/or information theoretic measures, to illustrate data sample completeness with respect to the expected background data population; your choice of visualisations here depends on what you implemented in the _"Exploring Completeness"_ challenge in **exercise 0204**.

### 4. Document the Exploration

Document the exercise the same way that you documented the results from **exercises 0202-04**; focusing what you have learnt from plotting the data.

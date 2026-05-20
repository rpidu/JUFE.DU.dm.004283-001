# Lecuture 0205, exercise; Data Visualisation

Task: Visualise the history of the dataset, from generated to clean data - together with aggregates, model approximations and other measures.

---

## Overview

The task is to build a small script that renders the data you have cleaned, with focus on measures on data completeness, using the same pluggable pipeline pattern as used previously in the course.

## Challenges

Todays exercises is split into 3 incremental challenges that build on each other. As previous exercise, this exercise builds heavily on AI use; you are to discuss and work through examples together with AI, asking AI to explain and find sources for the material, and execute parts of the challenges. Keep in mind though, that you need to keep meticulous track of your work, in order to discuss the end result and process to it, in the documentation part of the challenges.

This work is **student work**, and go into the **student repository**.

### 1. Visualise dataset history

The data should now be visualised, implemented this feature as a processing function, capable of plotting any of the uncleaned generated dataset, through to the fully imputed and normalised data.

Use the same approach as in all the challenges in prevoius **exercise 0204**, focusing

- How to plot and visually compare the different versions of the dataset;
  - generated,
  - filtered,
  - completed,
  - imputed and
  - normalised data

Example plotting of histogram:

```python
import matplotlib.pyplot as plt

plt.hist(df['value'])
plt.show()
```

Reference:
https://matplotlib.org/stable/tutorials/index.html

### 2. Visualise aggregates with data

Extend the visualisation series, by adding a plotting plugin that adds aggregates to the visualisation, to any of the plotted datasets.

Use the same approach as previously, remembering to use the `.json` metadata from previous exercise.

### 3. Visualise information measures and population

Add capacity visualise data completeness, correlation analysis information and information theoretic measures, to illustrate data sample completeness with respect to the expected background data population.

### 4. Document the Exploration

Document the exercise the same way that you documented the results from **exercises 0202-03**.

# Lecuture 0202, exercise; Generating and Filtering Data

TODO: extend all days with challenges

Task: Load CSV and clean missing values.

---

## Overview

The task is to build a small script filtering and completing a generated set of data, which contains malformed or missing data, using and extending the previously introduced **Backend-Model-Process** and object-oriented architectural pattern.

## Challenges

Todays exercises is split into 4 incremental challenges to get you started. Begin with the first, continuing through the rest as you go. This exercise builds heavily on AI use; you are to discuss and work through examples together with AI, asking AI to explain and find sources for the material - and also generate both data and small challenges for you along the key concepts provided.

This work is **student work**, and go into the **student repository**.

### 1. Generate Data

Begin by discussing the research stories into experiment design;

- Use the Research Stories (RS) you created in exercise 0101 (see `20260512_du_jufe_dm_asm_01_exercise.md`)
- Discuss your RS together with AI, generating hypotheses and experiment design as you did in exercise 0105 (see `20260515_du_jufe_dm_asm_05_exercise.md`)
- Using the experiment design that you arrived upon with AI in the previous step; design a data collection method that would test your hypotheses

Then continue to work on how to design the generator;

- Discuss how a minimalistic data generator could be designed to generate data samples from such a data collection method; discussing in particular
  - how to focus a subspace of the problems full dimensionality, for
    - simple proof-of-concept of the experiment design
  - from what statistical distribution the samples should be drawn
  - how you should format the samples in a CSV file
  - how to simulate input or collection errors in the data
  - how to simulate other missing data
- Find high quality peer reviewed scholarly articles,
  - covering the key concepts in your discussion of the generator, with
  - one article for each of such concepts

After arriving at the generator design, implement it using AI - generating the data;

- Implement the data generator,
  - with a minimalistic, less-is-more, approach
  - using the **Backend-Model-Process** architcture
  - as a CLI script using python argparse and the `__name__ == "__main__"` entrypoint
- Generate the data
  - The resulting data should be in CSV file format
  - It should contain some
    - missing data, and
    - malformed or false data
  - Document the process in your repository, extending ex. `README.md`

Then document how you have worked together with AI, and what results you arrived at;

- Document your discussion with AI, and your understanding of the resulting model
  - provide at most one paragraph each, detailing all of;
    - the target experiment, the
    - the design of the generator,
    - why the design is applicable for the experiment, and
    - the implemented generator and quality of the data.
  - Summarise the whole generator exercise in one paragraph, which
    - begins with one sentence that summarise the whole paragraf.

### 2. Filtering Data

The data should now be filtered, using a simple data filter implemented as a processing function, filtering the data contained in the data file you generated above.

- Use the same style of data processing script developed in **exercises 0201**; a
  - Backend-Model-Process, with
  - IPO for process function and
  - CLI entrypoint with argparse
- The data filtering artifact should be fully implemented in the processing function
- Process generated data from CLI
- Document how your code should be called from CLI, and expected output, in your `README.md`

Example minimalistic filtering artifact, targeting missing data;

```python
import pandas as pd

df = pd.read_csv("data.csv")
df = df.dropna()
```

Reference:
https://pandas.pydata.org/docs/user_guide/10min.html

### 3. Completing Missing Data

### 4. Imputing Missing Data

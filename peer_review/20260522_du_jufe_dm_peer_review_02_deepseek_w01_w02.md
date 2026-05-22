Based on the files you provided, the peer review document, the syllabus, and the five exercises for week 2, I have extracted the learning targets. The targets are organized according to the definitions in your `peer_review.md` file.

Below is a structured summary of the 10 most prominent learning targets for **Concepts & Challenges** (combined into review questions) and the 10 most important **Artifacts**, formatted for download.

---

# Week 1 & 2 Learning Targets Summary

**Course:** JUFE HDa - Data Management (004283-001)
**Focus:** Core principles (Week 1) & Python Data Science Crash Course (Week 2)

## Part 1: Key Concepts & Challenges (Peer Review Questions)

_These 10 items combine key concepts and challenges. A peer would query the respondent on these topics to verify understanding._

**1. The Scientific Method & The Collegium**

- **Question to Respondent:** Explain the role of peer review in verifying scientific value, principles, and factfulness within a scientific collegium, as described in the course definition.

**2. Input-Process-Output (IPO) Model**

- **Question to Respondent:** Demonstrate your understanding of the IPO model by explaining how a Python script can read data from a CLI (Input), process it with a function (Process), and print a result (Output).

**3. Backend-Model-Process Architectural Pattern**

- **Question to Respondent:** Describe the separation of concerns in the Backend-Model-Process pattern and why it is beneficial for building a data processing pipeline.

**4. Experiment Design & Hypothesis Generation**

- **Question to Respondent:** Explain the process of using a Research Story (RS) to generate a testable hypothesis and designing a data collection method to test that hypothesis.

**5. Statistical Distribution for Data Simulation**

- **Question to Respondent:** Justify your choice of a specific statistical distribution (e.g., uniform, normal) for generating synthetic data in your experiment simulation.

**6. Data Quality: Malformed & Missing Data**

- **Question to Respondent:** Discuss the difference between simulating "malformed/false data" and "missing data" in a generator, and explain why both are important for testing a pipeline.

**7. Data Wrangling & Filtering**

- **Question to Respondent:** Explain the purpose of a "pluggable filter" in a data pipeline, contrasting strategies for dropping erroneous data vs. imputing missing values.

**8. Data Aggregation & Key Statistics**

- **Question to Respondent:** Describe how aggregation functions (e.g., `groupby()`, `mean()`) are used to explore key characteristics of a cleaned dataset and measure data completeness.

**9. Data Normalisation & Outlier Impact**

- **Question to Respondent:** Argue why normalisation is an important preprocessing step before training statistical models, specifically addressing how outliers can skew results.

**10. Dataset History & Visual Comparison**

- **Question to Respondent:** Explain how visualising different versions of a dataset (raw, filtered, imputed, normalised) helps in understanding the impact of each step in your pipeline.

---

## Part 2: Key Artifacts (Peer Review Instructions)

_These 10 items are key artifacts. The peer review document instructs the reviewer on what to look for in the respondent's repository or group work._

**1. Data Generation Script (`generate_data.py`)**

- **Review Instruction:** Verify the existence of a CLI script that generates a CSV file simulating an experiment, containing both true data and injected errors (malformed/missing), based on an experiment design documented in the `README.md`.

**2. Raw Generated Dataset (`data.csv`)**

- **Review Instruction:** Check the repository for a `data.csv` file (or similar) produced by the generation script, confirming it has a substantial number of rows (e.g., 10,000) and contains the simulated data errors as specified in the exercise.

**3. Filtering/Imputing Script (`process_data.py`)**

- **Review Instruction:** Locate the Python script that loads the generated CSV, applies a plugin-based filter (drop, heuristic completion, or imputation), and saves the cleaned output to a JSON file.

**4. Cleaned & Imputed Dataset (`.json`)**

- **Review Instruction:** Find the JSON output file resulting from the filtering/imputing process. Verify that the data structure is valid JSON and that missing/malformed values have been addressed according to one of the implemented methods.

**5. Data Exploration Script (`explore_data.py`)**

- **Review Instruction:** Identify the script that reads the cleaned JSON data, performs aggregation (e.g., calculating mean, standard deviation), and reports key statistics as metadata, likely in a separate `.json` file.

**6. Aggregation Metadata File (`aggregates.json`)**

- **Review Instruction:** Check for a metadata file (e.g., `aggregates.json`) that contains the results of the data exploration, such as statistical parameters, error levels, or outlier measures.

**7. Data Visualisation Script (`visualise_data.py`)**

- **Review Instruction:** Locate the script capable of generating plots (e.g., histograms, scatter plots) for any version of the dataset (raw, cleaned, normalised) using matplotlib.

**8. Visualisation Output (e.g., `.png` files)**

- **Review Instruction:** Look for saved plot images (e.g., `history_plot.png`, `aggregate_plot.png`) in the repository that visually compare different stages of the data pipeline or illustrate aggregate information.

**9. Updated `README.md` with CLI Documentation**

- **Review Instruction:** Verify that the `README.md` has been substantially updated to include clear, step-by-step instructions on how to run each script (generate, process, explore, visualise) from the CLI, including expected arguments and output.

**10. Documentation of AI Collaboration**

- **Review Instruction:** In the `README.md` or a separate document, confirm the presence of a summary paragraph (as requested in exercise 0202) that details the discussion with AI, the final generator/filter design, and a one-sentence summary of the entire exercise.

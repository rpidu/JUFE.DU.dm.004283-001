Based on the files you provided and the GitHub repository structure for **Week 2** (The script - data and file formats), I have extracted the learning targets. The review focuses exclusively on the 5 exercises from Week 2 (`exercises_01` through `05`), aligning with the course's main objectives of building a Python data pipeline.

Below is the summary and listing of the **10 most prominent learning targets** (concepts & challenges) and the **10 most important artifacts**, formatted for peer review.

---

### Week 2 Peer Review Summary

**Focus:** Data Pipeline, Scripting, and File Formats (CSV/JSON)
**Method:** Peers verify understanding (Concepts/Challenges) and repository presence (Artifacts) against the specifications in `exercises_01` to `05`.

---

### Part 1: Peer Review Questions (Concepts & Challenges)

_For each target, the peer will query the respondent student. A score of `+` indicates the student demonstrates understanding and has met the challenge._

| #   | Target Type   | Learning Target (One-line statement)                                                                                                                          | Peer Review Question                                                                                                                                |
| :-- | :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Concept**   | **IPO Model**: The fundamental structure of a script using Input, Process, Output.                                                                            | "Explain the IPO model and show where Input, Process, and Output occur in your Week 2 script."                                                      |
| 2   | **Concept**   | **Backend-Model-Process Pattern**: An OOP architecture separating file handling (backend), core logic (model), and execution (process).                       | "Describe the roles of the Backend, Model, and Process components in your OOP refactoring from Exercise 01."                                        |
| 3   | **Concept**   | **Data Generation & Simulation**: Creating synthetic data, including intentional errors or missing values, to mimic real-world collection.                    | "What statistical distribution did you use in your generator (Ex. 02) and why? How did you simulate data errors?"                                   |
| 4   | **Concept**   | **Data Wrangling**: The process of cleaning, transforming, and reshaping raw data (e.g., dropping malformed rows).                                            | "What specific criteria did your 'drop' filter (Ex. 03) use to detect malformed data? Why was this choice appropriate for your experiment?"         |
| 5   | **Concept**   | **Data Imputation vs. Completion**: The difference between filling missing data with a heuristic (e.g., mean) versus inferring it from complete data subsets. | "Explain the difference between the 'completion' heuristic and the 'imputation' method you implemented. When would you use one over the other?"     |
| 6   | **Concept**   | **Data Normalisation**: Scaling data to a standard range (e.g., 0-1) to prepare it for statistical models.                                                    | "Why is normalising your data important before training a model? How would outliers affect your raw vs. normalised data?"                           |
| 7   | **Challenge** | **CLI Pipeline with `argparse`**: Building a script that accepts arguments from the command line for flexible operation.                                      | "Demonstrate how to call your analysis script (Ex. 04) from the CLI to produce a JSON report. What arguments does it accept?"                       |
| 8   | **Challenge** | **Pluggable Processing Functions**: Designing the `process` function to accept different plugins (e.g., `drop`, `impute`, `normalise`).                       | "Show how your architecture allows you to 'plug in' a new filter like 'normalise' without changing the core Model or Backend."                      |
| 9   | **Challenge** | **Data Aggregation & Statistics**: Calculating key metrics (mean, outliers, completeness) from a cleaned dataset.                                             | "What key statistics did your aggregation function (Ex. 04, #1) report? What did these tell you about your data's quality?"                         |
| 10  | **Challenge** | **Visualising Dataset History**: Plotting different versions of the data (raw, filtered, imputed, normalised) for comparison.                                 | "Show the plot that compares your generated data to your cleaned data. What does this visual comparison tell you about the impact of your filters?" |

---

### Part 2: Artifact Review Instructions

_The peer reviews the student's repository. For each artifact, the peer checks for presence and correctness against the specification. Score `+` if fully present and correct._

| #   | Artifact                              | File Location (Expected)                         | Review Query (Instruction for Peer)                                                                                                                                                                                                              |
| :-- | :------------------------------------ | :----------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Generated Raw Data**                | `week_02_ds/data.csv` or similar                 | **Check for presence of `data.csv`.** Does it contain ~10,000 rows, two numerical columns (e.g., `x`, `y`), and some clearly malformed/missing values (e.g., `NaN`, strings)?                                                                    |
| 2   | **Data Generator Script**             | `week_02_ds/generate_data.py`                    | **Check for presence of the generator script.** Does it use a **Backend-Model-Process** OOP pattern? Does it include a CLI entrypoint (`if __name__ == "__main__"`)?                                                                             |
| 3   | **Filtering (Drop) Script**           | `week_02_ds/filter_data.py`                      | **Check for presence of the filter script.** Does it read `data.csv`, drop malformed/missing rows, and output a **JSON file** (e.g., `clean_data.json`)? Is the filter a pluggable function?                                                     |
| 4   | **Completion Script**                 | `week_02_ds/complete_data.py`                    | **Check for presence of the completion script** (or extended filter script). Does it add a heuristic (e.g., fill with mean/median) to handle missing data? Retains `drop` as an option?                                                          |
| 5   | **Imputation Script**                 | `week_02_ds/impute_data.py`                      | **Check for presence of the imputation script.** Does it infer missing values from complete data subsets (e.g., using a simple model like `KNN` or `mean` by group)?                                                                             |
| 6   | **Aggregation Script & JSON Report**  | `week_02_ds/analyse_data.py` & `aggregates.json` | **Check for presence of analysis script and report.** Does it read **JSON** input, calculate key stats (e.g., mean, error %, outliers), and write a new `.json` file with the results?                                                           |
| 7   | **Normalisation Script**              | `week_02_ds/normalise_data.py`                   | **Check for presence of normalisation script** (or extended filter). Does it transform the data (e.g., `(x - min)/(max - min)`) and output a normalised JSON file?                                                                               |
| 8   | **Visualisation Script (History)**    | `week_02_ds/plot_history.py`                     | **Check for presence of the plot script.** Does it generate a figure (e.g., `history.png`) comparing at least two dataset versions (e.g., raw vs. cleaned) using a scatter or histogram plot?                                                    |
| 9   | **Visualisation Script (Aggregates)** | `week_02_ds/plot_aggregates.py`                  | **Check for presence of the aggregate plot script.** Does it overlay aggregate info (e.g., mean line, confidence band) on the data plot, potentially using the `aggregates.json` metadata?                                                       |
| 10  | **Documentation (`README.md`)**       | `week_02_ds/README.md`                           | **Check for documentation.** Does the `README` clearly state how to run **each** script from the CLI, what each script does, and describe the student's discussion with AI about the design choices (as per Ex. 02-05 documentation challenges)? |

This list focuses on the **pipeline architecture, data handling (CSV/JSON), statistical transformation, and visualisation**—the core of Week 2's learning.

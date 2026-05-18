Thank you for uploading all the files. I now have:

1. **Peer review document** (definition of learning targets)
2. **Week 1 crash course syllabus** (5-day structure)
3. **Exercises for Days 1–5** (with group vs. student work clearly marked)

I have analyzed all materials and extracted the learning targets for Week 1. Below is the complete summary and listing, sorted by **group work** vs. **student work**, following your specification.

---

# Week 1 Learning Targets – Data Management (004283-001)

## Summary

This summary extracts **learning targets** from the Week 1 crash course syllabus and exercises (Days 1–5). Each target is classified as a **Concept**, **Challenge**, or **Artifact** according to the peer review definition. For each target, a query is provided:

- **Concepts** → query a _student respondent_ on their knowledge
- **Challenges** → query a _student respondent_ on their understanding of the challenge
- **Artifacts** → instruct a _student peer_ on how to review a repository for artifact presence

Targets are separated into **Student Work** (submitted to individual student repository) and **Group Work** (submitted to shared group repository).

---

## Student Work (Individual Repository)

Each student maintains their own repository. Peers review these artifacts and query the respondent on concepts and challenges.

| #   | Type      | Target Name                                 | One-line Query for Peer Review                                                                                                                                                                                                                                                                       |
| --- | --------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| S1  | Concept   | Agile Software Development                  | Query the respondent: _Explain the core principle of Agile software development that is of importance for this course._                                                                                                                                                                              |
| S2  | Concept   | Research Story (local variant)              | Query the respondent: _Explain the Research Story format (area, exploration, manifestation) used in this course and how it adapts the user story for scientific inquiry._                                                                                                                            |
| S3  | Concept   | Markdown                                    | Query the respondent: _What is Markdown and what do we use it for in this course?_                                                                                                                                                                                                                   |
| S4  | Concept   | Git – Branching                             | Query the respondent: _What is a Git branch and how does it support parallel development work?_                                                                                                                                                                                                      |
| S5  | Concept   | Git – Merging                               | Query the respondent: _Explain what happens during a Git merge and what a merge conflict is._                                                                                                                                                                                                        |
| S6  | Concept   | IPO Model (Input-Process-Output)            | Query the respondent: _Describe the IPO architectural pattern and why it is fundamental to procedural programming._                                                                                                                                                                                  |
| S7  | Concept   | Function (in programming)                   | Query the respondent: _What is a function in programming and what is the purpose of a "main guard" or entrypoint in a script?_                                                                                                                                                                       |
| S8  | Challenge | Write Research Stories                      | Query the respondent: _Explain why was it nescessary to write research stories_                                                                                                                                                                                                                      |
| S9  | Challenge | Branch, Edit, Merge                         | Query the respondent: _Explain the challenge of creating a branch, editing README.md, merging changes, and handling any potential conflicts._                                                                                                                                                        |
| S10 | Challenge | Write Reflective Docstring                  | Query the respondent: _Explain the challenge of writing a script-level docstring that reflects on what you learned, why it matters for the course, and future help._                                                                                                                                 |
| S11 | Artifact  | Student Repository – Research Stories       | Peer instruction: _Review the respondent's student repository. Verify that a Markdown file exists containing 3–5 research stories following the RS format (area, exploration, manifestation). Check that priorities are included and stories are grouped into a sprint._                             |
| S12 | Artifact  | Student Repository – Git History (Commit 1) | Peer instruction: _Review the respondent's student repository. Verify via `git log` that an initial commit exists with a README.md file._                                                                                                                                                            |
| S13 | Artifact  | Student Repository – Git History (Commit 2) | Peer instruction: _Review the respondent's student repository. Verify via `git log` that a second commit exists with modifications to README.md._                                                                                                                                                    |
| S14 | Artifact  | Student Repository – Branch & Merge         | Peer instruction: _Review the respondent's student repository. Verify that a branch was created (other than main/master), edits were made on that branch, and those changes were merged back into the default branch._                                                                               |
| S15 | Artifact  | Student Repository – Remote Hosting         | Peer instruction: _Review the respondent's shared repository URL. Verify that the repository is publicly accessible on Gitee, GitCode, or equivalent hosting service._                                                                                                                               |
| S16 | Artifact  | Student Repository – IPO Script             | Peer instruction: _Review the respondent's student repository. Locate a script file (reasonably named related to Day 4 exercise) that implements the IPO pattern with multiple inputs, custom processing, and formatted output._                                                                     |
| S17 | Artifact  | Student Repository – IPO as Function        | Peer instruction: _Review the respondent's script. Verify that the IPO logic is encapsulated within a function, and that the function is called from a main guard/entrypoint (Python: `if __name__ == "__main__":`)._                                                                                |
| S18 | Artifact  | Student Repository – Code Comments          | Peer instruction: _Review the respondent's script. Verify the presence of: (a) a function docstring explaining the function, (b) inline comments in processing/output sections where needed, and (c) a script-level docstring with reflections on learning, importance for course, and future help._ |

---

## Group Work (Shared Group Repository)

Groups of ~4 students share a central repository (write permissions within group, read-only for peer reviewers). Peers review these artifacts and query the respondent on group challenges and concepts.

| #   | Type      | Target Name                                       | One-line Query for Peer Review                                                                                                                                                                                                    |
| --- | --------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| G1  | Concept   | IMRaD Report Structure                            | Query the respondent: _Explain the four main sections of an IMRaD report (Introduction, Methods, Results, Discussion) and the purpose of each._                                                                                   |
| G2  | Concept   | Scientific Method                                 | Query the respondent: _Describe the steps of the scientific method and how hypothesis, experiment, and reproducibility fit into this framework._                                                                                  |
| G3  | Concept   | Hypothesis & Null Hypothesis                      | Query the respondent: _What is a hypothesis, what is a null hypothesis, and why is a null hypothesis useful for testing?_                                                                                                         |
| G4  | Concept   | Experiment Design                                 | Query the respondent: _Explain what constitutes a well-designed experiment in terms of testability, measurement, and documentation._                                                                                              |
| G5  | Concept   | Reproducibility                                   | Query the respondent: _What does reproducibility mean in a scientific context, and how does a well-documented method support it?_                                                                                                 |
| G6  | Concept   | Group Repository Collaboration                    | Query the respondent: _Explain how multiple students can collaborate using a shared group repository with write permissions and individual branches._                                                                             |
| G7  | Challenge | Write IMRaD Introduction                          | Query the respondent: _Describe the challenge of writing an Introduction that identifies: an impact (societal value), a reference frame (theory), a challenge (open problem), and a tentative solution (your work)._              |
| G8  | Challenge | Establish Group Repository                        | Query the respondent: _Explain the challenge of setting up a central group repository on a hosting service, granting write permissions to group members, and sharing the read-only URL with peers._                               |
| G9  | Challenge | Create Student Branches in Group Repo             | Query the respondent: _Describe the challenge where each group member creates their own branch (not named with personal information) and updates README.md with a 3-sentence summary of course intentions._                       |
| G10 | Challenge | Merge All Student Branches                        | Query the respondent: _Explain the challenge of merging all student branches into the default branch (master/main) in the central group repository without losing anyone's contributions._                                        |
| G11 | Challenge | Move Old README & Replace with IMRaD              | Query the respondent: _Describe the challenge of moving the existing README.md to a backup file (e.g., README_w1e2.md) and replacing it with the IMRaD report template as the new top-level README._                              |
| G12 | Challenge | Add Superscript/Author-Date References            | Query the respondent: _Explain the challenge of adding formatted references (superscript or author-year style) to the IMRaD report._                                                                                              |
| G13 | Challenge | Extract Hypothesis from Research Questions        | Query the respondent: _Describe the challenge of extracting testable hypotheses (and null hypotheses) from your research stories/questions, especially when questions are broadly formulated._                                    |
| G14 | Challenge | Design Reproducible Experiment                    | Query the respondent: _Explain the challenge of designing an experiment such that a reader following your method could arrive at the same results (reproducibility)._                                                             |
| G15 | Artifact  | Group Repository – IMRaD README.md                | Peer instruction: _Review the group's central repository. Verify that the top-level README.md follows the IMRaD template with sections: Introduction, Methods, Results, Discussion, References._                                  |
| G16 | Artifact  | Group Repository – Old README Preserved           | Peer instruction: _Review the group's central repository. Verify that the original README.md has been moved/renamed (e.g., to README_w1e2.md) and not deleted._                                                                   |
| G17 | Artifact  | Group Repository – Student Branches               | Peer instruction: _Review the group's central repository. Verify that each group member has an individual branch (not default branch) containing a README.md with a 3-sentence summary of course intentions (no personal names)._ |
| G18 | Artifact  | Group Repository – Merged Default Branch          | Peer instruction: _Review the group's central repository. Verify that all student branches have been merged into the default branch (master/main), and the default branch contains the IMRaD README.md._                          |
| G19 | Artifact  | Group Repository – Formatted References           | Peer instruction: _Review the group's IMRaD README.md. Verify that the References section contains 5–10 properly formatted references (superscript or author-year style) relevant to the work._                                   |
| G20 | Artifact  | Group Repository – Hypothesis Statement           | Peer instruction: _Review the group's IMRaD README.md. Locate a clear hypothesis statement and a corresponding null hypothesis (or antithesis) within the Introduction or Methods section._                                       |
| G21 | Artifact  | Group Repository – Experiment Description         | Peer instruction: _Review the group's IMRaD README.md. Verify that an experiment is described in sufficient detail that another researcher could replicate it._                                                                   |
| G22 | Artifact  | Group Repository – Method & Reproducibility Claim | Peer instruction: _Review the group's IMRaD Methods section. Verify that the method is documented step-by-step and includes an explicit or implicit claim of reproducibility._                                                    |

---

## Summary Counts

| Category         | Concepts | Challenges | Artifacts | **Total** |
| ---------------- | -------- | ---------- | --------- | --------- |
| **Student Work** | 7        | 3          | 8         | **18**    |
| **Group Work**   | 6        | 8          | 8         | **22**    |
| **Overall**      | 13       | 11         | 16        | **40**    |

---

## How to Use This List

- **For peer reviewers:** Use the one-line query as a script when reviewing another student's or group's work. For artifacts, follow the instruction to inspect the relevant repository.
- **For respondents (students):** Ensure that for each target, you can answer the concept query, explain the challenge, and produce the required artifact in the correct repository (student or group).
- **For teachers:** Sample these targets during verification. Scores: `+` (passed), `-` (not passed), `0` (cannot tell).

---

_This summary was produced from the Week 1 crash course syllabus and exercise files dated May 11–15, 2026, in accordance with the peer review definition provided._

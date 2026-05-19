# JUFE HDa - Data Management - Peer Review - Prompts

## Prompt, deepseek.com: extracting learning targets, and designing peer-to-respondent queries

As of `20260515` this prompt session provided a full summary of learning targets and their relevance for the course, with good queries that can be used by the students to probe their peers.

### P1

Hi deepseek, please extract and produce a summary and listing of the learning targets found in the first week of the course available at; https://gitee.com/robert-pilstaal/jufe.du.dm.004283-001 .

The definition of learning targets, you'll find in a file that I will provide by uploading. The same goes for the week 1 crash course syllabus and exercises, which comes in several files that I will upload.

Please observe the difference between group and student work defined in the exercises; use this to sort if learning targets between group and student work.

Provide me with a list of all targets, with a one-line statement for each target, which query depending on target type;

- Concepts: a student respondent is queried on their knowledge of the key concept
- Challenges: a student respondent is queried on their understanding of the challenge
- Artifacts: a student peer is instructed on how to review group or student repository for artifact presence

Format the list summary in markdown `.md` for me to download; but wait until I have uploaded all the files for you to analyse.

### P2

Here is the peer review documentation;

#### Notes

Uploaded `20260514_du_jufe_dm_peer_review.md` file using chat interface.

### P3

Here is the week crash course syllabus and exercises;

#### Notes

Uploaded files, using chat interface;

- `20260511_du_jufe_dm_asm_syllabus.md`
- `20260512_du_jufe_dm_asm_01_exercise.md`
- `20260512_du_jufe_dm_asm_02_exercise.md`
- `20260512_du_jufe_dm_asm_03_exercise.md`
- `20260512_du_jufe_dm_asm_03_exercise_template.md`
- `20260512_du_jufe_dm_asm_04_exercise.md`
- `20260512_du_jufe_dm_asm_05_exercise.md`

## `20260515`Prompt, deepseek.com vs copilot: form for collecting a grading vector

Deepseek failed to provie an excel sheet from this prompt, but gave instead an `.csv` file to paste into excel by myself; but that would loose the color coding. The same prompt, with additional "Furthermore; ..." was submitted to copilot, which succeeded in producing a result on a cloud service.

### P1

Given the learning targets that I submit as a file, provide me an excel sheet to download; with a vector of the enumerated learning targets, color coded after the types and class of targets. Where types are the type of targets in artefacts, challenges and concepts and class is the kind of work as in student or group work. Attached, you find the summary of the learning targets to process. You have to provide me with a funcgtional link to the form that I actually can download, and it may not contain any summary file or stub file, but most be the full excel form that you have generated as the result of my prompt. Furthermore;

- It should not contain the full descriptions of the queries, but summaries and the code for each artifact.

#### Notes

Uploading the file `./20260515_du_jufe_dm_peer_review_prompt_deepseek.md` .

## `20260519` Prompt: generate student peer and respondent set

NOTE: this resulted in the script `./20260519_du_jufe_dm_peer_review_group_generator_determ.md` .

Hi deepseek, please provide me with the python script to download, in accord with the following specification;

Given a set of identifiers, each identifier should be grouped with a unique subset of other identifiers, making a new set of identifier groupings that cover the set of identifiers evenly.

Interpretations,

- the new set of identifier groups cover the set of identifiers evenly, so that all identifiers appears the same number of times across the groupings in total.
  - if this is impossible, then try to approximate this as closely as possible
- each identifier should be used as a group identifier for an identifier grouping, meaning we will have as many identifier groupings as we have identifiers in the initial set.
- the identifiers within a grouping should all be unique within the grouping, and selected randomly from the set of identifiers

Inputs,

- Read the st of identifiers from a text file, containing one identifier per line

Outputs,

- report the groupings as lists, with the first identifier being the group identifier, and the other identifiers sorted alphanumerically following the group identifier
  - each grouping is listed on a single line, with spaces separating each identifier
- sort the output of groupings alphanumerically on the group identifier

Conditions,

- each grouping should contain 9 identifiers

Format,

- Write the script in Python,
- Use a Backend-Model-Process pattern, defining two classes and a function(s)
  - Formalise file reading as a backend, accepting target file(s), yielding data to the model
  - Formalise model as a process, accepting backend object and process function(s)
- Use IPO style procedural programm for any process function(s)
- Include a main function, which accepts target file and arguments from CLI, using python argumentparser
  - the main function should be invoked if in the top-level code environment, ie. `if __name__ == '__main__'`
- All code should follow PEP 8, and have good docstrings for classes, functions and the script as a whole; with inline descriptive comments for each relevant block of code and a concise one-line description of the script in the help option from the CLI.
  - Docstrings focus architecture design and intent
  - Inline commentary focus procedural and algorithmic design

### Variation 2

Hi deepseek, please provide me with the python script to download, in accord with the following specification;

Given a set of identifiers, each identifier should be grouped with a unique subset of other identifiers, making a new set of identifier groupings that cover the set of identifiers evenly.

Interpretations,

- the new set of identifier groups cover the set of identifiers evenly, so that all identifiers appears the same number of times across the groupings in total.
  - if this is impossible, then approximate this as closely as possible, finding and reporting a reasonable approximative set as close as possible to the specification; within reasonable time and effort
- each identifier should be used as a group identifier for an identifier grouping, meaning we will have as many identifier groupings as we have identifiers in the initial set.
- the identifiers within a grouping should all be unique within the grouping, and selected randomly from the set of identifiers

Inputs,

- Read the st of identifiers from a text file, containing one identifier per line

Outputs,

- report the groupings as lists, with the first identifier being the group identifier, and the other identifiers sorted alphanumerically following the group identifier
  - each grouping is listed on a single line, with spaces separating each identifier
- sort the output of groupings alphanumerically on the group identifier

Conditions,

- each grouping should contain 9 identifiers

Format,

- Write the script in Python,
- Use a Backend-Model-Process pattern, defining two classes and a function(s)
  - Formalise file reading as a backend, accepting target file(s), yielding data to the model
  - Formalise model as a process, accepting backend object and process function(s)
- Use IPO style procedural programm for any process function(s)
- Include a main function, which accepts target file and arguments from CLI, using python argumentparser
  - the main function should be invoked if in the top-level code environment, ie. `if __name__ == '__main__'`
- All code should follow PEP 8, and have good docstrings for classes, functions and the script as a whole; with inline descriptive comments for each relevant block of code and a concise one-line description of the script in the help option from the CLI.
  - Docstrings focus architecture design and intent
  - Inline commentary focus procedural and algorithmic design

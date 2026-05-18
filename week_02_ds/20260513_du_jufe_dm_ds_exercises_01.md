# Lecuture 0201, exercise; IPO from CLI

## Overview

The task is to build a small script analysing a list of numbers, which includes generating the data, and structuring the code appropriately. Last but not least, the code should be refactored a bit, implementing it in a backend-model-process and object-oriented pattern.

## Challenges

Todays exercises is split into 3 incremental challenges to get you started. Begin with the first, continuing through the rest as you go.

### 1. Generate data

Generate the data to process, using a script similar to the below;

```pyton
# From deepseek
import csv
import random

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'y'])
    for _ in range(10000):
        writer.writerow([random.uniform(0, 1), random.uniform(0, 1)])

print("data.csv generated with 10,000 rows")
```

Reference:

- https://docs.python.org/3/tutorial/

### 2. Process the data

The data should now be processed, producing a simple data arithmetic from the data contained in the data file you generated above.

- Program using IPO and python from CLI
- Processing a data metric artifact
  - implemented as a process function
- Process generated data from CLI

Example arithmetic artifact;

```python
data = [1,2,3,4]
mean = sum(data)/len(data)
```

Reference:

- https://docs.python.org/3/tutorial/
- https://github.com/ropil/stubs_py3
  - https://gitee.com/robert-pilstaal/stubs-p3
  - https://gitee.com/robert-pilstaal/stubs-p3/blob/master/stub_reading_file_or_stdin_gpl.py

### 3. Structure as objects, in Object Oriented Programming fashion (OOP)

Define two classes, one formalising the file reading backend, and one formalising the internal process. The process class accepts the backend class and process function as arguments upon initialisation - and your process functions might need to be adapted to fit into the new Object Oriented (OO) architecture of your script;

- Formalise file reading as a backend, accepting target file(s)
- Formalise model as a process, accepting backend object and process function
- Rewrite process function to conform to OOP structure

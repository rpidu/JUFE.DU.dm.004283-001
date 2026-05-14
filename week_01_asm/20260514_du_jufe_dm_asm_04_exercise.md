# Day 4 Exercise – IPO Model

The **Input Output Process** (IPO) architectural pattern is an atomistic pattern that is very hard to escape from in _procedural_ programming; you will nescessarily find yourself writing IPO patterns all over your code. Since it is so simple, it might reflect to you as a banality, but knowing about it will help you in discerning what code can be structured differently - **refactoring** it into more loosely coupled and _disentangled_ code, which is easier to audit and maintain.

## Objective

Write a script using the IPO.

## Example

This example is written in BASH,

```bash
#!/bin/bash
# Input
read -p "Enter number: " num

# Process
result=$((num * 2))

# Output
echo "Result: $result"
```

## Challenges

- If you are using powershell, **convert** the above into powershell
  - _optional:_ you may convert it into python or your _desired language_ within this course instead
- **Extensions** to the code;
  - Add multiple _inputs_
  - Add your own _processing_, extending the simple arithmetic
  - Update the _output_ to match your new process and inputs, as you go
- Write the same code in **Python** (recommended), or your desired language
  - it is optional to write the above extensions in powershell, you can
    convert into your preferred language before implementing extensions.
- Implement your IPO pattern as a **function**
  - _Python specific:_ call the function from behind a _main-guard/entrypoint_ at the end of
    the script file
  - _Other languages:_ mimic this with a call to your function, which is included as a library and executed from the main execution entrypoint.
- Add **coments** to the code,
  - a _docstring_ explaining your _function_,
  - _comments_ in processing and output _sections_ of the function, if
    nescessary to explain each step, and also
  - a _docstring_ in the beginning of the _script_, with your **reflection** answering;
    - what did I **learn** from this?
    - why is it **important** for the course?
    - what will it help me with in the **future**?
- Hand in by submitting the code file, to your **student repository**; name it
  reasonably so we can identify it - it should be _semantically_ linked to
  how this exercise is named and described.

## References

- https://en.wikipedia.org/wiki/Input-process-output_model
- [python.org - functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [python.org - entrypoint](https://docs.python.org/3/library/__main__.html#idiomatic-usage)

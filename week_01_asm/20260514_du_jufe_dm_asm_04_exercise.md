# Day 4 Exercise – IPO Model

## Objective

Write a Bash script using IPO.

## Example

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

- If you are using powershell, convert the above into powershell
  - optional, you may convert it into python or your desired language within this course instead
- Extensions to the code;
  - Add multiple inputs
  - Add your own processing, extending the simple arithmetic
  - Update the output to match your new process and inputs, as you go
- Write the same code in Python (recommended), or your desired language
  - it is optional to write the above extensions in powershell, you can
    convert into python before implementing extensions.
- Implement your IPO pattern as a function
  - Python specific; call the function from behind a main-guard/entrypoint at the end of
    the script file
  - Other languages; mimic this with a call to your function, which is included as a library and executed from the main execution entrypoint.
- Add coments to the code,
  - a docstring explaining your function,
  - comments in processing and output sections of the function, if
    nescessary to explain each step, and also
  - a docstring in the beginning of the script, with your **reflection** answering;
    - what did I **learn** from this?
    - why is it **important** for the course?
    - what will it help me with in the **future**?
- Hand in by submitting the code file, to your **student repository**; name it
  reasonably so we can identify it - it should be _semantically_ linked to
  how this exercise is named and described.

## References

- https://en.wikipedia.org/wiki/Input-process-output_model

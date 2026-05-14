# 5-Day Exercise Set

TODO: split up in separate files, and clean-up
TODO: fix examples, should execute against `./`
TODO: extend with a normality check against data (day 4)
TODO: extend all days with challenges

## Day 1

Task: Build a small script analysing a list of numbers.

Example:

```python
data = [1,2,3,4]
mean = sum(data)/len(data)
```

Reference:
https://docs.python.org/3/tutorial/

---

## Day 2

Task: Load CSV and clean missing values.

Example:

```python
import pandas as pd

df = pd.read_csv("data.csv")
df = df.dropna()
```

Reference:
https://pandas.pydata.org/docs/user_guide/10min.html

---

## Day 3

Task: Group and aggregate data.

Example:

```python
df.groupby("category").mean()
```

With pandas all together:

```python
import pandas as pd

df = pd.read_csv('data.csv')
df = df.dropna()
df = df.groupby('category').mean()
```

Reference:
https://wesmckinney.com/book/

---

## Day 4

Task: Perform correlation analysis.

Example:

```python
df.corr()
```

Further example, on mean and standard deviation:

```python
import numpy as np

mean = np.mean(df['value'])
std = np.std(df['value'])
```

Reference:
https://jakevdp.github.io/PythonDataScienceHandbook/

---

## Day 5

Task: Plot dataset.

Example:

```python
import matplotlib.pyplot as plt

df.plot()
plt.show()
```

Further example, with histogram:

```python
import matplotlib.pyplot as plt

plt.hist(df['value'])
plt.show()
```

Reference:
https://matplotlib.org/stable/tutorials/index.html

---

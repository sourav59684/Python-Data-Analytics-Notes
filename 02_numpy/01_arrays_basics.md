# 🔢 NumPy Arrays — Basics

---

## 📌 What Is NumPy?

**NumPy** (Numerical Python) is a library that lets Python work with numbers
— especially big groups of numbers — much faster and more conveniently than
plain Python lists.

```python
import numpy as np    # "np" is the standard shortcut everyone uses
```

The core building block of NumPy is the **array** (technically called an
`ndarray`, short for "n-dimensional array"). Think of it as an upgraded list,
built specifically for fast math.

---

## 📊 Why This Matters for Data Analytics

Pandas (which you'll use constantly for data analytics) is actually **built
on top of NumPy**. Every column in a Pandas DataFrame is really a NumPy
array underneath. Understanding arrays now means you'll understand *why*
Pandas behaves the way it does later — and NumPy alone is also what powers
fast calculations on large numeric datasets (averages, sums, statistics).

---

## 🏗️ Array vs. Python List

| | Python List | NumPy Array |
|---|---|---|
| Can hold mixed types | ✅ Yes (`[1, "two", 3.0]`) | ❌ No — all items must be the same type |
| Math on the whole collection at once | ❌ No (`[1,2,3] * 2` repeats the list) | ✅ Yes (`array * 2` multiplies every item) |
| Speed on large data | Slower | Much faster |
| Built for | General-purpose storage | Numeric/data calculations |

```python
# Python list — this does NOT do what you might expect
prices = [100, 200, 300]
print(prices * 2)   # [100, 200, 300, 100, 200, 300] → repeats the list!

# NumPy array — does actual math
import numpy as np
prices = np.array([100, 200, 300])
print(prices * 2)   # [200 400 600] → multiplies every number
```
*Explanation:* This single difference is one of the biggest reasons NumPy
(and Pandas) exists — real math on entire collections, in one line.

---

## 🧱 Creating Arrays

```python
import numpy as np

a = np.array([1, 2, 3, 4])                 # from a list
b = np.array([[1, 2, 3], [4, 5, 6]])        # 2D array (rows and columns, like a table)
```

### 🔧 Common Array-Creation Functions

| Function | What It Does | Example |
|---|---|---|
| `np.array(list)` | Creates an array from a list | `np.array([1,2,3])` |
| `np.zeros(n)` | Creates an array of all zeros | `np.zeros(4)` → `[0. 0. 0. 0.]` |
| `np.ones(n)` | Creates an array of all ones | `np.ones(3)` → `[1. 1. 1.]` |
| `np.arange(start, stop, step)` | Like Python's `range()`, but returns an array | `np.arange(0, 10, 2)` → `[0 2 4 6 8]` |
| `np.linspace(start, stop, n)` | Creates `n` evenly spaced numbers | `np.linspace(0, 1, 5)` → `[0. 0.25 0.5 0.75 1.]` |
| `np.full(n, value)` | Fills an array with one repeated value | `np.full(3, 7)` → `[7 7 7]` |

```python
zeros = np.zeros(5)
print(zeros)          # [0. 0. 0. 0. 0.]

sequence = np.arange(1, 11)
print(sequence)        # [ 1  2  3  4  5  6  7  8  9 10]
```

---

## 🔍 Array Attributes — Inspecting an Array

| Attribute | What It Tells You | Example |
|---|---|---|
| `.shape` | Rows and columns (dimensions) | `(2, 3)` → 2 rows, 3 columns |
| `.ndim` | Number of dimensions | `1` for a plain list, `2` for a table |
| `.size` | Total number of elements | `6` for a 2×3 array |
| `.dtype` | The data type stored in the array | `int64`, `float64` |

```python
data = np.array([[1, 2, 3], [4, 5, 6]])

print(data.shape)   # (2, 3)  → 2 rows, 3 columns
print(data.ndim)    # 2       → 2-dimensional
print(data.size)    # 6       → 6 total numbers
print(data.dtype)   # int64   → whole numbers
```

---

## 💡 Examples

### 1. Basic — Creating and inspecting an array
```python
import numpy as np

scores = np.array([88, 92, 79, 95, 60])
print(scores)
print("Shape:", scores.shape)
print("Type:", scores.dtype)
```

### 2. Analytics Use Case — Instant math on a whole column of numbers
```python
sales = np.array([1200, 1500, 900, 2000, 1100])

total = sales.sum()
average = sales.mean()
highest = sales.max()

print("Total:", total)      # 6700
print("Average:", average)  # 1340.0
print("Highest:", highest)  # 2000
```
*Explanation:* This is the exact same style of calculation you'll do on
Pandas DataFrame columns later — NumPy is what makes it fast under the hood.

### 3. Creating a table-like 2D array
```python
# Rows = days, Columns = [temperature, humidity]
weather = np.array([
    [30, 65],
    [32, 60],
    [28, 70]
])
print(weather.shape)   # (3, 2) → 3 days, 2 measurements each
print(weather[0])       # [30 65] → first day's data
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting `import numpy as np` | Always import it first at the top of your file |
| Expecting `list * 2` to do math like an array | Convert to `np.array()` first if you want real multiplication |
| Mixing types in an array (`np.array([1, "two"])`) | NumPy converts everything to one shared type (often turning numbers into text) — avoid mixing |
| Confusing `.size` with `.shape` | `.size` is total count, `.shape` is the (rows, columns) layout |

---

## ✍️ Practice Questions

1. What's the main difference between a Python list and a NumPy array?
2. Create a NumPy array of the numbers 1 through 10 using `np.arange()`.
3. What does `.shape` tell you about an array?
4. Given `data = np.array([[1,2],[3,4],[5,6]])`, what would `data.shape` return?
5. Why is NumPy faster than plain Python lists for math operations?

<details>
<summary>💡 Click to see answers</summary>

1. A NumPy array requires all elements to be the same type and supports
   real math operations across the entire collection at once, while a
   Python list can mix types but doesn't support that kind of direct math.
2. ```python
   import numpy as np
   numbers = np.arange(1, 11)
   ```
3. `.shape` tells you the array's dimensions — how many rows and columns it has.
4. `(3, 2)` — 3 rows, 2 columns.
5. NumPy arrays store data in a more compact, uniform way in memory and use
   optimized, pre-compiled code for calculations, instead of Python looping
   through each item one by one.

</details>

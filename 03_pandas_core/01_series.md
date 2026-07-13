# 🐼 Pandas — Series Fundamentals

---

## 📌 What Is a Series?

A **Series** is Pandas' version of a single column of data — a list of
values, but with labels (called an **index**) attached to each one.

```python
import pandas as pd

scores = pd.Series([88, 92, 79, 95])
print(scores)
```
```
0    88
1    92
2    79
3    95
dtype: int64
```

The numbers on the left (`0, 1, 2, 3`) are the **index** — automatically
created labels for each value, unless you set your own.

> 💬 **Key idea:** A Series is basically a NumPy array with labels attached.
> A whole spreadsheet (DataFrame) is just several Series stuck together,
> one per column.

---

## 📊 Why This Matters for Data Analytics

Every single column in a Pandas DataFrame — the tool you'll use constantly
for real analytics work — is actually a Series underneath. Understanding how
a Series behaves on its own makes everything about DataFrames make sense later.

---

## 🏗️ Creating a Series

```python
import pandas as pd

# From a list — gets automatic index (0, 1, 2, ...)
scores = pd.Series([88, 92, 79, 95])

# With a custom index (labels instead of numbers)
scores = pd.Series([88, 92, 79, 95], index=["Ravi", "Anu", "Simran", "Karan"])
print(scores)
```
```
Ravi       88
Anu        92
Simran     79
Karan      95
dtype: int64
```

```python
# From a dictionary — keys automatically become the index
prices = pd.Series({"apple": 100, "banana": 40, "mango": 80})
print(prices)
```
```
apple     100
banana     40
mango      80
dtype: int64
```

---

## 🔧 Common Series Methods & Attributes

| Method / Attribute | What It Does | Example |
|---|---|---|
| `.index` | Shows the labels | `scores.index` |
| `.values` | Shows just the values (as a NumPy array) | `scores.values` |
| `.dtype` | Shows the data type stored | `scores.dtype` |
| `.sum()` | Adds up all values | `scores.sum()` |
| `.mean()` | Average of all values | `scores.mean()` |
| `.max()` / `.min()` | Largest / smallest value | `scores.max()` |
| `.sort_values()` | Sorts the values | `scores.sort_values()` |
| `.value_counts()` | Counts how often each value appears | `data.value_counts()` |
| `.unique()` | Lists each distinct value once | `data.unique()` |
| `.isnull()` | Checks for missing values, returns True/False for each | `scores.isnull()` |

```python
scores = pd.Series([88, 92, 79, 95, 60])

print(scores.mean())     # 82.8
print(scores.max())      # 95
print(scores.sort_values())   # sorted smallest to largest
```

---

## 🔎 Accessing Values in a Series

```python
scores = pd.Series([88, 92, 79, 95], index=["Ravi", "Anu", "Simran", "Karan"])

print(scores["Ravi"])     # 88 → access by label
print(scores.iloc[0])      # 88 → access by position (0 = first)
print(scores[scores > 85]) # filters, keeping only values > 85
```

| Access Method | Meaning |
|---|---|
| `series["label"]` | Access by label/index name |
| `series.iloc[0]` | Access by position (like a list) |
| `series[condition]` | Filter values matching a condition |

---

## 💡 Examples

### 1. Basic — Creating and inspecting a Series
```python
import pandas as pd

sales = pd.Series([1200, 800, 1500, 300, 2000])
print(sales)
print("Total:", sales.sum())
print("Average:", sales.mean())
```

### 2. Analytics Use Case — Labeled data for readability
```python
city_population = pd.Series({
    "Mumbai": 20400000,
    "Delhi": 30300000,
    "Pune": 7400000
})

print(city_population["Delhi"])          # 30300000
print(city_population.sort_values(ascending=False))   # largest to smallest
```

### 3. Filtering values with a condition
```python
temperatures = pd.Series([22, 35, 28, 40, 19, 31])
hot_days = temperatures[temperatures > 30]
print(hot_days)
```

### 4. Counting how often each value appears
```python
ratings = pd.Series([5, 4, 5, 3, 5, 4, 2, 5])
print(ratings.value_counts())
```
```
5    4
4    2
3    1
2    1
dtype: int64
```
*Explanation:* `.value_counts()` is one of the most-used methods in real
analytics work — instantly showing how often each unique value shows up,
like counting votes or survey ratings.

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Assuming a Series is just a plain list | It's a list **with labels** — that's the whole point |
| Using `[ ]` when you meant `.iloc[ ]` for position-based access | If your index isn't 0,1,2..., use `.iloc[position]` to be safe |
| Forgetting `.value_counts()` exists and counting manually | Use `.value_counts()` — much faster and built for exactly this |
| Confusing `.values` (the data) with `.index` (the labels) | `.values` = the actual numbers, `.index` = the labels attached to them |

---

## ✍️ Practice Questions

1. What is the difference between a Series and a Python list?
2. Create a Series of 4 city names with population values as a custom index.
3. What does `.value_counts()` do?
4. Given `s = pd.Series([10, 20, 30])`, what does `s.iloc[1]` return?
5. How would you filter a Series `temps` to keep only values below 20?

<details>
<summary>💡 Click to see answers</summary>

1. A Series is like a list, but every value has a **label (index)**
   attached, and it comes with many built-in methods for analysis
   (`.mean()`, `.sort_values()`, etc.) that plain lists don't have.
2. ```python
   population = pd.Series(
       [20400000, 30300000, 7400000, 4600000],
       index=["Mumbai", "Delhi", "Pune", "Chennai"]
   )
   ```
3. It counts how many times each unique value appears in the Series,
   sorted from most frequent to least frequent by default.
4. `20` — `.iloc[1]` accesses the item at position 1 (the second item).
5. ```python
   cold = temps[temps < 20]
   ```

</details>

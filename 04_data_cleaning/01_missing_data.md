# 🧹 Data Cleaning — Missing Data

---

## 📌 What Is Missing Data?

**Missing data** is any spot in your dataset where a value should exist but
doesn't — a blank cell in a spreadsheet, an empty field from a form, a value
that never got recorded. Pandas represents these as **`NaN`** (Not a Number).

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Ravi", "Anu", None],
    "age": [25, np.nan, 28]
})
print(df)
```
```
   name   age
0  Ravi  25.0
1   Anu   NaN
2  None  28.0
```

> 💬 **Key idea:** `NaN` isn't `0` and isn't an empty string `""` — it
> specifically means "no value was recorded here."

---

## 📊 Why This Matters for Data Analytics

Missing data is everywhere in real datasets — skipped survey questions,
failed sensor readings, incomplete forms. If you calculate an average
without handling missing values properly, your results can be misleading.
Deciding how to handle missing data (remove it? fill it in?) is one of the
most important judgment calls in any analysis.

---

## 🔍 1. Finding Missing Values

### 🔧 Common Methods

| Method | What It Does | Example |
|---|---|---|
| `.isnull()` | Returns True/False for each value | `df.isnull()` |
| `.isnull().sum()` | Counts missing values per column | `df.isnull().sum()` |
| `.notnull()` | Opposite of `.isnull()` — True where data exists | `df.notnull()` |
| `.isnull().any()` | Checks if a column has ANY missing values | `df.isnull().any()` |

```python
print(df.isnull())
```
```
    name    age
0  False  False
1  False   True
2   True  False
```

```python
print(df.isnull().sum())
```
```
name    1
age     1
dtype: int64
```
*Explanation:* `.isnull().sum()` is the single most useful line for a quick
missing-data report — it tells you exactly how many missing values are in
every column, in one line.

---

## 🗑️ 2. Removing Missing Data — `.dropna()`

```python
df_clean = df.dropna()          # removes any ROW that has at least one missing value
```

### 🔧 Common `.dropna()` Options

| Option | What It Does | Example |
|---|---|---|
| `.dropna()` | Drops rows with ANY missing value | Default behavior |
| `.dropna(axis=1)` | Drops COLUMNS with any missing value | `df.dropna(axis=1)` |
| `.dropna(subset=["col"])` | Only checks specific column(s) | `df.dropna(subset=["age"])` |
| `.dropna(how="all")` | Only drops rows where EVERY value is missing | Less aggressive |

```python
df_clean = df.dropna(subset=["age"])   # only removes rows missing "age"
```

> ⚠️ **`.dropna()` can throw away a lot of data.** If 30% of rows are missing
> just one column, dropping all of them loses a lot of otherwise-good
> information. Consider filling instead, when appropriate.

---

## 🩹 3. Filling in Missing Data — `.fillna()`

```python
df["age"] = df["age"].fillna(df["age"].mean())    # fill with the average age
df["name"] = df["name"].fillna("Unknown")           # fill with a placeholder
```

### 🔧 Common Filling Strategies

| Strategy | Best For | Example |
|---|---|---|
| Fill with mean/average | Numeric columns (price, age, score) | `df["age"].fillna(df["age"].mean())` |
| Fill with median | Numeric columns with outliers | `df["salary"].fillna(df["salary"].median())` |
| Fill with mode (most common value) | Categorical columns (city, category) | `df["city"].fillna(df["city"].mode()[0])` |
| Fill with a fixed placeholder | When missing itself is meaningful | `df["name"].fillna("Unknown")` |
| Forward fill (`.ffill()`) | Time series — carry the last known value forward | `df["price"].ffill()` |
| Backward fill (`.bfill()`) | Fill using the next known value | `df["price"].bfill()` |

```python
sales = pd.Series([100, np.nan, np.nan, 200, np.nan])
print(sales.ffill())    # [100, 100, 100, 200, 200]
print(sales.bfill())    # [100, 200, 200, 200, NaN]
```
*Explanation:* `.ffill()` carries the last real value forward to fill gaps.
`.bfill()` does the opposite — pulls the next real value backward. Notice
the last value stays `NaN` with `.bfill()` because there's nothing after it.

---

## 💡 Examples

### 1. Basic — Checking for missing values
```python
df = pd.read_csv("customer_data.csv")
print(df.isnull().sum())
```

### 2. Analytics Use Case — Filling numeric and categorical columns differently
```python
df["age"] = df["age"].fillna(df["age"].mean())
df["city"] = df["city"].fillna(df["city"].mode()[0])
print(df.isnull().sum())   # should now show 0 for both columns
```
*Explanation:* Using the **mean** for numbers and the **mode** (most common
value) for categories is the standard, sensible default approach for simple
missing-data imputation.

### 3. Dropping rows only when a critical column is missing
```python
df_clean = df.dropna(subset=["customer_id"])   # customer_id is essential, others less so
```

### 4. Comparing before and after cleaning
```python
print("Before:", df.shape)
df_clean = df.dropna()
print("After:", df_clean.shape)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Using `== None` or `== np.nan` to check for missing values | Use `.isnull()` — direct comparisons with NaN don't work reliably |
| Dropping all rows with any missing value without checking impact first | Check `.isnull().sum()` and `.shape` before and after — you might lose too much data |
| Filling every column the same way | Use mean/median for numbers, mode or a placeholder for categories |
| Forgetting `.dropna()` and `.fillna()` return new DataFrames by default | Reassign the result: `df = df.dropna()`, or use `inplace=True` |

---

## ✍️ Practice Questions

1. What does `NaN` mean in Pandas?
2. Write code to count missing values in every column of `df`.
3. What's the difference between `.dropna()` and `.fillna()`?
4. Why might filling with the mode be better than the mean for a "city" column?
5. What does `.ffill()` do, and when is it useful?

<details>
<summary>💡 Click to see answers</summary>

1. `NaN` stands for "Not a Number" — it's how Pandas represents a missing or
   unrecorded value.
2. ```python
   df.isnull().sum()
   ```
3. `.dropna()` **removes** rows or columns that have missing values.
   `.fillna()` **replaces** missing values with something else (a number, a
   placeholder, etc.) instead of removing data.
4. "City" is a category (text), not a number — you can't average text values.
   The mode (most frequent value) is a sensible stand-in for a missing category.
5. `.ffill()` (forward fill) replaces a missing value with the last known
   value before it. It's especially useful for time series data, like
   carrying forward yesterday's stock price if today's is missing.

</details>

# 🐼 Pandas — Inspecting Data

---

## 📌 Why Inspect Data First?

Before cleaning, filtering, or analyzing anything, you need to understand
what you're working with — how many rows, what columns exist, what type of
data is in each, and whether anything looks off. Pandas gives you a handful
of go-to commands for this "first look."

```python
import pandas as pd
df = pd.read_csv("sales_data.csv")

df.head()   # peek at the first few rows
```

> 💬 **This is always step one.** Every real analytics task starts with
> inspecting the data before doing anything else with it.

---

## 📊 Why This Matters for Data Analytics

Skipping this step is one of the most common beginner mistakes — jumping
straight into analysis on data you don't actually understand yet. A quick
inspection reveals missing values, wrong data types, and unexpected values
*before* they cause confusing errors later.

---

## 🔧 Common Inspection Methods

| Method | What It Shows |
|---|---|
| `.head(n)` | First `n` rows (default 5) |
| `.tail(n)` | Last `n` rows (default 5) |
| `.info()` | Column names, data types, non-null counts, memory usage |
| `.describe()` | Statistical summary (mean, min, max, etc.) for numeric columns |
| `.shape` | (rows, columns) |
| `.columns` | List of column names |
| `.dtypes` | Data type of every column |
| `.sample(n)` | `n` random rows (useful for spotting issues `.head()` might miss) |
| `.nunique()` | Number of unique values per column |

```python
df.head()      # first 5 rows
df.tail(3)      # last 3 rows
df.info()       # structure overview
df.describe()   # statistics summary
```

---

## 🏗️ `.info()` — Understanding the Output

```python
df.info()
```
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype
---  ------   --------------  -----
 0   name     500 non-null    object
 1   age      480 non-null    int64
 2   salary   500 non-null    float64
 3   city     495 non-null    object
dtypes: float64(1), int64(1), object(2)
```

| What to Look For | Why |
|---|---|
| **Non-Null Count** lower than total rows | Means that column has missing values (`age` has 20 missing, `city` has 5) |
| **Dtype** matches what you expect | A "salary" column shown as `object` (text) instead of `float64` usually means dirty data |
| Total rows/columns | Confirms you loaded what you expected |

---

## 📈 `.describe()` — Understanding the Output

```python
df.describe()
```
```
              age       salary
count   480.000000   500.000000
mean     34.200000  55340.500000
std       8.913000  12500.750000
min      18.000000  25000.000000
25%      28.000000  46000.000000
50%      34.000000  55000.000000
75%      40.000000  63000.000000
max      65.000000  99000.000000
```

| Row | Meaning |
|---|---|
| `count` | How many non-missing values (matches `.info()`) |
| `mean` | Average |
| `std` | Standard deviation — how spread out the values are |
| `min` / `max` | Smallest and largest values |
| `25%`, `50%`, `75%` | Percentiles — `50%` is the median |

> 💡 By default, `.describe()` only covers **numeric** columns. Add
> `.describe(include="all")` to include text columns too (shows count,
> unique values, and the most common value for those).

---

## 💡 Examples

### 1. Basic — First look at a new dataset
```python
import pandas as pd
df = pd.read_csv("sales_data.csv")

print(df.shape)     # (1000, 6)
print(df.head())     # first 5 rows
print(df.info())     # structure and missing values
```

### 2. Analytics Use Case — Spotting missing data immediately
```python
df.info()
# If "customer_email" shows 950 non-null out of 1000 rows,
# you instantly know 50 rows are missing an email — before doing any analysis.
```

### 3. Quick statistical summary of prices
```python
df["price"].describe()
```
```
count    1000.000000
mean      249.870000
std        85.320000
min        10.000000
25%       199.990000
50%       249.500000
75%       299.990000
max       999.990000
Name: price, dtype: float64
```
*Explanation:* Running `.describe()` on a single column gives you a fast
statistical snapshot — useful for spotting unusually high/low values (like a
`max` of 999.99 when most prices are under 300, which might be an outlier).

### 4. Checking unique values per column
```python
print(df.nunique())
```
```
name        850
age          45
city         12
```
*Explanation:* Helps you understand which columns are categories (like
`city` with only 12 unique values) versus columns that are mostly unique
identifiers (like `name`).

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Skipping inspection and jumping straight to analysis | Always run `.head()`, `.info()`, `.describe()` first |
| Assuming `.describe()` covers text columns too | Add `include="all"` if you want text/object columns included |
| Ignoring the "Non-Null Count" in `.info()` | It's your first clue about where missing data exists |
| Only checking `.head()` and assuming the whole file looks the same | Also check `.tail()` and `.sample()` — problems can be anywhere in the file |

---

## ✍️ Practice Questions

1. What's the difference between `.head()` and `.sample()`?
2. What does the "Non-Null Count" column in `.info()` tell you?
3. What does the `50%` row mean in `.describe()`'s output?
4. Why should you check `.shape` right after loading a new dataset?
5. How would you include text columns in `.describe()`'s output?

<details>
<summary>💡 Click to see answers</summary>

1. `.head()` always shows the first rows in order. `.sample()` shows random
   rows from anywhere in the dataset — better for spotting issues that
   might not appear at the very start.
2. It tells you how many non-missing values exist in that column — if it's
   lower than the total row count, that column has missing data.
3. The `50%` row is the **median** — the middle value when all values are
   sorted from smallest to largest.
4. To immediately confirm the dataset loaded correctly and has the expected
   number of rows and columns, before doing any further work.
5. ```python
   df.describe(include="all")
   ```

</details>

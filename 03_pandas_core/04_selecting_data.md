# 🐼 Pandas — Selecting Data (loc, iloc, Filtering)

---

## 📌 What Does "Selecting Data" Mean?

Once your data is loaded, you rarely want the *whole* thing at once. You'll
usually want:
- Specific **columns** ("just show me name and salary")
- Specific **rows** ("just show me the first 10 rows")
- Specific rows **matching a condition** ("only rows where age > 30")

Pandas gives you dedicated tools for each of these.

---

## 📊 Why This Matters for Data Analytics

Selecting and filtering data is something you'll do in almost every single
line of real analytics work — pulling out just the columns you need, or just
the rows that matter for a specific question you're answering.

---

## 📋 1. Selecting Columns

```python
import pandas as pd
df = pd.DataFrame({
    "name": ["Ravi", "Anu", "Simran"],
    "age": [25, 30, 28],
    "city": ["Mumbai", "Delhi", "Pune"]
})

print(df["name"])              # single column → returns a Series
print(df[["name", "city"]])     # multiple columns → returns a DataFrame (note the double brackets!)
```

> ⚠️ **Single `[ ]` vs. double `[[ ]]`:** `df["name"]` gives you a Series.
> `df[["name", "city"]]` gives you a DataFrame with just those columns. The
> double brackets are needed for selecting more than one column.

---

## 🔎 2. `.loc[]` and `.iloc[]` — Selecting Rows (and Columns)

| | `.loc[]` | `.iloc[]` |
|---|---|---|
| Selects by | **Label** (row/column names) | **Position** (numbers, like a list) |
| Example | `df.loc[0, "name"]` | `df.iloc[0, 0]` |
| Range behavior | Includes the last item | Excludes the last item (like Python slicing) |

```python
df = pd.DataFrame({
    "name": ["Ravi", "Anu", "Simran", "Karan"],
    "age": [25, 30, 28, 35]
})

print(df.loc[0])          # first row, by label
print(df.loc[0, "name"])   # "Ravi" → row 0, column "name"
print(df.loc[0:2])         # rows 0, 1, 2 → INCLUDES row 2 with .loc

print(df.iloc[0])          # first row, by position
print(df.iloc[0, 0])        # "Ravi" → row 0, column 0
print(df.iloc[0:2])         # rows 0, 1 → EXCLUDES row 2 with .iloc
```

### 🔧 Common `.loc` / `.iloc` Patterns

| Pattern | What It Does |
|---|---|
| `df.loc[5]` | Row with label `5` |
| `df.loc[:, "age"]` | All rows, just the "age" column |
| `df.iloc[0:5]` | First 5 rows, by position |
| `df.iloc[:, 0:2]` | All rows, first 2 columns by position |
| `df.loc[df["age"] > 30]` | Rows where age > 30 (condition-based) |

---

## ✅ 3. Filtering Rows with Conditions

```python
df = pd.DataFrame({
    "name": ["Ravi", "Anu", "Simran", "Karan"],
    "age": [25, 30, 28, 35],
    "city": ["Mumbai", "Delhi", "Mumbai", "Pune"]
})

# Single condition
adults_over_28 = df[df["age"] > 28]

# Multiple conditions — use & (and) / | (or), each condition in ( )
result = df[(df["age"] > 25) & (df["city"] == "Mumbai")]
print(result)
```

> ⚠️ **Just like NumPy, use `&` and `|`, not `and`/`or`,** and wrap each
> condition in its own parentheses.

### 🔧 Common Filtering Tools

| Tool | What It Does | Example |
|---|---|---|
| `df[condition]` | Basic filter | `df[df["age"] > 30]` |
| `&` , `|` | Combine multiple conditions | `df[(cond1) & (cond2)]` |
| `.isin([...])` | Keep rows where value is in a list | `df[df["city"].isin(["Mumbai","Delhi"])]` |
| `~` | NOT — flips a condition | `df[~(df["age"] > 30)]` |
| `.between(a, b)` | Keep values within a range | `df[df["age"].between(25, 35)]` |

```python
target_cities = ["Mumbai", "Pune"]
filtered = df[df["city"].isin(target_cities)]
print(filtered)
```

---

## 💡 Examples

### 1. Basic — Selecting one column and a few rows
```python
df = pd.read_csv("sales_data.csv")
print(df["price"])       # just the price column
print(df.iloc[0:5])        # first 5 rows
```

### 2. Analytics Use Case — Filtering for high-value customers
```python
high_value = df[df["total_spent"] > 10000]
print(high_value[["customer_name", "total_spent"]])
```

### 3. Combining loc with a condition
```python
result = df.loc[df["age"] > 30, ["name", "age"]]   # matching rows, only these columns
print(result)
```
*Explanation:* `.loc` can take a condition AND a column list at the same
time — very common in real filtering work.

### 4. Filtering with multiple conditions
```python
result = df[(df["age"] >= 25) & (df["age"] <= 35) & (df["city"] == "Mumbai")]
print(result)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Using single `[ ]` for multiple columns: `df["name", "age"]` | Use double brackets: `df[["name", "age"]]` |
| Using `and`/`or` for combining filter conditions | Use `&` and `\|`, with each condition wrapped in `()` |
| Confusing `.loc` (label-based) with `.iloc` (position-based) | `.loc` uses names/labels, `.iloc` uses numeric position |
| Forgetting `.loc` slicing includes the last item, unlike `.iloc` | `df.loc[0:2]` includes row 2; `df.iloc[0:2]` does not |

---

## ✍️ Practice Questions

1. What's the difference between `df["age"]` and `df[["age"]]`?
2. What's the difference between `.loc` and `.iloc`?
3. Write code to filter a DataFrame `df` for rows where `"salary"` is greater than 50000.
4. How would you select rows where `"city"` is either `"Delhi"` or `"Mumbai"`?
5. Why must you use `&` instead of `and` when combining conditions in Pandas?

<details>
<summary>💡 Click to see answers</summary>

1. `df["age"]` returns a **Series** (single column). `df[["age"]]` returns a
   **DataFrame** with just that one column (still a table, not a Series).
2. `.loc` selects using **labels** (row/column names). `.iloc` selects using
   **numeric positions**, similar to how Python lists work.
3. ```python
   high_earners = df[df["salary"] > 50000]
   ```
4. ```python
   result = df[df["city"].isin(["Delhi", "Mumbai"])]
   ```
5. Python's `and`/`or` are built for single `True`/`False` values, not for
   comparing entire columns element-by-element — Pandas (like NumPy)
   requires `&` and `|` for that, with each condition in parentheses.

</details>

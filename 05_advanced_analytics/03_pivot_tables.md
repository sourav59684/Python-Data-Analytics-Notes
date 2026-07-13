# 📊 Advanced Analytics — Pivot Tables

---

## 📌 What Is a Pivot Table?

A **pivot table** reorganizes your data — turning unique values from one
column into new column headers, and summarizing another column underneath
them. If you've ever used pivot tables in Excel, this is the exact same
idea, done in code.

```python
import pandas as pd

df = pd.DataFrame({
    "region": ["North", "North", "South", "South"],
    "product": ["A", "B", "A", "B"],
    "sales": [500, 700, 300, 900]
})

pivot = df.pivot_table(values="sales", index="region", columns="product", aggfunc="sum")
print(pivot)
```
```
product    A    B
region
North    500  700
South    300  900
```

---

## 📊 Why This Matters for Data Analytics

Pivot tables are one of the best ways to summarize data into a clear,
readable format — especially for reports and dashboards. "Sales by region
AND by product, side by side" is a classic pivot table question, and it's
far more readable than a long list of grouped rows.

---

## 🏗️ Pivot Table Structure

```python
df.pivot_table(
    values="column_to_summarize",
    index="column_for_rows",
    columns="column_for_new_columns",
    aggfunc="sum"    # or "mean", "count", etc.
)
```

| Parameter | Meaning |
|---|---|
| `values` | The column you want to summarize (numbers) |
| `index` | The column whose unique values become the **rows** |
| `columns` | The column whose unique values become the **new columns** |
| `aggfunc` | How to summarize (`"sum"`, `"mean"`, `"count"`, etc. — default is `"mean"`) |

---

## 🔧 Common Pivot Table Options

| Option | What It Does | Example |
|---|---|---|
| `aggfunc="sum"` | Totals per group | Most common for sales data |
| `aggfunc="mean"` | Average per group | Good for ratings, scores |
| `aggfunc="count"` | Counts entries per group | Good for "how many orders" |
| `fill_value=0` | Replaces empty cells (no data) with 0 instead of `NaN` | Cleaner output |
| `margins=True` | Adds a "Total" row and column | Quick grand totals |

```python
pivot = df.pivot_table(
    values="sales",
    index="region",
    columns="product",
    aggfunc="sum",
    fill_value=0,
    margins=True
)
print(pivot)
```
```
product    A    B   All
region
North    500  700  1200
South    300  900  1200
All      800 1600  2400
```

---

## 🆚 pivot_table vs. groupby

| | `.groupby()` | `.pivot_table()` |
|---|---|---|
| Output shape | Long, stacked format | Wide, spreadsheet-style format |
| Best for | Further calculations in code | Readable summaries and reports |

```python
# groupby (long format)
df.groupby(["region", "product"])["sales"].sum()

# pivot_table (wide format) — same data, easier to read at a glance
df.pivot_table(values="sales", index="region", columns="product", aggfunc="sum")
```

---

## 🔀 `pd.crosstab()` — Quick Counting Pivot

`crosstab` is a shortcut specifically for **counting** how often
combinations occur — no `values` or `aggfunc` needed.

```python
df = pd.DataFrame({
    "gender": ["M", "F", "F", "M", "F"],
    "purchased": ["Yes", "Yes", "No", "No", "Yes"]
})

print(pd.crosstab(df["gender"], df["purchased"]))
```
```
purchased  No  Yes
gender
F           1    2
M           1    1
```

---

## 💡 Examples

### 1. Basic — Average score by subject and class
```python
df = pd.DataFrame({
    "class": ["A", "A", "B", "B"],
    "subject": ["Math", "Science", "Math", "Science"],
    "score": [80, 90, 70, 85]
})

pivot = df.pivot_table(values="score", index="class", columns="subject")
print(pivot)
```

### 2. Analytics Use Case — Monthly sales by product, with totals
```python
pivot = df.pivot_table(
    values="sales",
    index="month",
    columns="product",
    aggfunc="sum",
    fill_value=0,
    margins=True
)
print(pivot)
```
*Explanation:* This is exactly the format you'd export straight into a
report — clean rows and columns, with grand totals already calculated.

### 3. Counting survey responses with crosstab
```python
responses = pd.DataFrame({
    "age_group": ["18-25", "26-35", "18-25", "36+"],
    "satisfied": ["Yes", "No", "Yes", "Yes"]
})

print(pd.crosstab(responses["age_group"], responses["satisfied"]))
```

### 4. Multiple values summarized at once
```python
pivot = df.pivot_table(
    values=["sales", "quantity"],
    index="region",
    aggfunc="sum"
)
print(pivot)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting `aggfunc` and getting an average when you wanted a sum | Default is `"mean"` — always specify `aggfunc="sum"` if that's what you need |
| Confusing `pivot_table` with `crosstab` | `crosstab` is specifically for counting combinations; `pivot_table` is for summarizing any numeric column |
| Not using `fill_value=0` and getting confusing `NaN` cells | Add `fill_value=0` for a cleaner, report-ready table |
| Using `pivot_table` when a simple `groupby` would be clearer for further code | Use `pivot_table` mainly for final, readable summaries — not mid-analysis calculations |

---

## ✍️ Practice Questions

1. What does a pivot table do, in your own words?
2. Write a pivot table showing total "sales" by "city" (rows) and "year" (columns).
3. What's the difference between `pivot_table` and `crosstab`?
4. What does `fill_value=0` do?
5. What does `margins=True` add to a pivot table?

<details>
<summary>💡 Click to see answers</summary>

1. A pivot table reorganizes data by turning one column's unique values into
   new column headers, and summarizing another column underneath them —
   creating an easy-to-read summary table.
2. ```python
   df.pivot_table(values="sales", index="city", columns="year", aggfunc="sum")
   ```
3. `pivot_table` summarizes any numeric column using a chosen function (sum,
   mean, etc.). `crosstab` is a simpler shortcut specifically for **counting**
   how often combinations of two columns occur.
4. It replaces empty/missing cells in the pivot table (where no data existed
   for that combination) with `0` instead of `NaN`.
5. It adds an extra "Total" row and column showing the grand totals across
   all categories.

</details>

# 🐼 Pandas — Sorting & Editing DataFrames

---

## 📌 What This Covers

Once you can select and filter data, the next step is **reorganizing** it
(sorting) and **modifying** it (adding, renaming, or removing columns).

```python
import pandas as pd
df = pd.DataFrame({
    "name": ["Ravi", "Anu", "Simran"],
    "score": [88, 95, 79]
})

df_sorted = df.sort_values("score")
print(df_sorted)
```

---

## 📊 Why This Matters for Data Analytics

Sorting is how you find your top performers, highest sales, or oldest
records. Editing columns — renaming confusing headers, adding calculated
fields, dropping columns you don't need — is a core part of shaping raw data
into something ready for analysis.

---

## 🔃 1. Sorting

### 🔧 Common Sorting Methods

| Method | What It Does | Example |
|---|---|---|
| `.sort_values("col")` | Sorts rows by a column's values | Ascending by default |
| `.sort_values("col", ascending=False)` | Sorts largest to smallest | Descending |
| `.sort_values(["col1", "col2"])` | Sorts by multiple columns | First by col1, ties broken by col2 |
| `.sort_index()` | Sorts by the row index/label | Restores original order after other sorts |

```python
df = pd.DataFrame({
    "name": ["Ravi", "Anu", "Simran", "Karan"],
    "score": [88, 95, 79, 95]
})

print(df.sort_values("score"))                       # ascending (lowest first)
print(df.sort_values("score", ascending=False))       # descending (highest first)
print(df.sort_values(["score", "name"], ascending=[False, True]))  # score desc, ties broken by name asc
```

> 💡 **`sort_values()` doesn't change the original DataFrame** unless you
> add `inplace=True`, or reassign it: `df = df.sort_values(...)`.

---

## ✏️ 2. Adding, Renaming, and Dropping Columns

### Adding a New Column

```python
df["bonus"] = df["score"] * 0.1     # a new calculated column
print(df)
```

```python
# Adding a column based on a condition
df["passed"] = df["score"] >= 60
print(df)
```

### Renaming Columns

```python
df = df.rename(columns={"score": "exam_score"})
print(df.columns)   # Index(['name', 'exam_score', 'bonus', 'passed'])
```

### Dropping (Removing) Columns or Rows

```python
df = df.drop(columns=["bonus"])          # drop a column
df = df.drop(index=[0])                   # drop a row by its label
```

### 🔧 Common Editing Methods

| Method | What It Does | Example |
|---|---|---|
| `df["new_col"] = ...` | Adds a new column | `df["total"] = df["price"] * df["qty"]` |
| `.rename(columns={...})` | Renames one or more columns | `df.rename(columns={"old":"new"})` |
| `.drop(columns=[...])` | Removes column(s) | `df.drop(columns=["unused_col"])` |
| `.drop(index=[...])` | Removes row(s) by label | `df.drop(index=[0, 1])` |
| `.rename(index={...})` | Renames row labels | Less common than renaming columns |

> ⚠️ **Most Pandas methods return a NEW DataFrame** by default — they don't
> change the original unless you reassign it (`df = df.rename(...)`) or use
> `inplace=True`.

---

## 💡 Examples

### 1. Basic — Sorting by a single column
```python
df = pd.DataFrame({
    "product": ["Pen", "Notebook", "Bag", "Bottle"],
    "price": [10, 40, 500, 150]
})

print(df.sort_values("price"))
```

### 2. Analytics Use Case — Finding the top 3 highest sales
```python
sorted_df = df.sort_values("price", ascending=False)
top_3 = sorted_df.head(3)
print(top_3)
```
*Explanation:* Sorting descending and then taking `.head(3)` is one of the
most common combinations in analytics — "show me the top N."

### 3. Adding a calculated column
```python
df["price_with_tax"] = df["price"] * 1.18
print(df)
```

### 4. Renaming and dropping columns for cleaner output
```python
df = df.rename(columns={"price": "unit_price"})
df = df.drop(columns=["price_with_tax"])
print(df.columns)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Expecting `.sort_values()` to change the original DataFrame automatically | Reassign it: `df = df.sort_values(...)`, or add `inplace=True` |
| Forgetting `columns=` inside `.rename()` | Must specify: `.rename(columns={"old": "new"})` |
| Dropping a column with `.drop("col")` without specifying `columns=` | Use `.drop(columns=["col"])` to avoid ambiguity with dropping rows |
| Assuming `ascending=False` sorts alphabetically the "wrong way" for text | It works the same for text too — Z to A instead of A to Z |

---

## ✍️ Practice Questions

1. How do you sort a DataFrame by "salary" from highest to lowest?
2. Write code to add a new column "total" as `price * quantity`.
3. How would you rename a column from "old_name" to "new_name"?
4. What happens if you run `df.sort_values("score")` without reassigning it to `df`?
5. How do you drop a column called "notes" from a DataFrame?

<details>
<summary>💡 Click to see answers</summary>

1. ```python
   df.sort_values("salary", ascending=False)
   ```
2. ```python
   df["total"] = df["price"] * df["quantity"]
   ```
3. ```python
   df = df.rename(columns={"old_name": "new_name"})
   ```
4. Nothing changes in `df` itself — `.sort_values()` returns a **new**,
   sorted DataFrame, but the original `df` stays exactly as it was unless
   you reassign it or use `inplace=True`.
5. ```python
   df = df.drop(columns=["notes"])
   ```

</details>

# 🧹 Data Cleaning — Duplicates

---

## 📌 What Are Duplicates?

**Duplicates** are rows that repeat the same information — often caused by
data entry errors, repeated form submissions, or merging data from multiple
sources. If left in place, they can inflate totals and skew averages.

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Ravi", "Anu", "Ravi", "Simran"],
    "age": [25, 30, 25, 28]
})
```
Here, row 0 and row 2 are exact duplicates.

---

## 📊 Why This Matters for Data Analytics

Duplicate rows silently distort your analysis — a customer counted twice
looks like two customers, a sale recorded twice inflates your revenue total.
Checking for and handling duplicates is a routine, essential step before any
serious analysis.

---

## 🔍 1. Finding Duplicates

### 🔧 Common Methods

| Method | What It Does | Example |
|---|---|---|
| `.duplicated()` | Returns True/False — True means this row is a repeat of an earlier one | `df.duplicated()` |
| `.duplicated().sum()` | Counts how many duplicate rows exist | `df.duplicated().sum()` |
| `.duplicated(subset=["col"])` | Checks duplicates based on specific column(s) only | `df.duplicated(subset=["name"])` |

```python
print(df.duplicated())
```
```
0    False
1    False
2     True    # this row matches row 0 exactly
3    False
dtype: bool
```

> 💡 **`.duplicated()` marks the SECOND (and later) occurrence as `True`.**
> The very first occurrence of a repeated row is always marked `False`.

```python
print(df.duplicated().sum())   # 1 → one duplicate row found
```

---

## 🗑️ 2. Removing Duplicates — `.drop_duplicates()`

```python
df_clean = df.drop_duplicates()
print(df_clean)
```

### 🔧 Common Options

| Option | What It Does | Example |
|---|---|---|
| `.drop_duplicates()` | Removes rows that are FULL duplicates | Default behavior |
| `.drop_duplicates(subset=["col"])` | Removes duplicates based on specific column(s) | `df.drop_duplicates(subset=["email"])` |
| `.drop_duplicates(keep="first")` | Keeps the first occurrence (default) | Standard behavior |
| `.drop_duplicates(keep="last")` | Keeps the last occurrence instead | Useful if later entries are more up-to-date |
| `.drop_duplicates(keep=False)` | Removes ALL copies, including the first one | Only keeps truly unique rows |

```python
# Treat rows as duplicates if the "email" matches, even if other columns differ
df_clean = df.drop_duplicates(subset=["email"], keep="last")
```

---

## 💡 Examples

### 1. Basic — Checking and removing exact duplicate rows
```python
df = pd.read_csv("customer_data.csv")
print("Duplicate rows found:", df.duplicated().sum())

df_clean = df.drop_duplicates()
print("Shape before:", df.shape)
print("Shape after:", df_clean.shape)
```

### 2. Analytics Use Case — Duplicate customers based on email only
```python
# Same customer, but maybe their name was typed slightly differently
df_clean = df.drop_duplicates(subset=["email"], keep="first")
```
*Explanation:* Full-row duplicate checks miss cases where only some fields
match. Checking a unique identifier like `email` or `customer_id` catches
duplicate customers even if other details (like name spelling) differ slightly.

### 3. Keeping the most recent record
```python
# Assuming the dataset is already sorted by date, oldest first
df_clean = df.drop_duplicates(subset=["customer_id"], keep="last")
```
*Explanation:* If a customer's info was updated and re-entered later,
`keep="last"` ensures you keep their most recent record instead of an
outdated one.

### 4. Finding duplicates before deciding how to handle them
```python
duplicate_rows = df[df.duplicated(keep=False)]   # shows BOTH copies of every duplicate
print(duplicate_rows)
```
*Explanation:* `keep=False` is useful specifically for *investigating*
duplicates — it shows every copy involved, not just the "extra" ones, so you
can inspect what happened before deciding how to clean them.

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Only checking full-row duplicates when a unique ID should be checked instead | Use `subset=["id_column"]` to catch duplicates based on a key field |
| Assuming `.duplicated()` marks ALL copies as True | It marks all copies **except the first** as `True` by default |
| Removing duplicates without checking how many rows you're losing | Compare `.shape` before and after |
| Not deciding `keep="first"` vs `keep="last"` intentionally | Think about which copy is more likely to be accurate/up to date |

---

## ✍️ Practice Questions

1. What does `.duplicated()` return?
2. How would you check for duplicate rows based only on the "email" column?
3. What's the difference between `keep="first"` and `keep="last"`?
4. Why might full-row duplicate checking miss real duplicate customers?
5. Write code to remove all duplicate rows from `df`, keeping the first occurrence.

<details>
<summary>💡 Click to see answers</summary>

1. It returns a `True`/`False` value for every row — `True` if that row is a
   repeat of an earlier row, `False` otherwise (including the first
   occurrence of any repeated row).
2. ```python
   df.duplicated(subset=["email"])
   ```
3. `keep="first"` keeps the first occurrence of a duplicate and marks later
   copies for removal. `keep="last"` does the opposite — keeps the last
   (often most recent) occurrence instead.
4. If any single field differs slightly (like a typo in the name, or a
   different date), a full-row comparison won't consider them duplicates,
   even though they represent the same real-world customer.
5. ```python
   df_clean = df.drop_duplicates(keep="first")
   ```

</details>

# 🐼 Pandas — DataFrame Basics

---

## 📌 What Is a DataFrame?

A **DataFrame** is Pandas' version of a spreadsheet or table — rows and
columns, where each column is actually a Series (from the previous file).

```python
import pandas as pd

data = {
    "name": ["Ravi", "Anu", "Simran"],
    "age": [25, 30, 28],
    "city": ["Mumbai", "Delhi", "Pune"]
}

df = pd.DataFrame(data)
print(df)
```
```
     name  age    city
0    Ravi   25  Mumbai
1     Anu   30   Delhi
2  Simran   28    Pune
```

> 💬 **Key idea:** Think of a DataFrame exactly like an Excel sheet — rows,
> columns, and column headers — except you control it entirely through code.

---

## 📊 Why This Matters for Data Analytics

The DataFrame is *the* central tool of data analytics in Python. Almost
every real task — cleaning, filtering, summarizing, visualizing — happens on
a DataFrame. Everything you learned in Python Foundations and NumPy has been
building up to working comfortably with this one structure.

---

## 🏗️ Creating a DataFrame

```python
import pandas as pd

# From a dictionary of lists (most common way)
data = {
    "product": ["Pen", "Notebook", "Bag"],
    "price": [10, 40, 500]
}
df = pd.DataFrame(data)

# From a list of lists, with column names specified
df2 = pd.DataFrame(
    [["Pen", 10], ["Notebook", 40], ["Bag", 500]],
    columns=["product", "price"]
)
```

### Reading Data from Files (the most common real-world way)

| Function | Reads From |
|---|---|
| `pd.read_csv("file.csv")` | A CSV file |
| `pd.read_excel("file.xlsx")` | An Excel file |
| `pd.read_json("file.json")` | A JSON file |
| `pd.read_sql(query, connection)` | A SQL database |

```python
df = pd.read_csv("sales_data.csv")
df = pd.read_excel("sales_data.xlsx", sheet_name="Sheet1")
```

### Writing Data Back Out

| Function | Saves To |
|---|---|
| `df.to_csv("output.csv", index=False)` | A CSV file |
| `df.to_excel("output.xlsx", index=False)` | An Excel file |

> 💡 **`index=False`** is important — without it, Pandas saves its own
> automatic row numbers as an extra column in your file, which usually isn't
> what you want.

---

## 🔧 Common DataFrame Attributes

| Attribute | What It Shows | Example |
|---|---|---|
| `.shape` | (rows, columns) | `(3, 2)` |
| `.columns` | List of column names | `Index(['product', 'price'])` |
| `.index` | The row labels | `RangeIndex(start=0, stop=3)` |
| `.dtypes` | Data type of every column | Shows int/float/object per column |
| `.values` | All the data as a NumPy array (no labels) | 2D array of raw values |

```python
print(df.shape)     # (3, 2)  → 3 rows, 2 columns
print(df.columns)   # Index(['product', 'price'], dtype='object')
print(df.dtypes)
```

---

## 💡 Examples

### 1. Basic — Creating a DataFrame from scratch
```python
import pandas as pd

data = {
    "student": ["Ravi", "Anu", "Simran", "Karan"],
    "score": [88, 92, 79, 95]
}
df = pd.DataFrame(data)
print(df)
```

### 2. Analytics Use Case — Loading a real CSV file
```python
df = pd.read_csv("sales_data.csv")
print(df.shape)       # how many rows and columns
print(df.columns)     # what columns are available
```
*Explanation:* This is usually the very first two lines of code in any real
analytics project — load the file, then check its size and structure before
doing anything else.

### 3. Accessing a Single Column (returns a Series!)
```python
df = pd.DataFrame({"name": ["Ravi", "Anu"], "age": [25, 30]})
ages = df["age"]
print(ages)
print(type(ages))   # <class 'pandas.core.series.Series'>
```
*Explanation:* This is the direct link back to the Series file — a single
DataFrame column IS a Series.

### 4. Saving a cleaned DataFrame back to a file
```python
df.to_csv("cleaned_sales.csv", index=False)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting `index=False` when saving to CSV | Adds an unwanted extra column of row numbers otherwise |
| Assuming column order in the dictionary controls display order | Pandas keeps the order you define, but be careful when merging from multiple sources |
| Using `df.column_name` instead of `df["column_name"]` for columns with spaces | `df["column name"]` always works; the dot version fails for names with spaces |
| Not checking `.shape` before starting analysis | Always confirm the size and structure of your data first |

---

## ✍️ Practice Questions

1. What is a DataFrame, in your own words?
2. Create a DataFrame with columns "item" and "quantity" for 3 items.
3. What does `df.shape` tell you?
4. What type of object do you get when you access a single column with `df["column"]`?
5. Why is `index=False` usually added when saving to CSV?

<details>
<summary>💡 Click to see answers</summary>

1. A DataFrame is a table of data — rows and columns, like a spreadsheet —
   made up of Pandas Series (one Series per column).
2. ```python
   df = pd.DataFrame({
       "item": ["Pen", "Notebook", "Eraser"],
       "quantity": [50, 30, 20]
   })
   ```
3. It shows the number of rows and columns as `(rows, columns)`.
4. A **Series** — a single DataFrame column is always a Series.
5. Without it, Pandas adds its own automatic row-number index as an extra
   unwanted column in the saved file.

</details>

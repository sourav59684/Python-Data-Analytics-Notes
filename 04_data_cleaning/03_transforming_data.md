# 🧹 Data Cleaning — Transforming Data

---

## 📌 What Does "Transforming Data" Mean?

**Transforming** means changing the values in a column — converting units,
fixing text formatting, applying custom logic to every row. This is how you
turn messy raw data into clean, usable data.

```python
import pandas as pd

df = pd.DataFrame({"price_text": ["199.99", "250", "89.50"]})
df["price"] = df["price_text"].astype(float)   # transform text into real numbers
```

---

## 📊 Why This Matters for Data Analytics

Real-world data rarely comes in exactly the shape you need. Prices come in
as text, names have inconsistent capitalization, dates are in the wrong
format. Transforming data is how you standardize everything before analysis
— and getting good at it means most cleaning tasks become one-liners.

---

## 🔧 1. `.apply()` — Running a Function on Every Value

`.apply()` runs a function (built-in, lambda, or your own custom one) on
every value in a column.

```python
def age_group(age):
    if age < 18:
        return "Minor"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

df["group"] = df["age"].apply(age_group)
```

```python
# Using a lambda for something simpler
df["price_with_tax"] = df["price"].apply(lambda x: x * 1.18)
```

---

## 🗺️ 2. `.map()` — Replacing Values Using a Function or a Dictionary

`.map()` works only on a single Series (column), and is especially handy
with a dictionary for direct value replacement.

```python
status_map = {"Y": "Active", "N": "Inactive"}
df["status"] = df["status_code"].map(status_map)
```

```python
# Also works with a function, similar to .apply()
df["price_doubled"] = df["price"].map(lambda x: x * 2)
```

| | `.apply()` | `.map()` |
|---|---|---|
| Works on | Series or entire DataFrame | Series only |
| Best for | Custom functions, row-wise logic | Simple value replacement (especially with a dict) |

---

## 🔤 3. String Cleaning with `.str`

Pandas has a `.str` accessor that lets you use string methods across an
entire column at once.

### 🔧 Common `.str` Methods

| Method | What It Does | Example |
|---|---|---|
| `.str.upper()` / `.str.lower()` | Changes case | `df["name"].str.upper()` |
| `.str.strip()` | Removes extra whitespace | `df["name"].str.strip()` |
| `.str.replace(old, new)` | Replaces text | `df["phone"].str.replace("-", "")` |
| `.str.contains("text")` | Checks if text appears — returns True/False | `df["email"].str.contains("@gmail")` |
| `.str.split(sep)` | Splits text into parts | `df["full_name"].str.split(" ")` |
| `.str.len()` | Length of each text value | `df["name"].str.len()` |

```python
df["name"] = df["name"].str.strip().str.title()   # clean spacing + fix capitalization

gmail_users = df[df["email"].str.contains("@gmail.com")]
```
*Explanation:* Chaining `.str.strip().str.title()` in one line is extremely
common — clean whitespace, then fix capitalization, all in one step across
the whole column.

---

## 🔁 4. Converting Data Types — `.astype()`

```python
df["price"] = df["price"].astype(float)
df["customer_id"] = df["customer_id"].astype(str)
```

```python
# Safer conversion that handles errors gracefully
df["price"] = pd.to_numeric(df["price"], errors="coerce")   # invalid values become NaN instead of crashing
```

| Function | Best For |
|---|---|
| `.astype(type)` | Clean data, when you're sure the conversion will work |
| `pd.to_numeric(col, errors="coerce")` | Messy numeric columns — invalid values become `NaN` instead of an error |
| `pd.to_datetime(col)` | Converting text into real dates |

---

## 💡 Examples

### 1. Basic — Cleaning messy text
```python
df = pd.DataFrame({"city": ["  mumbai", "DELHI ", "Pune"]})
df["city"] = df["city"].str.strip().str.title()
print(df)
```
```
     city
0   Mumbai
1    Delhi
2     Pune
```

### 2. Analytics Use Case — Converting a "dirty" numeric column safely
```python
df = pd.DataFrame({"votes": ["1200", "850", "N/A", "2000"]})
df["votes"] = pd.to_numeric(df["votes"], errors="coerce")
print(df)
```
```
    votes
0  1200.0
1   850.0
2     NaN
3  2000.0
```
*Explanation:* `errors="coerce"` means any value that can't be converted
(like `"N/A"`) becomes `NaN` instead of crashing your entire script.

### 3. Applying custom logic with `.apply()`
```python
def categorize_sales(amount):
    if amount >= 1000:
        return "High"
    elif amount >= 500:
        return "Medium"
    else:
        return "Low"

df["category"] = df["sales"].apply(categorize_sales)
```

### 4. Replacing coded values with readable labels using `.map()`
```python
gender_map = {"M": "Male", "F": "Female"}
df["gender"] = df["gender_code"].map(gender_map)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Using `.astype(float)` on messy data with invalid entries | Use `pd.to_numeric(col, errors="coerce")` instead — safer |
| Forgetting `.str` before string methods on a column | `df["name"].upper()` fails — must be `df["name"].str.upper()` |
| Using `.map()` for row-wise logic involving multiple columns | `.map()` only works on a single column — use `.apply()` with `axis=1` for row-wise logic |
| Applying a complex function inline as an unreadable lambda | Define a named function with `def` if the logic has more than one step |

---

## ✍️ Practice Questions

1. What's the difference between `.apply()` and `.map()`?
2. Write code to convert a column "score_text" to numbers, safely handling invalid entries.
3. How would you remove extra whitespace and capitalize the first letter of every word in a "city" column?
4. What does `pd.to_numeric(col, errors="coerce")` do with invalid values?
5. Write a `.map()` example that converts `"Y"`/`"N"` into `"Yes"`/`"No"`.

<details>
<summary>💡 Click to see answers</summary>

1. `.apply()` can run more complex, custom functions and works on both
   Series and DataFrames. `.map()` only works on a single Series and is
   especially convenient for direct value replacement using a dictionary.
2. ```python
   df["score"] = pd.to_numeric(df["score_text"], errors="coerce")
   ```
3. ```python
   df["city"] = df["city"].str.strip().str.title()
   ```
4. It converts any value it can't turn into a number into `NaN`, instead of
   raising an error and stopping your code.
5. ```python
   df["answer"] = df["answer_code"].map({"Y": "Yes", "N": "No"})
   ```

</details>

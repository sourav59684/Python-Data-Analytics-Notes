# 📊 Advanced Analytics — GroupBy & Aggregation

---

## 📌 What Is GroupBy?

**GroupBy** lets you split your data into groups based on a column, then
calculate something for each group separately — like "total sales per
city" or "average score per class."

```python
import pandas as pd

df = pd.DataFrame({
    "city": ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi"],
    "sales": [1200, 800, 1500, 600, 900]
})

city_totals = df.groupby("city")["sales"].sum()
print(city_totals)
```
```
city
Delhi     1700
Mumbai    2700
Pune       600
Name: sales, dtype: int64
```

> 💬 **The idea in 3 steps:** **Split** the data into groups (by city) →
> **Apply** a calculation to each group (sum) → **Combine** the results back
> into one output. This is called "split-apply-combine," and it's the
> foundation of almost all real data analysis.

---

## 📊 Why This Matters for Data Analytics

Nearly every business question is really a groupby question: "sales by
region," "average rating by product category," "signups by month." GroupBy
is one of the single most important tools you'll use as a data analyst.

---

## 🏗️ GroupBy Structure

```
df.groupby("column_to_group_by")["column_to_calculate"].function()
```

```python
# Group by one column, calculate on one column
avg_by_city = df.groupby("city")["sales"].mean()

# Group by multiple columns
df.groupby(["city", "product"])["sales"].sum()

# Multiple calculations at once
df.groupby("city")["sales"].agg(["sum", "mean", "count"])
```

---

## 🔧 Common Aggregation Functions

| Function | What It Calculates |
|---|---|
| `.sum()` | Total |
| `.mean()` | Average |
| `.count()` | Number of non-missing values |
| `.min()` / `.max()` | Smallest / largest value |
| `.median()` | Middle value |
| `.std()` | Standard deviation |
| `.nunique()` | Number of unique values |
| `.agg([...])` | Run MULTIPLE functions at once |

```python
summary = df.groupby("city")["sales"].agg(["sum", "mean", "max"])
print(summary)
```
```
        sum    mean   max
city
Delhi   1700   850.0  900
Mumbai  2700  1350.0 1500
Pune     600   600.0  600
```

### Custom Named Aggregations

```python
summary = df.groupby("city").agg(
    total_sales=("sales", "sum"),
    average_sales=("sales", "mean"),
    number_of_orders=("sales", "count")
)
print(summary)
```
*Explanation:* Named aggregation lets you rename the resulting columns
directly — much cleaner output than the default column names.

---

## 💡 Examples

### 1. Basic — Total sales per city
```python
df = pd.DataFrame({
    "city": ["Mumbai", "Delhi", "Mumbai", "Pune"],
    "sales": [1200, 800, 1500, 600]
})
print(df.groupby("city")["sales"].sum())
```

### 2. Analytics Use Case — Average order value per customer segment
```python
df = pd.read_csv("orders.csv")
segment_avg = df.groupby("customer_segment")["order_value"].mean()
print(segment_avg.sort_values(ascending=False))
```
*Explanation:* Sorting the result right after grouping is extremely common
— instantly shows you which segment spends the most.

### 3. Grouping by multiple columns
```python
df = pd.DataFrame({
    "region": ["North", "North", "South", "South"],
    "product": ["A", "B", "A", "B"],
    "sales": [500, 700, 300, 900]
})

result = df.groupby(["region", "product"])["sales"].sum()
print(result)
```
```
region  product
North   A          500
        B          700
South   A          300
        B          900
Name: sales, dtype: int64
```

### 4. Multiple aggregations with clean, named columns
```python
summary = df.groupby("region").agg(
    total_sales=("sales", "sum"),
    order_count=("sales", "count")
)
print(summary)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting to specify which column to calculate on | `df.groupby("city")["sales"].sum()`, not just `df.groupby("city").sum()` on a large DataFrame |
| Assuming `.groupby()` alone returns visible results | Nothing prints until you chain a calculation like `.sum()` or `.mean()` on it |
| Confusing `.agg(["sum","mean"])` with named aggregation syntax | Use `.agg(new_name=("column","function"))` for renamed output columns |
| Not sorting grouped results when order matters | Chain `.sort_values()` right after the groupby calculation |

---

## ✍️ Practice Questions

1. What does "split-apply-combine" mean?
2. Write code to find the average "price" grouped by "category".
3. How would you calculate both the sum AND count of "sales" grouped by "region" in one line?
4. What's the benefit of named aggregation (`total_sales=("sales","sum")`)?
5. Given sales data grouped by month, how would you find the month with the highest total sales?

<details>
<summary>💡 Click to see answers</summary>

1. It's the 3-step process behind groupby: **split** the data into groups,
   **apply** a calculation to each group separately, then **combine** the
   results into one final output.
2. ```python
   df.groupby("category")["price"].mean()
   ```
3. ```python
   df.groupby("region")["sales"].agg(["sum", "count"])
   ```
4. It lets you directly control and clean up the output column names,
   instead of getting Pandas' default (sometimes less readable) naming.
5. ```python
   monthly_sales = df.groupby("month")["sales"].sum()
   print(monthly_sales.idxmax())   # returns the month with the highest total
   ```

</details>

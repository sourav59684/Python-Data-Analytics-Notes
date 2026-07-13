# 📊 Advanced Analytics — Combining Data (merge, join, concat)

---

## 📌 Why Combine Data?

Real-world data often lives in separate tables — customers in one file,
orders in another. To analyze them together (e.g., "show each order with
the customer's name"), you need to combine them. Pandas gives you three main
tools: **merge**, **join**, and **concat**.

```python
import pandas as pd

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "name": ["Ravi", "Anu", "Simran"]
})

orders = pd.DataFrame({
    "customer_id": [1, 2, 1],
    "amount": [500, 800, 300]
})

combined = pd.merge(customers, orders, on="customer_id")
print(combined)
```
```
   customer_id    name  amount
0            1    Ravi     500
1            1    Ravi     300
2            2     Anu     800
```

---

## 📊 Why This Matters for Data Analytics

Almost no real analysis uses just one table. You'll constantly combine
customer info with order history, product details with sales records,
survey responses with demographic data. Knowing how to combine tables
correctly (and avoiding accidental duplicate rows) is essential.

---

## 🔗 1. `pd.merge()` — Combining Based on a Shared Column

This is like a SQL JOIN — it matches rows between two tables based on a
common column (a "key").

### 🔧 Types of Merge

| Type | Keeps |
|---|---|
| `how="inner"` (default) | Only rows that match in BOTH tables |
| `how="left"` | All rows from the left table, matched data where available |
| `how="right"` | All rows from the right table, matched data where available |
| `how="outer"` | ALL rows from both tables, filling gaps with `NaN` |

```python
# Inner join (default) — only customers WITH orders appear
pd.merge(customers, orders, on="customer_id", how="inner")

# Left join — ALL customers appear, even ones with no orders (amount = NaN)
pd.merge(customers, orders, on="customer_id", how="left")
```

```
Inner Join                    Left Join
┌─────────┐   ┌─────────┐    ┌─────────┐   ┌─────────┐
│  Table  │   │  Table  │    │  Table  │   │  Table  │
│    A    │ ∩ │    B    │    │    A    │ + │  B (if  │
│         │   │         │    │ (ALL)   │   │ matched)│
└─────────┘   └─────────┘    └─────────┘   └─────────┘
Only matches                  All of A, matched B or NaN
```

---

## 🔗 2. `.join()` — Combining Based on the Index

`.join()` is similar to merge, but combines tables using their **row index**
instead of a shared column (useful when the index already lines up).

```python
df1 = pd.DataFrame({"score": [88, 92]}, index=["Ravi", "Anu"])
df2 = pd.DataFrame({"grade": ["B", "A"]}, index=["Ravi", "Anu"])

result = df1.join(df2)
print(result)
```
```
      score grade
Ravi     88     B
Anu      92     A
```

---

## 📚 3. `pd.concat()` — Stacking Tables Together

`concat` simply stacks DataFrames — either on top of each other (more rows)
or side-by-side (more columns). It doesn't match on any key; it just combines.

```python
jan_sales = pd.DataFrame({"product": ["Pen", "Bag"], "sales": [100, 200]})
feb_sales = pd.DataFrame({"product": ["Pen", "Bag"], "sales": [150, 250]})

all_sales = pd.concat([jan_sales, feb_sales])
print(all_sales)
```
```
  product  sales
0     Pen    100
1     Bag    200
0     Pen    150
1     Bag    250
```

> 💡 **Notice the repeated index (0, 1, 0, 1).** Add `ignore_index=True` to
> get a clean, continuous index: `pd.concat([jan_sales, feb_sales], ignore_index=True)`

### 🔧 Common `concat` Options

| Option | What It Does |
|---|---|
| `pd.concat([df1, df2])` | Stacks rows (default, `axis=0`) |
| `pd.concat([df1, df2], axis=1)` | Stacks columns side-by-side |
| `pd.concat([df1, df2], ignore_index=True)` | Resets the index cleanly |

---

## 🆚 merge vs. join vs. concat — Quick Reference

| Tool | Combines Based On | Best For |
|---|---|---|
| `pd.merge()` | A shared column (like a SQL join) | Combining related tables (customers + orders) |
| `.join()` | The row index | Quick combining when indexes already line up |
| `pd.concat()` | Just stacking, no matching | Combining monthly files, or the same structure repeated |

---

## 💡 Examples

### 1. Basic — Merging two related tables
```python
products = pd.DataFrame({"product_id": [1, 2], "name": ["Pen", "Bag"]})
sales = pd.DataFrame({"product_id": [1, 1, 2], "amount": [10, 15, 20]})

merged = pd.merge(products, sales, on="product_id")
print(merged)
```

### 2. Analytics Use Case — Keeping all customers, even those without orders
```python
result = pd.merge(customers, orders, on="customer_id", how="left")
print(result)   # customers with no orders show NaN in the "amount" column
```
*Explanation:* A `left` join is extremely common in analytics — "show me
every customer, and their order info if they have any" — instead of
accidentally dropping customers who haven't ordered yet.

### 3. Combining monthly sales files into one dataset
```python
jan = pd.read_csv("jan_sales.csv")
feb = pd.read_csv("feb_sales.csv")
mar = pd.read_csv("mar_sales.csv")

full_year_so_far = pd.concat([jan, feb, mar], ignore_index=True)
print(full_year_so_far.shape)
```

### 4. Merging on differently-named columns
```python
customers = pd.DataFrame({"cust_id": [1, 2], "name": ["Ravi", "Anu"]})
orders = pd.DataFrame({"customer_id": [1, 2], "amount": [500, 800]})

merged = pd.merge(customers, orders, left_on="cust_id", right_on="customer_id")
print(merged)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Using the default `inner` merge and losing unmatched rows silently | Use `how="left"` or `how="outer"` when you need to keep unmatched rows |
| Using `pd.concat()` when you actually need to match on a key | `concat` just stacks — use `merge` when rows need to be matched up correctly |
| Forgetting `ignore_index=True` and ending up with duplicate index values | Add it when stacking multiple DataFrames together |
| Not checking row count after merging (accidental row duplication) | Compare `.shape` before and after — a mismatched key can create duplicate rows |

---

## ✍️ Practice Questions

1. What's the difference between `pd.merge()` and `pd.concat()`?
2. What does a "left" join keep that an "inner" join might drop?
3. Write code to combine `df1` and `df2` (same columns) into one DataFrame with a clean index.
4. When would you use `.join()` instead of `.merge()`?
5. If merging on columns with different names in each table, which merge arguments do you use?

<details>
<summary>💡 Click to see answers</summary>

1. `pd.merge()` combines tables by matching values in a shared column (like
   a SQL join). `pd.concat()` simply stacks tables together (rows or
   columns) without matching on any key.
2. A "left" join keeps **all rows from the left table**, even if there's no
   match in the right table (filling missing info with `NaN`). An "inner"
   join only keeps rows that have a match in both tables.
3. ```python
   combined = pd.concat([df1, df2], ignore_index=True)
   ```
4. When the two DataFrames already share the same row index and you just
   want to combine columns quickly, without needing the full flexibility of `merge()`.
5. `left_on="column_name_in_left_table"` and `right_on="column_name_in_right_table"`.

</details>

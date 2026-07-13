# 🔢 NumPy — Indexing, Slicing & Boolean Masking

---

## 📌 What Is Indexing & Slicing?

**Indexing** means grabbing a single item from an array using its position.
**Slicing** means grabbing a *range* of items at once.

Counting positions in Python always starts at **0**, not 1.

```python
import numpy as np
scores = np.array([88, 92, 79, 95, 60])

print(scores[0])   # 88 → the first item
print(scores[2])   # 79 → the third item
```

---

## 📊 Why This Matters for Data Analytics

Indexing and slicing are how you pull out specific rows, specific values, or
subsets of your data — "give me the first 5 rows," "give me only the values
above 100." This is the exact foundation for how you'll filter and select
data in Pandas DataFrames later.

---

## 🔎 1. Basic Indexing

```python
data = np.array([10, 20, 30, 40, 50])

print(data[0])     # 10  → first item
print(data[-1])     # 50  → last item (negative counts from the end)
print(data[-2])     # 40  → second-to-last item
```

| Index | Meaning |
|---|---|
| `data[0]` | First item |
| `data[-1]` | Last item |
| `data[1]` | Second item |
| `data[-2]` | Second-to-last item |

### Indexing a 2D Array (rows and columns)

```python
grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(grid[0])        # [1 2 3]  → the whole first row
print(grid[1, 2])      # 6        → row 1, column 2
print(grid[0][1])      # 2        → row 0, column 1 (alternate syntax)
```

---

## ✂️ 2. Slicing — Grabbing a Range

```
array[start:stop]        # from start up to (not including) stop
array[start:stop:step]   # with a step size
```

```python
data = np.array([10, 20, 30, 40, 50, 60])

print(data[1:4])     # [20 30 40]  → index 1 up to (not including) 4
print(data[:3])       # [10 20 30]  → from the beginning up to index 3
print(data[3:])       # [40 50 60]  → from index 3 to the end
print(data[::2])      # [10 30 50]  → every 2nd item
print(data[::-1])     # [60 50 40 30 20 10]  → reversed
```

| Slice | Meaning |
|---|---|
| `[1:4]` | Items at index 1, 2, 3 (stop is excluded) |
| `[:3]` | From the start up to index 3 |
| `[3:]` | From index 3 to the end |
| `[::2]` | Every 2nd item |
| `[::-1]` | The whole array, reversed |

### Slicing a 2D Array

```python
grid = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(grid[:2])          # first 2 rows
print(grid[:, 0])         # first column of every row → [1 4 7]
print(grid[0:2, 1:3])     # rows 0-1, columns 1-2
```

---

## ✅ 3. Boolean Masking — Filtering with Conditions

This is one of the most useful NumPy features for data analytics: pulling
out only the values that meet a condition.

```python
sales = np.array([1200, 800, 1500, 300, 2000])

mask = sales > 1000
print(mask)              # [ True False  True False  True]

high_sales = sales[mask]
print(high_sales)        # [1200 1500 2000]

# or do it in one line
high_sales = sales[sales > 1000]
print(high_sales)        # [1200 1500 2000]
```
*Explanation:* `sales > 1000` creates a `True`/`False` array (a "mask").
Using that mask inside `[ ]` keeps only the values where it's `True`. This
exact pattern is how you'll filter rows in a Pandas DataFrame later.

### 🔧 Common Filtering Patterns

| Pattern | What It Does | Example |
|---|---|---|
| `arr[arr > x]` | Keep values greater than `x` | `sales[sales > 1000]` |
| `arr[arr == x]` | Keep values equal to `x` | `scores[scores == 100]` |
| `arr[(arr > x) & (arr < y)]` | Keep values in a range (use `&` not `and`) | `sales[(sales > 500) & (sales < 1500)]` |
| `np.where(condition)` | Get the *positions* where a condition is true | `np.where(sales > 1000)` |

> ⚠️ **Use `&` and `|`, not `and`/`or`, with NumPy arrays.** Python's
> `and`/`or` don't work correctly on arrays — always use `&` (and), `|` (or)
> with parentheses around each condition.

---

## 💡 Examples

### 1. Basic — Grabbing specific values
```python
temperatures = np.array([22, 25, 19, 30, 28])
print(temperatures[1])    # 25
print(temperatures[-1])   # 28
```

### 2. Slicing a range of days
```python
week_sales = np.array([500, 700, 650, 800, 900, 1200, 1000])
first_half = week_sales[:4]     # first 4 days
weekend = week_sales[5:]         # Sat, Sun
print(first_half)   # [500 700 650 800]
print(weekend)       # [1200 1000]
```

### 3. Analytics Use Case — Filtering underperforming products
```python
product_sales = np.array([1200, 300, 1500, 200, 2000, 150])
underperforming = product_sales[product_sales < 500]
print(underperforming)   # [300 200 150]
```

### 4. Combining Multiple Conditions
```python
scores = np.array([45, 78, 92, 60, 55, 88])
mid_range = scores[(scores >= 50) & (scores <= 80)]
print(mid_range)   # [78 60 55]
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Thinking index counting starts at 1 | It starts at **0** — `array[0]` is the first item |
| Expecting `array[1:4]` to include index 4 | The `stop` index is always excluded |
| Using `and`/`or` with array conditions | Use `&` and `\|` instead, with each condition in parentheses |
| Forgetting `,` for 2D indexing (`grid[1][2]` vs `grid[1,2]`) | Both work, but `grid[1,2]` is the standard NumPy way |
| Modifying a slice and being surprised the original array changed | Slices are *views*, not copies — use `.copy()` if you need an independent copy |

---

## ✍️ Practice Questions

1. Given `arr = np.array([5, 10, 15, 20, 25])`, what does `arr[1:3]` return?
2. What does `arr[::-1]` do?
3. Write code to filter an array `nums` to keep only values greater than 50.
4. Why can't you use `and`/`or` for combining conditions on NumPy arrays?
5. Given a 2D array `grid`, how would you grab just the first column of every row?

<details>
<summary>💡 Click to see answers</summary>

1. `[10, 15]` — index 1 and 2 (index 3 is excluded).
2. It reverses the entire array.
3. ```python
   filtered = nums[nums > 50]
   ```
4. `and`/`or` are designed to work on single `True`/`False` values, not on
   entire arrays of them — NumPy requires `&` and `|` (with parentheses
   around each condition) to compare element-by-element correctly.
5. ```python
   grid[:, 0]
   ```

</details>

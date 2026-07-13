# 🔢 NumPy — Reshaping, Stacking & Splitting

---

## 📌 What Is Reshaping?

**Reshaping** means changing the *layout* of an array — how many rows and
columns it has — without changing the actual data or the number of values.

```python
import numpy as np

numbers = np.arange(1, 7)     # [1 2 3 4 5 6]
grid = numbers.reshape(2, 3)   # reshape into 2 rows, 3 columns

print(grid)
# [[1 2 3]
#  [4 5 6]]
```

> 💬 **Key idea:** Reshaping doesn't add or remove data — it just rearranges
> the same values into a different shape. The total number of values must
> stay the same (6 numbers → 2×3 = 6 slots, that works; 2×4 = 8 would error).

---

## 📊 Why This Matters for Data Analytics

Data doesn't always arrive in the shape you need. You might get one long
list of values that actually represents a table (rows and columns), or you
might need to flatten a table into one list for a specific calculation.
Reshaping is how you fix the "shape mismatch" between raw data and the
structure you actually need to work with.

---

## 🏗️ 1. Reshape & Flatten

### 🔧 Common Reshaping Methods

| Method | What It Does | Example |
|---|---|---|
| `.reshape(rows, cols)` | Changes the array's shape | `arr.reshape(2, 3)` |
| `.flatten()` | Turns any array back into a single flat 1D array | `grid.flatten()` |
| `.T` | Transposes — flips rows and columns | `grid.T` |
| `-1` in reshape | "Figure this dimension out automatically" | `arr.reshape(-1, 1)` |

```python
data = np.array([1, 2, 3, 4, 5, 6])

reshaped = data.reshape(3, 2)   # 3 rows, 2 columns
print(reshaped)
# [[1 2]
#  [3 4]
#  [5 6]]

flat_again = reshaped.flatten()
print(flat_again)   # [1 2 3 4 5 6]
```

### Using `-1` to Let NumPy Figure Out a Dimension

```python
data = np.arange(1, 13)         # 12 numbers
grid = data.reshape(3, -1)       # "3 rows, and figure out the columns yourself"
print(grid.shape)                 # (3, 4) → NumPy calculated 4 columns automatically
```
*Explanation:* `-1` is a convenience — useful when you know how many rows
you want but don't want to manually calculate the columns.

### Transposing (Flipping Rows and Columns)

```python
grid = np.array([[1, 2, 3], [4, 5, 6]])
print(grid.T)
# [[1 4]
#  [2 5]
#  [3 6]]
```

---

## 🧩 2. Stacking — Combining Arrays

| Function | What It Does | Example |
|---|---|---|
| `np.vstack([a, b])` | Stacks arrays **vertically** (adds rows) | Combine two arrays as new rows |
| `np.hstack([a, b])` | Stacks arrays **horizontally** (adds columns) | Combine two arrays side-by-side |
| `np.concatenate([a, b])` | General-purpose joining of arrays | Works for both directions with `axis=` |

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(np.vstack([a, b]))
# [[1 2 3]
#  [4 5 6]]

print(np.hstack([a, b]))
# [1 2 3 4 5 6]
```

---

## ✂️ 3. Splitting — Breaking an Array Apart

| Function | What It Does | Example |
|---|---|---|
| `np.split(arr, n)` | Splits an array into `n` equal parts | `np.split(arr, 3)` |
| `np.hsplit(arr, n)` | Splits horizontally (columns) | For 2D arrays |
| `np.vsplit(arr, n)` | Splits vertically (rows) | For 2D arrays |

```python
data = np.arange(1, 11)   # 10 numbers
parts = np.split(data, 5)   # split into 5 equal chunks of 2
print(parts)
# [array([1, 2]), array([3, 4]), array([5, 6]), array([7, 8]), array([9, 10])]
```

---

## 💡 Examples

### 1. Basic — Reshaping a list of scores into a grid
```python
scores = np.arange(1, 13)
grid = scores.reshape(4, 3)   # 4 students, 3 test scores each
print(grid)
```

### 2. Analytics Use Case — Reshaping before feeding into a calculation
```python
# Imagine 1 long list of sales figures for 3 stores, 4 weeks each
raw_sales = np.array([200,220,250,270, 300,310,290,320, 150,180,175,190])
store_sales = raw_sales.reshape(3, 4)   # 3 stores, 4 weeks

weekly_totals = store_sales.sum(axis=0)   # sum down each column (across stores)
store_totals = store_sales.sum(axis=1)    # sum across each row (per store)

print("Weekly totals:", weekly_totals)
print("Store totals:", store_totals)
```
*Explanation:* `axis=0` sums **down columns**, `axis=1` sums **across rows**
— this exact `axis` concept comes back constantly in Pandas.

### 3. Flattening a table back to a list
```python
grid = np.array([[1, 2], [3, 4], [5, 6]])
flat = grid.flatten()
print(flat)   # [1 2 3 4 5 6]
```

### 4. Stacking two arrays together
```python
week1 = np.array([100, 150, 200])
week2 = np.array([120, 130, 210])

combined = np.vstack([week1, week2])
print(combined)
# [[100 150 200]
#  [120 130 210]]
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Reshaping into a size that doesn't match the total values | Rows × columns must equal the total number of elements, or it errors |
| Confusing `.flatten()` with `.reshape()` | `.flatten()` always returns 1D; `.reshape()` lets you pick any valid shape |
| Mixing up `axis=0` and `axis=1` | `axis=0` = down the columns, `axis=1` = across the rows |
| Forgetting reshape doesn't change the data, only the layout | The values stay exactly the same — only their arrangement changes |

---

## ✍️ Practice Questions

1. Given 8 numbers, what shapes could you reshape them into?
2. What does `.flatten()` do?
3. What's the difference between `np.vstack()` and `np.hstack()`?
4. Given a 2D array `sales` of shape (3, 4), what does `sales.sum(axis=1)` calculate?
5. Why might you use `-1` inside `.reshape()`?

<details>
<summary>💡 Click to see answers</summary>

1. Any shape where rows × columns = 8: `(1,8)`, `(2,4)`, `(4,2)`, `(8,1)`.
2. It converts any shaped array back into a single flat 1D array.
3. `np.vstack()` stacks arrays **vertically** (as new rows). `np.hstack()`
   stacks them **horizontally** (as new columns, side by side).
4. It sums **across each row** — giving you one total per row (e.g., total
   per store, if each row represents a store).
5. To let NumPy automatically calculate that dimension for you, so you don't
   have to manually work out the exact number.

</details>

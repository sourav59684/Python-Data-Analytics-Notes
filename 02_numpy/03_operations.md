# 🔢 NumPy — Operations, Vectorization & Broadcasting

---

## 📌 What Is Vectorization?

**Vectorization** means applying an operation to an entire array at once,
instead of looping through it item by item. This is the whole reason NumPy
is fast.

```python
import numpy as np

prices = np.array([100, 200, 300])

# ❌ The slow way — looping manually
discounted = []
for p in prices:
    discounted.append(p * 0.9)

# ✅ The vectorized way — one line, no loop needed
discounted = prices * 0.9
print(discounted)   # [ 90. 180. 270.]
```

---

## 📊 Why This Matters for Data Analytics

Real datasets can have millions of rows. Looping through each one manually
in Python is slow. Vectorized operations let NumPy (and Pandas, built on top
of it) apply a calculation to an entire column instantly — this is *the*
reason data analysts use these libraries instead of plain Python loops.

---

## ➕ 1. Basic Arithmetic on Arrays

Every arithmetic operator works element-by-element automatically.

```python
a = np.array([1, 2, 3])
b = np.array([10, 20, 30])

print(a + b)    # [11 22 33]
print(a - b)    # [ -9 -18 -27]
print(a * b)    # [10 40 90]
print(b / a)    # [10. 10. 10.]
print(a ** 2)   # [1 4 9]
```
*Explanation:* Notice each operation happens **position by position** — the
first item of `a` with the first item of `b`, and so on.

---

## 📡 2. Broadcasting — Operating on Different Shapes

**Broadcasting** is NumPy's rule for how to combine arrays of *different*
shapes — most commonly, a whole array combined with a single number.

```python
prices = np.array([100, 200, 300])
tax_rate = 0.18   # just a single number, not an array

total = prices + (prices * tax_rate)
print(total)   # [118. 236. 354.]
```
*Explanation:* NumPy automatically "stretches" the single number (`0.18`) to
match every item in the array — you never had to write a loop.

```
Array:        [100, 200, 300]
Single value:  0.18   -->  stretched to  [0.18, 0.18, 0.18]
Result:       [18.0, 36.0, 54.0]
```

### Broadcasting Rule of Thumb

| Combination | Works? |
|---|---|
| Array + single number | ✅ Always works |
| Array + array of the same shape | ✅ Works, item-by-item |
| Array + array of a *different, incompatible* shape | ❌ Error |

```python
a = np.array([1, 2, 3])
b = np.array([1, 2])
# a + b   # ❌ This would raise a ValueError — shapes (3,) and (2,) don't match
```

---

## 📈 3. Mathematical & Statistical Functions

### 🔧 Common Aggregate Functions

| Function | What It Does | Example |
|---|---|---|
| `.sum()` | Adds up all values | `arr.sum()` |
| `.mean()` | Average | `arr.mean()` |
| `.max()` / `.min()` | Largest / smallest value | `arr.max()` |
| `.std()` | Standard deviation (spread of the data) | `arr.std()` |
| `.median()` — via `np.median(arr)` | Middle value | `np.median(arr)` |
| `.argmax()` / `.argmin()` | Position of the largest/smallest value | `arr.argmax()` |
| `np.sqrt(arr)` | Square root of every value | `np.sqrt([4, 9, 16])` → `[2. 3. 4.]` |
| `np.round(arr, n)` | Rounds every value to `n` decimals | `np.round(arr, 2)` |

```python
sales = np.array([1200, 800, 1500, 300, 2000])

print(sales.sum())      # 5800
print(sales.mean())     # 1160.0
print(sales.max())      # 2000
print(sales.std())      # spread of the sales values
print(sales.argmax())   # 4 → the position of the highest value
```

---

## 💡 Examples

### 1. Basic — Applying a discount to every price
```python
prices = np.array([500, 1000, 1500, 2000])
discounted = prices - (prices * 0.10)
print(discounted)   # [ 450.  900. 1350. 1800.]
```

### 2. Analytics Use Case — Quick statistics summary
```python
exam_scores = np.array([88, 92, 79, 95, 60, 73, 85])

print("Average:", exam_scores.mean())
print("Highest:", exam_scores.max())
print("Lowest:", exam_scores.min())
print("Std Dev:", round(exam_scores.std(), 2))
```
*Explanation:* This is a preview of exactly what `.describe()` will do
automatically for an entire DataFrame once you reach Pandas.

### 3. Vectorization vs. Loop — Speed comparison in concept
```python
import numpy as np

numbers = np.arange(1, 1000001)   # 1 million numbers

# Vectorized — fast, one line
squared = numbers ** 2

# Looping manually would take noticeably longer for the same result
```
*Explanation:* On large datasets, vectorized NumPy operations can be 10-100x
faster than a plain Python `for` loop doing the same math.

### 4. Broadcasting with a 2D array
```python
grades = np.array([
    [80, 90, 70],
    [60, 85, 95]
])

curved = grades + 5    # add 5 bonus points to every single value
print(curved)
# [[85 95 75]
#  [65 90 100]]
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Looping through arrays manually out of habit | Use vectorized operations (`arr * 2`) instead — faster and shorter |
| Assuming two arrays of different shapes always combine | Broadcasting only works if shapes are compatible — mismatched shapes raise an error |
| Forgetting `.mean()`, `.sum()` etc. are methods, not free functions | Call them directly on the array: `arr.mean()`, or use `np.mean(arr)` |
| Confusing `.min()`/`.max()` (the value) with `.argmin()`/`.argmax()` (the position) | Use `arg` versions when you need *where* the value is, not what it is |

---

## ✍️ Practice Questions

1. What does "vectorization" mean, and why is it faster than a loop?
2. Given `arr = np.array([2, 4, 6])`, what does `arr * 10` return?
3. What is broadcasting, in your own words?
4. Given `scores = np.array([70, 85, 90, 60])`, find the average and the highest score.
5. What's the difference between `.max()` and `.argmax()`?

<details>
<summary>💡 Click to see answers</summary>

1. Vectorization means applying an operation to an entire array at once,
   using NumPy's optimized internal code, instead of looping through each
   item in plain Python — this makes it much faster on large data.
2. `[20 40 60]`
3. Broadcasting is NumPy's way of applying an operation between arrays of
   different shapes (most commonly, an array and a single number) by
   automatically "stretching" the smaller one to match.
4. ```python
   scores = np.array([70, 85, 90, 60])
   print(scores.mean())   # 76.25
   print(scores.max())    # 90
   ```
5. `.max()` returns the actual highest **value**. `.argmax()` returns the
   **position (index)** where that highest value is located.

</details>

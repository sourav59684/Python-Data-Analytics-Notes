# 🔢 NumPy — Random Numbers

---

## 📌 What Is `np.random`?

NumPy has a built-in toolkit for generating **random numbers** — useful for
simulations, testing, sampling data, and shuffling datasets.

```python
import numpy as np

random_number = np.random.randint(1, 100)
print(random_number)   # a random whole number between 1 and 99
```

---

## 📊 Why This Matters for Data Analytics

Random number generation is used constantly in data work: creating sample/
test datasets, randomly splitting data into training/testing groups,
simulating scenarios ("what if sales varied randomly by ±10%?"), and
randomly sampling a huge dataset down to a manageable size for exploration.

---

## 🔧 Common Random Functions

| Function | What It Does | Example |
|---|---|---|
| `np.random.randint(low, high, size)` | Random whole numbers | `np.random.randint(1, 10, 5)` |
| `np.random.rand(size)` | Random decimals between 0 and 1 | `np.random.rand(3)` |
| `np.random.randn(size)` | Random numbers following a normal ("bell curve") distribution | `np.random.randn(5)` |
| `np.random.choice(list)` | Randomly picks item(s) from a list | `np.random.choice(["A","B","C"])` |
| `np.random.shuffle(arr)` | Randomly reorders an array **in place** | `np.random.shuffle(arr)` |
| `np.random.seed(n)` | Locks the "randomness" so results are repeatable | `np.random.seed(42)` |

```python
# 5 random whole numbers between 1 and 100
random_ints = np.random.randint(1, 101, 5)
print(random_ints)   # e.g. [45 12 87 3 76]

# 3 random decimals between 0 and 1
random_floats = np.random.rand(3)
print(random_floats)   # e.g. [0.34 0.87 0.12]
```

---

## 🔒 Using `np.random.seed()` for Repeatable Results

Randomness is genuinely random every time you run it — **unless** you "seed"
it. Seeding makes your random results **repeatable**, which is critical when
testing code or sharing results with others so everyone sees the same output.

```python
np.random.seed(42)
print(np.random.randint(1, 100, 5))   # always the same 5 numbers, every time you run this

np.random.seed(42)
print(np.random.randint(1, 100, 5))   # identical output — because the seed is the same
```
*Explanation:* Without a seed, you'd get different numbers every single run.
With `np.random.seed(42)` set beforehand, the "random" sequence becomes
predictable and repeatable — extremely useful for testing and sharing
reproducible analysis.

---

## 💡 Examples

### 1. Basic — Rolling a dice 10 times
```python
import numpy as np

dice_rolls = np.random.randint(1, 7, 10)   # 1 to 6, 10 times
print(dice_rolls)
```

### 2. Analytics Use Case — Simulating daily sales with randomness
```python
np.random.seed(1)
simulated_sales = np.random.randint(800, 1500, 7)   # 7 days of random sales
print(simulated_sales)
print("Average simulated sales:", simulated_sales.mean())
```
*Explanation:* This is exactly how analysts create test/sample datasets when
real data isn't available yet, or when running "what-if" simulations.

### 3. Randomly sampling from a list of categories
```python
regions = ["North", "South", "East", "West"]
random_region = np.random.choice(regions)
print(random_region)   # one randomly chosen region

# picking multiple, with repeats allowed
sampled_regions = np.random.choice(regions, size=6)
print(sampled_regions)
```

### 4. Shuffling data (e.g., before splitting into train/test sets)
```python
customer_ids = np.arange(1, 11)   # [1 2 3 4 5 6 7 8 9 10]
np.random.shuffle(customer_ids)
print(customer_ids)   # same numbers, random order
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Expecting the same "random" result every run without a seed | Use `np.random.seed(n)` if you need repeatable results |
| Confusing `.rand()` (0 to 1 decimals) with `.randint()` (whole numbers in a range) | Pick the right function based on what kind of number you need |
| Forgetting `np.random.shuffle()` changes the array in place | It doesn't return a new array — it modifies the original directly |
| Using randomness for anything that should reflect real data | Random numbers are for simulation/testing — not a substitute for real data |

---

## ✍️ Practice Questions

1. What does `np.random.randint(1, 50, 5)` generate?
2. Why would you use `np.random.seed()`?
3. What's the difference between `np.random.rand()` and `np.random.randint()`?
4. Write code to randomly shuffle the list `[1, 2, 3, 4, 5]`.
5. How would you randomly pick 3 names from `["Ravi", "Anu", "Simran", "Karan"]`?

<details>
<summary>💡 Click to see answers</summary>

1. It generates 5 random whole numbers, each between 1 and 49 (50 is excluded).
2. To make your "random" results repeatable — so running the code again
   gives the exact same output, which is important for testing and sharing results.
3. `.rand()` generates random **decimal** numbers between 0 and 1.
   `.randint()` generates random **whole numbers** within a range you specify.
4. ```python
   import numpy as np
   nums = np.array([1, 2, 3, 4, 5])
   np.random.shuffle(nums)
   print(nums)
   ```
5. ```python
   names = ["Ravi", "Anu", "Simran", "Karan"]
   picked = np.random.choice(names, size=3, replace=False)
   print(picked)
   ```
   (`replace=False` ensures no name is picked twice.)

</details>

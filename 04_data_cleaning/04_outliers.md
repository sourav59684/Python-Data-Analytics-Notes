# 🧹 Data Cleaning — Outliers

---

## 📌 What Is an Outlier?

An **outlier** is a value that's unusually far from the rest of the data —
like one customer with a $500,000 order in a dataset where most orders are
$50-$200. Outliers can be genuine (a real VIP customer) or errors (a typo
adding an extra zero).

```python
import pandas as pd
orders = pd.Series([50, 60, 55, 48, 52, 500000, 58])
```
That `500000` clearly doesn't belong with the rest — it's an outlier.

---

## 📊 Why This Matters for Data Analytics

A single outlier can distort your entire analysis — a huge value drags the
average way up, making it look like "typical" orders are much bigger than
they really are. Detecting outliers (and deciding whether to keep, remove,
or investigate them) is a key step before trusting any summary statistic.

---

## 📏 1. The IQR Method (Interquartile Range)

The **IQR method** is the standard way to detect outliers using percentiles.

```
Q1 = 25th percentile (25% of values are below this)
Q3 = 75th percentile (75% of values are below this)
IQR = Q3 - Q1

Lower bound = Q1 - 1.5 × IQR
Upper bound = Q3 + 1.5 × IQR

Anything below the lower bound or above the upper bound = outlier
```

```python
import pandas as pd

data = pd.Series([50, 60, 55, 48, 52, 500000, 58, 61, 47])

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data < lower_bound) | (data > upper_bound)]
print(outliers)   # 500000
```

### 🔧 Common IQR-Related Methods

| Method | What It Does |
|---|---|
| `.quantile(0.25)` | 25th percentile (Q1) |
| `.quantile(0.75)` | 75th percentile (Q3) |
| `.quantile(0.5)` | Median (same as 50th percentile) |

---

## 📐 2. The Z-Score Method

A **Z-score** measures how many standard deviations a value is from the
mean. Values with a Z-score beyond a certain threshold (commonly ±3) are
flagged as outliers.

```
Z = (value - mean) / standard deviation
```

```python
import pandas as pd
import numpy as np

data = pd.Series([50, 60, 55, 48, 52, 500000, 58, 61, 47])

mean = data.mean()
std = data.std()

z_scores = (data - mean) / std
outliers = data[abs(z_scores) > 3]
print(outliers)   # 500000
```

| | IQR Method | Z-Score Method |
|---|---|---|
| Based on | Percentiles (median-based) | Mean and standard deviation |
| Works well when | Data isn't perfectly symmetric | Data roughly follows a normal ("bell curve") distribution |
| Common threshold | 1.5 × IQR | Z-score beyond ±3 |

---

## 💡 Examples

### 1. Basic — Detecting outliers in a price column with IQR
```python
prices = pd.Series([100, 120, 110, 95, 105, 98, 5000, 115])

Q1 = prices.quantile(0.25)
Q3 = prices.quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = prices[(prices < lower) | (prices > upper)]
print(outliers)
```

### 2. Analytics Use Case — Flagging outliers in a full DataFrame column
```python
df = pd.DataFrame({"order_amount": [50, 60, 55, 48, 52, 500000, 58, 61, 47]})

Q1 = df["order_amount"].quantile(0.25)
Q3 = df["order_amount"].quantile(0.75)
IQR = Q3 - Q1

df["is_outlier"] = (df["order_amount"] < Q1 - 1.5*IQR) | (df["order_amount"] > Q3 + 1.5*IQR)
print(df)
```
*Explanation:* Adding a `True`/`False` outlier flag column is a common
approach — it lets you keep the data intact while marking which rows need a
closer look, rather than deleting anything immediately.

### 3. Removing detected outliers
```python
clean_df = df[~df["is_outlier"]]   # keep only rows where is_outlier is False
print(clean_df.shape)
```

### 4. Comparing average before and after removing an outlier
```python
print("Average with outlier:", df["order_amount"].mean())
print("Average without outlier:", clean_df["order_amount"].mean())
```
*Explanation:* This comparison shows exactly how much a single extreme
value can distort the average — a great way to justify why outlier handling
matters.

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Automatically deleting every outlier without investigating | Some outliers are real and important (a genuine VIP order) — investigate first |
| Using the mean to summarize data that still contains outliers | Consider the median instead, or handle outliers first |
| Only checking for outliers visually, skipping numeric methods | Use IQR or Z-score for a repeatable, objective definition |
| Assuming one threshold (1.5 × IQR or Z=3) fits every dataset | Thresholds are starting points — adjust based on context and domain knowledge |

---

## ✍️ Practice Questions

1. What is an outlier, in your own words?
2. What are Q1 and Q3 in the IQR method?
3. Write the formula for the IQR outlier bounds.
4. What does a Z-score tell you about a value?
5. Why shouldn't you always delete outliers automatically?

<details>
<summary>💡 Click to see answers</summary>

1. An outlier is a value that's unusually far from most of the other values
   in a dataset — either a genuine unusual case or a data error.
2. Q1 is the 25th percentile (25% of values fall below it). Q3 is the 75th
   percentile (75% of values fall below it).
3. ```
   IQR = Q3 - Q1
   Lower bound = Q1 - 1.5 * IQR
   Upper bound = Q3 + 1.5 * IQR
   ```
4. It tells you how many standard deviations a value is away from the
   mean — a large positive or negative Z-score (commonly beyond ±3) suggests
   the value is unusually far from the average.
5. Some outliers represent real, meaningful data (like a genuinely huge but
   legitimate order) — deleting them automatically could remove important
   information rather than just noise or errors.

</details>

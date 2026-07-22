# 📈 Data Visualization — Seaborn

---

## 📌 What Is Seaborn?

**Seaborn** is a charting library built on top of Matplotlib, designed
specifically for statistical and data analysis charts. It makes some of the
most useful analytics charts (distributions, comparisons, correlations)
much easier to create than plain Matplotlib, with better-looking defaults.

```python
import seaborn as sns   # "sns" is the standard shortcut everyone uses
import matplotlib.pyplot as plt

sns.histplot(data=df, x="age")
plt.show()
```

> 💬 **Seaborn and Matplotlib work together.** Seaborn creates the chart,
> and you still use `plt.show()`, `plt.title()`, etc. from Matplotlib
> alongside it.

---

## 📊 Why This Matters for Data Analytics

Seaborn is built specifically for exploring datasets — understanding
distributions, spotting outliers, comparing groups, and checking
relationships between columns. It's the standard tool analysts reach for
during exploratory data analysis (EDA).

---

## 📊 1. Distribution Plots — Understanding One Column

### `histplot` — Histogram (how values are distributed)

```python
sns.histplot(data=df, x="age", bins=10)
plt.title("Age Distribution")
plt.show()
```
*Explanation:* A histogram groups values into "bins" (ranges) and shows how
many values fall into each — instantly revealing whether data is spread
evenly, clustered, or skewed.

### `boxplot` — Spotting the Spread and Outliers

```python
sns.boxplot(data=df, y="salary")
plt.title("Salary Distribution")
plt.show()
```

```
        ┌─────┐
  ○     │     │        ○ = outlier
────────┤─────┤─────── ← whiskers show the typical range
        │     │
        └─────┘
   Q1  Median  Q3
```
*Explanation:* The box shows the middle 50% of the data (Q1 to Q3), the
line inside is the median, and the "whiskers" extend to the typical range —
individual dots beyond the whiskers are flagged as potential outliers
(exactly the IQR concept from the Data Cleaning section).

---

## 🔧 Common Seaborn Plot Types

| Function | What It Shows | Best For |
|---|---|---|
| `sns.histplot()` | Distribution of one numeric column | Understanding spread and shape of data |
| `sns.boxplot()` | Spread, median, and outliers | Comparing distributions, spotting outliers |
| `sns.countplot()` | Count of each category | "How many of each category exist" |
| `sns.barplot()` | Average value per category | Comparing a number across groups |
| `sns.lineplot()` | Trend over a continuous variable | Time series, trends |
| `sns.scatterplot()` | Relationship between two numeric columns | Checking correlation |
| `sns.violinplot()` | Distribution shape + spread combined | Detailed comparison across groups |
| `sns.heatmap()` | Grid of values shown as color intensity | Correlations, missing-data overview |
| `sns.pairplot()` | Scatter plots for every pair of numeric columns | Quick overview of all relationships at once |

---

## 📊 2. Categorical Plots — Comparing Groups

```python
sns.countplot(data=df, x="city")
plt.title("Number of Customers per City")
plt.show()
```
*Explanation:* `countplot` automatically counts how many rows fall into each
category — you don't need to `.groupby()` first, Seaborn does the counting.

```python
sns.barplot(data=df, x="city", y="salary")
plt.title("Average Salary by City")
plt.show()
```
*Explanation:* `barplot` automatically calculates and shows the **average**
of `y` for each category in `x` (unlike `countplot`, which just counts rows).

```python
sns.violinplot(data=df, x="department", y="salary")
plt.title("Salary Distribution by Department")
plt.show()
```

---

## 🌡️ 3. Heatmaps — Visualizing Missing Data or Correlations

```python
# Visualizing missing data at a glance
sns.heatmap(df.isnull(), cbar=False)
plt.title("Missing Data Overview")
plt.show()
```
*Explanation:* This turns `.isnull()` (True/False for every cell) into a
color grid — missing values show up as a distinct color, making patterns of
missing data easy to spot across the whole dataset at once.

```python
# Visualizing how numeric columns relate to each other
correlation = df.corr(numeric_only=True)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
```
*Explanation:* `annot=True` prints the actual correlation numbers on top of
the color grid, so you get both the visual pattern and the exact values.

---

## 💡 Examples

### 1. Basic — Distribution of exam scores
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(data=df, x="score", bins=8)
plt.title("Exam Score Distribution")
plt.show()
```

### 2. Analytics Use Case — Comparing salary spread across departments
```python
sns.boxplot(data=df, x="department", y="salary")
plt.title("Salary by Department")
plt.xticks(rotation=45)
plt.show()
```
*Explanation:* This single chart instantly shows which department has
higher typical salaries, which has more spread, and which has outliers.

### 3. Checking the relationship between two numeric columns
```python
sns.scatterplot(data=df, x="experience_years", y="salary")
plt.title("Experience vs. Salary")
plt.show()
```

### 4. Full EDA snapshot with a pairplot
```python
sns.pairplot(df[["age", "salary", "experience_years"]])
plt.show()
```
*Explanation:* `pairplot` generates scatter plots for every pair of numeric
columns at once — a fast way to spot relationships across an entire
dataset in a single command.

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Confusing `countplot` (counts rows) with `barplot` (averages a value) | Use `countplot` for "how many," `barplot` for "average of what" |
| Forgetting `plt.show()` after a Seaborn chart | Seaborn still relies on Matplotlib to actually display the chart |
| Running `.corr()` on a DataFrame with text columns without `numeric_only=True` | Add `numeric_only=True` or it may error on non-numeric columns |
| Overcrowding a `pairplot` with too many columns | Select only the columns you actually need — too many becomes unreadable |

---

## ✍️ Practice Questions

1. What's the difference between `sns.countplot()` and `sns.barplot()`?
2. Which chart would you use to spot outliers in a "price" column?
3. Write code for a heatmap showing missing data in a DataFrame `df`.
4. What does `annot=True` do in a correlation heatmap?
5. Which Seaborn chart would you use to quickly check relationships between all numeric columns at once?

<details>
<summary>💡 Click to see answers</summary>

1. `countplot` counts how many rows fall into each category. `barplot`
   shows the **average** of a numeric column for each category.
2. A **boxplot** — it clearly shows the typical range and flags individual
   points that fall outside it as potential outliers.
3. ```python
   sns.heatmap(df.isnull(), cbar=False)
   plt.show()
   ```
4. It prints the actual correlation number directly on each cell of the
   heatmap, in addition to the color shading.
5. `sns.pairplot()` — it generates scatter plots for every combination of
   numeric columns in one command.

</details>

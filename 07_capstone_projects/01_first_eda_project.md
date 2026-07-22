# 🎯 Capstone Project — Your First EDA (Exploratory Data Analysis)

---

## 📌 What Is This Project?

This is where everything from Foundations → NumPy → Pandas → Data Cleaning →
Advanced Analytics → Visualization comes together in one real workflow.

**EDA (Exploratory Data Analysis)** is the process of getting to know a new
dataset — understanding its structure, cleaning it up, and pulling out
initial insights — before any deeper analysis or modeling happens. It's the
single most common task a data analyst does, on almost every project.

We'll walk through a realistic dataset: **customer orders for an online store.**

```python
import pandas as pd

df = pd.read_csv("customer_orders.csv")
```

Imagine this dataset has these columns: `order_id`, `customer_name`,
`city`, `product`, `price`, `quantity`, `order_date`, `status`.

---

## 📊 Why This Matters

Real datasets are never perfectly clean. This project deliberately walks
through messy, realistic problems — missing values, duplicate rows, a price
column stored as text, outliers — exactly the kind of issues you'll face on
day one of any real analytics job.

---

## 🏗️ The EDA Workflow

```
1. Load the data
2. Inspect it (shape, info, describe)
3. Clean it (missing values, duplicates, wrong types)
4. Explore it (groupby, sorting, filtering)
5. Visualize it (charts to support your findings)
6. Summarize your insights
```

---

## 🔎 Step 1 & 2 — Load and Inspect

```python
import pandas as pd

df = pd.read_csv("customer_orders.csv")

print(df.shape)        # e.g. (1000, 8)
print(df.head())        # first look at the data
print(df.info())        # data types, missing value counts
print(df.describe())    # statistical summary of numeric columns
```

**What to look for right away:**
- Are there missing values? (Check the "Non-Null Count" in `.info()`)
- Are data types correct? (Is "price" really a number, or accidentally text?)
- Do the min/max values in `.describe()` look reasonable, or is something off?

---

## 🧹 Step 3 — Clean the Data

### Fix the "price" column (often stored as messy text)

```python
df["price"] = pd.to_numeric(df["price"], errors="coerce")
```

### Handle missing values

```python
print(df.isnull().sum())   # see exactly what's missing, and how much

df["city"] = df["city"].fillna(df["city"].mode()[0])   # fill categorical with the most common value
df = df.dropna(subset=["price", "order_id"])              # drop rows missing something essential
```

### Remove duplicate orders

```python
print("Duplicates found:", df.duplicated().sum())
df = df.drop_duplicates()
```

### Convert the date column

```python
df["order_date"] = pd.to_datetime(df["order_date"])
```

### Check for outliers in price

```python
Q1 = df["price"].quantile(0.25)
Q3 = df["price"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[(df["price"] < Q1 - 1.5*IQR) | (df["price"] > Q3 + 1.5*IQR)]
print("Potential outliers:", outliers.shape[0])
```

---

## 🔍 Step 4 — Explore the Data

### Which city generates the most revenue?

```python
df["total"] = df["price"] * df["quantity"]

revenue_by_city = df.groupby("city")["total"].sum().sort_values(ascending=False)
print(revenue_by_city)
```

### What's the average order value per product?

```python
avg_by_product = df.groupby("product")["total"].mean().sort_values(ascending=False)
print(avg_by_product)
```

### How does revenue trend over time?

```python
df = df.set_index("order_date")
monthly_revenue = df.resample("M")["total"].sum()
print(monthly_revenue)
```

### What percentage of orders were cancelled?

```python
status_counts = df["status"].value_counts(normalize=True) * 100
print(status_counts)
```

---

## 📈 Step 5 — Visualize the Findings

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Revenue by city
revenue_by_city.plot(kind="bar", title="Revenue by City")
plt.ylabel("Revenue ($)")
plt.show()

# Monthly revenue trend
monthly_revenue.plot(kind="line", title="Monthly Revenue Trend", marker="o")
plt.ylabel("Revenue ($)")
plt.show()

# Price distribution and outliers
sns.boxplot(y=df["price"])
plt.title("Price Distribution")
plt.show()

# Order status breakdown
sns.countplot(data=df.reset_index(), x="status")
plt.title("Order Status Breakdown")
plt.show()
```

---

## 📝 Step 6 — Summarize Your Insights

A good EDA always ends with a short written summary — this is what you'd
actually present to a manager or team, not the code itself.

**Example summary:**
> - Mumbai generates the highest total revenue, followed by Delhi and Pune.
> - Average order value is highest for "Electronics," suggesting a premium category.
> - Revenue shows a clear upward trend from January to June.
> - 8% of orders were cancelled — worth investigating why.
> - A small number of unusually high-priced orders were flagged as outliers
>   and should be reviewed for possible data entry errors.

---

## 💡 Full Mini Example — Putting It All Together

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load
df = pd.read_csv("customer_orders.csv")

# 2. Inspect
print(df.shape)
print(df.info())

# 3. Clean
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["city"] = df["city"].fillna(df["city"].mode()[0])
df = df.dropna(subset=["price"])
df = df.drop_duplicates()
df["order_date"] = pd.to_datetime(df["order_date"])

# 4. Explore
df["total"] = df["price"] * df["quantity"]
revenue_by_city = df.groupby("city")["total"].sum().sort_values(ascending=False)

# 5. Visualize
revenue_by_city.plot(kind="bar", title="Revenue by City")
plt.show()

# 6. Summarize (in your own written notes, alongside the code)
print(revenue_by_city)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Jumping straight to charts before cleaning the data | Always inspect and clean first — pretty charts of dirty data are still wrong |
| Fixing missing values the same way for every column | Use context: mean/median for numbers, mode for categories |
| Forgetting to check for duplicates before calculating totals | Duplicate rows silently inflate sums and averages |
| Presenting code instead of a written summary of findings | A short, plain-language summary is what stakeholders actually want to see |

---

## ✍️ Practice Questions

1. What are the 6 steps of a typical EDA workflow?
2. Why should you clean data before visualizing it, not after?
3. Given a "price" column stored as text, how would you safely convert it to numbers?
4. Why is it important to check for duplicates before calculating a total revenue figure?
5. What's the difference between exploring data and summarizing findings?

<details>
<summary>💡 Click to see answers</summary>

1. Load the data → Inspect it → Clean it → Explore it → Visualize it →
   Summarize the insights.
2. Because a chart built on dirty data (duplicates, wrong types, missing
   values) will show misleading patterns — cleaning first ensures your
   visuals reflect reality.
3. ```python
   df["price"] = pd.to_numeric(df["price"], errors="coerce")
   ```
4. Duplicate rows get counted (and summed) multiple times, which inflates
   totals and makes revenue or counts look higher than they really are.
5. Exploring is the technical process of running groupby, filters, and
   calculations to find patterns. Summarizing is translating those findings
   into a short, plain-language explanation that a non-technical person
   (like a manager) can understand and act on.

</details>

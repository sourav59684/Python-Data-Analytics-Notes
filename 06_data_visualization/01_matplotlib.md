# 📈 Data Visualization — Matplotlib

---

## 📌 What Is Matplotlib?

**Matplotlib** is Python's foundational charting library — it lets you turn
numbers into visuals like bar charts, line charts, and pie charts. Most
other Python visualization tools (including Seaborn, which you'll see next)
are actually built on top of it.

```python
import matplotlib.pyplot as plt   # "plt" is the standard shortcut everyone uses

plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.show()
```

---

## 📊 Why This Matters for Data Analytics

Numbers in a table are hard to interpret quickly — a chart makes trends,
comparisons, and outliers obvious at a glance. Being able to turn a Pandas
column into a clear chart is a core, constantly-used analytics skill.

---

## 📉 1. Line Charts — Showing Trends Over Time

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [200, 250, 220, 300, 280]

plt.plot(days, sales)
plt.title("Daily Sales")
plt.xlabel("Day")
plt.ylabel("Sales ($)")
plt.show()
```

Line charts are best for showing **change over time** — daily sales, stock
prices, temperature over a week.

---

## 📊 2. Bar Charts — Comparing Categories

```python
products = ["Pen", "Notebook", "Bag"]
sales = [150, 300, 500]

plt.bar(products, sales)
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.show()
```

Bar charts are best for **comparing separate categories** — sales by
product, population by city, votes by candidate.

---

## 🥧 3. Pie Charts — Showing Proportions

```python
categories = ["Electronics", "Clothing", "Groceries"]
share = [45, 30, 25]

plt.pie(share, labels=categories, autopct="%1.1f%%")
plt.title("Sales Share by Category")
plt.show()
```

Pie charts are best for showing **parts of a whole** — market share, budget
breakdown. `autopct="%1.1f%%"` displays the percentage on each slice.

> ⚠️ **Use pie charts sparingly.** They're only clear with a small number of
> categories (usually under 5-6) — beyond that, a bar chart is almost always
> easier to read accurately.

---

## 🔧 Common Matplotlib Functions

| Function | What It Does |
|---|---|
| `plt.plot(x, y)` | Draws a line chart |
| `plt.bar(x, y)` | Draws a bar chart |
| `plt.pie(values, labels=...)` | Draws a pie chart |
| `plt.scatter(x, y)` | Draws a scatter plot (individual points) |
| `plt.title("...")` | Adds a chart title |
| `plt.xlabel("...")` / `plt.ylabel("...")` | Labels the axes |
| `plt.legend()` | Shows a legend (when plotting multiple lines/series) |
| `plt.show()` | Displays the finished chart |
| `plt.figure(figsize=(w, h))` | Sets the chart size before plotting |

---

## 🎨 4. Customizing & Combining Charts

```python
plt.figure(figsize=(8, 5))
plt.plot(days, sales, color="green", marker="o", linestyle="--", label="This Week")
plt.title("Weekly Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales ($)")
plt.legend()
plt.grid(True)
plt.show()
```

| Customization | Example |
|---|---|
| Line color | `color="green"` |
| Point markers | `marker="o"` |
| Line style | `linestyle="--"` (dashed) |
| Add a grid | `plt.grid(True)` |
| Chart size | `plt.figure(figsize=(8, 5))` |

---

## 📊 Plotting Directly from Pandas

Pandas has a built-in `.plot()` shortcut, so you often don't even need to
call Matplotlib functions directly for simple charts.

```python
import pandas as pd

df = pd.DataFrame({"month": ["Jan", "Feb", "Mar"], "sales": [500, 700, 650]})
df.plot(x="month", y="sales", kind="line", title="Monthly Sales")
```

| `kind=` value | Chart Type |
|---|---|
| `"line"` | Line chart |
| `"bar"` | Bar chart |
| `"pie"` | Pie chart |
| `"hist"` | Histogram |

---

## 💡 Examples

### 1. Basic — A simple line chart
```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
revenue = [10000, 12000, 9000, 15000]

plt.plot(months, revenue, marker="o")
plt.title("Monthly Revenue")
plt.show()
```

### 2. Analytics Use Case — Comparing product sales with a bar chart
```python
df = pd.DataFrame({
    "product": ["Pen", "Notebook", "Bag", "Bottle"],
    "sales": [150, 300, 500, 220]
})

plt.bar(df["product"], df["sales"], color="skyblue")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales ($)")
plt.show()
```

### 3. Showing market share with a pie chart
```python
categories = ["Electronics", "Clothing", "Groceries", "Other"]
share = [40, 25, 20, 15]

plt.pie(share, labels=categories, autopct="%1.0f%%")
plt.title("Market Share")
plt.show()
```

### 4. Plotting two lines together for comparison
```python
plt.plot(months, [10000, 12000, 9000, 15000], label="2023", marker="o")
plt.plot(months, [11000, 13500, 9500, 16000], label="2024", marker="o")
plt.title("Revenue: 2023 vs 2024")
plt.legend()
plt.show()
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting `plt.show()` | Without it, the chart may not display, depending on your environment |
| Using a pie chart with too many categories | Switch to a bar chart once you have more than ~6 categories |
| Not labeling axes or adding a title | Charts without labels are confusing to anyone reading them later |
| Confusing `plt.plot()` (line) with `plt.bar()` (bar) | Pick the chart type that matches what you're trying to show — trend vs. comparison |

---

## ✍️ Practice Questions

1. Which chart type is best for showing a trend over time?
2. Which chart type is best for comparing categories side-by-side?
3. Write code for a bar chart showing sales `[100, 200, 150]` for products `["A", "B", "C"]`.
4. Why should pie charts be used sparingly?
5. What does `plt.legend()` do?

<details>
<summary>💡 Click to see answers</summary>

1. A **line chart** — it clearly shows how a value changes over time (like
   daily or monthly trends).
2. A **bar chart** — it makes it easy to compare distinct categories side by side.
3. ```python
   plt.bar(["A", "B", "C"], [100, 200, 150])
   plt.show()
   ```
4. Pie charts become hard to read accurately once there are more than a
   handful of slices — differences between similarly-sized slices are
   difficult to judge visually. A bar chart handles many categories more clearly.
5. It displays a legend/key on the chart, identifying which line or bar
   corresponds to which label — essential when plotting multiple series together.

</details>

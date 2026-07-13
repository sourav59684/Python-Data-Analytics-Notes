# 📊 Advanced Analytics — Time Series Basics

---

## 📌 What Is Time Series Data?

**Time series data** is any data tied to specific points in time — daily
sales, hourly temperature readings, monthly signups. Pandas has special
tools for working with dates and times, because they need different
handling than plain numbers or text.

```python
import pandas as pd

df = pd.DataFrame({
    "date": ["2024-01-01", "2024-01-02", "2024-01-03"],
    "sales": [500, 700, 650]
})

df["date"] = pd.to_datetime(df["date"])   # convert text into a real date
print(df.dtypes)
```
```
date     datetime64[ns]
sales             int64
dtype: object
```

---

## 📊 Why This Matters for Data Analytics

Business data is almost always tracked over time — "sales this month vs.
last month," "how does traffic change by day of the week," "what's the
7-day rolling average." Once dates are properly recognized (not just text),
Pandas unlocks powerful date-based filtering, grouping, and trend analysis.

---

## 📅 1. Converting to Datetime — `pd.to_datetime()`

```python
df["date"] = pd.to_datetime(df["date"])
```

Once a column is a real datetime type, you can pull out specific parts of it:

### 🔧 Common Datetime Attributes (via `.dt`)

| Attribute | What It Gives You | Example |
|---|---|---|
| `.dt.year` | The year | `2024` |
| `.dt.month` | The month number | `1` (January) |
| `.dt.day` | The day of the month | `15` |
| `.dt.day_name()` | The weekday name | `"Monday"` |
| `.dt.quarter` | Which quarter (1-4) | `1` |

```python
df["year"] = df["date"].dt.year
df["weekday"] = df["date"].dt.day_name()
print(df)
```

---

## 🗓️ 2. Setting a Date as the Index

Many time series operations work best when the date column is set as the
DataFrame's index.

```python
df = df.set_index("date")
print(df)
```
```
            sales
date
2024-01-01    500
2024-01-02    700
2024-01-03    650
```

Now you can slice by date directly:

```python
print(df["2024-01-01":"2024-01-02"])   # rows within this date range
```

---

## 🔁 3. Resampling — Summarizing by Time Period

**Resampling** groups time series data into larger chunks (weekly, monthly)
and summarizes it — similar to `groupby`, but specifically for time.

### 🔧 Common Resampling Frequencies

| Code | Means |
|---|---|
| `"D"` | Daily |
| `"W"` | Weekly |
| `"M"` | Monthly |
| `"Q"` | Quarterly |
| `"Y"` | Yearly |

```python
monthly_sales = df.resample("M")["sales"].sum()
print(monthly_sales)
```
*Explanation:* This takes daily data and rolls it up into monthly totals —
extremely common for turning detailed transaction logs into a readable
monthly report.

---

## 📈 4. Rolling Windows — Moving Averages

A **rolling window** calculates something (usually an average) over a
sliding window of recent periods — smoothing out day-to-day noise to reveal
the underlying trend.

```python
df["7_day_avg"] = df["sales"].rolling(window=7).mean()
```

```
Day:      1    2    3    4    5    6    7    8
Sales:   500  700  650  600  720  680  710  690
7-day
avg:      -    -    -    -    -    -   665.7 678.6
```
*Explanation:* The rolling average for day 7 is the average of days 1-7. For
day 8, it's the average of days 2-8 — the "window" slides forward one day
at a time. Notice the first 6 days show no value — there aren't yet 7 days
to average.

---

## 💡 Examples

### 1. Basic — Converting and extracting date parts
```python
df = pd.DataFrame({"date": ["2024-03-01", "2024-03-02"], "sales": [400, 550]})
df["date"] = pd.to_datetime(df["date"])
df["weekday"] = df["date"].dt.day_name()
print(df)
```

### 2. Analytics Use Case — Monthly revenue report
```python
df["date"] = pd.to_datetime(df["date"])
df = df.set_index("date")

monthly_revenue = df.resample("M")["sales"].sum()
print(monthly_revenue)
```
*Explanation:* This is one of the most common real-world tasks — turning
raw daily transaction data into a clean monthly summary for a report.

### 3. Smoothing noisy daily data with a rolling average
```python
df["sales_7d_avg"] = df["sales"].rolling(window=7).mean()
df[["sales", "sales_7d_avg"]].plot()   # visualizing raw vs. smoothed trend
```

### 4. Filtering data for a specific date range
```python
df = df.set_index("date")
q1_data = df["2024-01-01":"2024-03-31"]
print(q1_data.shape)
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting to convert a date column with `pd.to_datetime()` first | Dates stored as plain text can't be resampled, sorted correctly, or filtered by range |
| Using `.month` directly instead of `.dt.month` | Date attributes always need the `.dt` accessor: `df["date"].dt.month` |
| Expecting `.resample()` to work without a datetime index | Set the date column as the index first: `df.set_index("date")` |
| Misreading the first few `NaN` values in a rolling average as an error | They're expected — there aren't enough prior periods yet to calculate the window |

---

## ✍️ Practice Questions

1. Why do you need to convert a date column with `pd.to_datetime()`?
2. What does `.dt.day_name()` return?
3. Write code to calculate total monthly sales from a daily sales DataFrame.
4. What does a rolling window of 7 calculate?
5. Why do the first several rows of a rolling average show `NaN`?

<details>
<summary>💡 Click to see answers</summary>

1. Without conversion, a date is stored as plain text — Pandas can't sort it
   chronologically, filter by date range, or extract parts like month/year
   correctly. Converting makes it a real datetime type Pandas understands.
2. It returns the name of the weekday (e.g., `"Monday"`, `"Tuesday"`) for
   each date.
3. ```python
   df = df.set_index("date")
   monthly_totals = df.resample("M")["sales"].sum()
   ```
4. It calculates the average of the current row and the 6 rows before it
   (7 total), sliding forward one row at a time — smoothing out short-term
   fluctuations to show the underlying trend.
5. Because there aren't enough previous rows yet to fill the window — e.g.,
   with a 7-day rolling average, the first 6 rows don't have 7 full days of
   data to average yet.

</details>

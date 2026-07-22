# 📂 Datasets

Small sample datasets used across the notes in this repo. Both files are
intentionally a little messy (missing values, a duplicate row, an outlier,
a stray "N/A") so you can practice the cleaning techniques from
`04_data_cleaning/` on real examples, not just made-up ones.

## Files in This Folder

| File | Used In | Description |
|---|---|---|
| [`customer_orders.csv`](customer_orders.csv) | `07_capstone_projects/01_first_eda_project.md` | 30 e-commerce orders — customer, city, product, price, quantity, order date, status. Includes a missing city value, missing prices, one exact duplicate row (order 1001/1009), a stray `"N/A"` price, and one price outlier (₹50,000 vs. typical ₹1,000-2,000). |
| [`sales_data.csv`](sales_data.csv) | `03_pandas_core/`, `04_data_cleaning/` | 15 general retail sales records — product, category, price, quantity, city, sale date. Includes missing prices, a duplicate row, and one price outlier. |

## Quick Start

```python
import pandas as pd

orders = pd.read_csv("datasets/customer_orders.csv")
sales = pd.read_csv("datasets/sales_data.csv")

print(orders.info())    # notice the missing values and dtypes
print(orders.head())
```

## Notes

- Keep sample datasets small (a few hundred rows) — these notes are for
  learning, not production-scale data processing.
- If you add your own datasets, update the table above so it's clear what
  each file is used for and which note references it.
- Large or sensitive datasets should **not** be committed to a public
  repo — use small, anonymized samples instead.

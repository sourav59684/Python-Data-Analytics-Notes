# 🐍📊 Python for Data Analytics — Notes

Beginner-friendly, example-driven notes for learning Python, NumPy, and Pandas
for data analytics — written the same way as the companion
[SQL Data Analytics Notes](https://github.com/sourav59684/SQL-Data-Analytics-Notes).

Each file explains one topic area in plain language, with simple runnable
examples and small practice questions. No prior data analytics experience assumed.

---

## 📚 Index

### 01. Python Foundations
| # | File | Covers |
|---|------|--------|
| 1 | [01_introduction_to_python.md](01_python_foundations/01_introduction_to_python.md) | What is Python, why it's used for data analytics, how code runs |
| 2 | [02_data_types.md](01_python_foundations/02_data_types.md) | int, float, string, boolean, list, tuple, dict, set, None |
| 3 | [03_variables_and_conversion.md](01_python_foundations/03_variables_and_conversion.md) | Creating variables, naming rules, type casting |
| 4 | [04_operators.md](01_python_foundations/04_operators.md) | Arithmetic, comparison, logical, assignment, membership/identity |
| 5 | [05_control_flow.md](01_python_foundations/05_control_flow.md) | if-else, for loop, while loop, break/continue/pass |
| 6 | [06_functions.md](01_python_foundations/06_functions.md) | def, parameters, return, default/keyword args, lambda |
| 7 | [07_comprehensions.md](01_python_foundations/07_comprehensions.md) | List comprehension, dict comprehension |
| 8 | [08_error_handling.md](01_python_foundations/08_error_handling.md) | try/except, common error types |
| 9 | [09_file_handling.md](01_python_foundations/09_file_handling.md) | Reading files, writing files |

### 02. NumPy
| # | File | Covers |
|---|------|--------|
| 1 | [01_arrays_basics.md](02_numpy/01_arrays_basics.md) | What is an array, creating arrays, shape/dtype |
| 2 | [02_indexing_and_slicing.md](02_numpy/02_indexing_and_slicing.md) | Basic indexing, slicing, boolean masking |
| 3 | [03_operations.md](02_numpy/03_operations.md) | Vectorization vs loops, broadcasting, math/aggregate functions |
| 4 | [04_reshaping.md](02_numpy/04_reshaping.md) | Reshape, flatten, stack, split |
| 5 | [05_random_numbers.md](02_numpy/05_random_numbers.md) | np.random basics |

### 03. Pandas Core
| # | File | Covers |
|---|------|--------|
| 1 | [01_series.md](03_pandas_core/01_series.md) | What is a Series, basic operations |
| 2 | [02_dataframes_basics.md](03_pandas_core/02_dataframes_basics.md) | What is a DataFrame, creating one, reading CSV/Excel |
| 3 | [03_inspecting_data.md](03_pandas_core/03_inspecting_data.md) | head, tail, info, describe, dtypes |
| 4 | [04_selecting_data.md](03_pandas_core/04_selecting_data.md) | loc, iloc, selecting columns, filtering rows |
| 5 | [05_sorting_and_editing.md](03_pandas_core/05_sorting_and_editing.md) | sort_values, rename/add/drop columns |

### 04. Data Cleaning
| # | File | Covers |
|---|------|--------|
| 1 | [01_missing_data.md](04_data_cleaning/01_missing_data.md) | Finding missing values, dropna, fillna |
| 2 | [02_duplicates.md](04_data_cleaning/02_duplicates.md) | Finding & removing duplicates |
| 3 | [03_transforming_data.md](04_data_cleaning/03_transforming_data.md) | apply, map, string cleaning |
| 4 | [04_outliers.md](04_data_cleaning/04_outliers.md) | IQR method, Z-score method |

### 05. Advanced Analytics
| # | File | Covers |
|---|------|--------|
| 1 | [01_groupby_and_aggregation.md](05_advanced_analytics/01_groupby_and_aggregation.md) | Split-apply-combine, agg() |
| 2 | [02_combining_data.md](05_advanced_analytics/02_combining_data.md) | merge, join, concat |
| 3 | [03_pivot_tables.md](05_advanced_analytics/03_pivot_tables.md) | pivot_table, crosstab |
| 4 | [04_time_series.md](05_advanced_analytics/04_time_series.md) | datetime basics, resampling |

### 06. Data Visualization
| # | File | Covers |
|---|------|--------|
| 1 | [01_matplotlib.md](06_data_visualization/01_matplotlib.md) | Line, bar, pie charts |
| 2 | [02_seaborn.md](06_data_visualization/02_seaborn.md) | histplot, boxplot, countplot, heatmap |

### 07. Capstone Projects
| # | File | Covers |
|---|------|--------|
| 1 | [01_first_eda_project.md](07_capstone_projects/01_first_eda_project.md) | End-to-end exploratory data analysis |

---

## 🗂️ Datasets

Sample datasets used across the notes live in [`datasets/`](datasets/).

## 🛠️ Setup

See [`requirements.txt`](requirements.txt) for the libraries used throughout these notes.

```bash
pip install -r requirements.txt
```

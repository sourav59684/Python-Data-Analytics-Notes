# 🐍 Variables & Type Conversion — Foundations

---

## 📌 What Is a Variable?

A **variable** is just a labeled box where you store a value, so you can use
it again later instead of retyping it.

```python
age = 25
```

Here, `age` is the label (the variable name), and `25` is the value stored
inside it. Whenever you type `age` later in your code, Python replaces it
with `25`.

> 💬 **Key idea:** You don't need to tell Python what *type* of box you want.
> Just give it a name and a value — Python figures out the rest.

---

## 📊 Why This Matters for Data Analytics

Every column you load from a spreadsheet becomes a variable in your code
(usually inside a table-like structure, which you'll meet in Pandas). Before
that, you need to be completely comfortable with the basics: how to name
things sensibly, and how to convert one type into another — because messy
real-world data almost never arrives in the exact type you want.

---

## ✏️ Creating a Variable

```python
name = "Ravi"
age = 25
salary = 45000.50
is_employed = True
```

- Use `=` to assign a value.
- No need to declare a type first — Python does it automatically.
- You can change a variable's value (and even its type) any time:

```python
score = 10        # int
score = "ten"      # now a string — totally legal, just usually not a good idea
```

---

## 📛 Naming Rules & Conventions

### Rules (Python will error if you break these)

| Rule | Example |
|---|---|
| Must start with a letter or underscore | `_score`, `age` ✅ — `1age` ❌ |
| Can contain letters, numbers, underscores | `total_2024` ✅ |
| No spaces allowed | `total sales` ❌ → use `total_sales` |
| Cannot be a Python keyword | `list = 5` ❌ (`list` is a reserved word) |
| Case-sensitive | `Age` and `age` are two different variables |

### Conventions (Python won't error, but these keep code readable)

| Convention | Example | Used For |
|---|---|---|
| `snake_case` | `total_sales`, `customer_name` | Variable names (standard in Python) |
| ALL_CAPS | `TAX_RATE = 0.18` | Values that never change (constants) |
| Descriptive names | `customer_age` not `x` | Anyone reading your code later (including you) |

```python
# ❌ Hard to understand later
x = 45000
y = 0.18
z = x + (x * y)

# ✅ Clear and self-explanatory
salary = 45000
tax_rate = 0.18
salary_after_tax = salary + (salary * tax_rate)
```

---

## 🔄 Type Conversion (Casting)

Sometimes a value comes in the wrong type — most often, numbers arrive as
text (this happens constantly when reading data from files). **Type
conversion** means changing a value from one type to another.

```
"25"  --int()-->  25          (text → whole number)
25    --float()->  25.0        (whole number → decimal)
25.9  --int()-->  25          (decimal → whole number, cuts off decimal, doesn't round)
25    --str()-->  "25"         (number → text)
```

### 🔧 Common Conversion Functions

| Function | Converts To | Example |
|---|---|---|
| `int(x)` | Whole number | `int("25")` → `25` |
| `float(x)` | Decimal number | `float("25.5")` → `25.5` |
| `str(x)` | Text | `str(25)` → `"25"` |
| `bool(x)` | True/False | `bool(0)` → `False`, `bool(5)` → `True` |
| `list(x)` | List | `list("abc")` → `['a','b','c']` |

```python
age_text = "25"
age_number = int(age_text)
print(age_number + 5)     # 30 (works now — it's a real number)
# print(age_text + 5)     # ❌ this would error — can't add text + number
```

---

## 💡 Examples

### 1. Basic — Fixing a number stored as text
```python
price_text = "199.99"
price = float(price_text)
final_price = price * 1.18   # adding 18% tax
print(final_price)           # 235.9882
```
*Explanation:* Data from CSV files often comes in as text, even if it "looks"
like a number. You must convert it before doing any math.

---

### 2. Analytics Use Case — Cleaning a list of "numbers" from a file
```python
raw_values = ["120", "85", "N/A", "300"]

clean_values = []
for val in raw_values:
    try:
        clean_values.append(int(val))
    except ValueError:
        clean_values.append(None)   # can't convert "N/A", so mark as missing

print(clean_values)   # [120, 85, None, 300]
```
*Explanation:* This is a simplified version of what Pandas does automatically
with `pd.to_numeric(..., errors='coerce')` — invalid values become missing
instead of crashing your whole program.

---

### 3. Naming Variables Clearly
```python
# Bad naming — works, but confusing
a = 500
b = 12
c = a * b

# Good naming — self-explanatory
monthly_salary = 500
months = 12
annual_salary = monthly_salary * months
print(annual_salary)   # 6000
```
*Explanation:* Both versions run identically. Only one is understandable six
months from now (or to a teammate reading your code).

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| `1age = 25` | Variable names can't start with a number — use `age_1` |
| `total sales = 500` | No spaces allowed — use `total_sales = 500` |
| Assuming `"5" + 5` works | Convert first: `int("5") + 5` |
| `int("25.5")` | This errors — go through `float()` first: `int(float("25.5"))` |
| Naming a variable `list` or `str` | These are Python's built-in names — reusing them causes confusing bugs later |

---

## ✍️ Practice Questions

1. Why doesn't Python require you to say a variable's type upfront?
2. Convert the text `"42"` into a real number and add `8` to it.
3. Fix this variable name so it follows Python's rules: `2nd_score`
4. What does `int(9.9)` return, and why might that surprise someone?
5. Why is `total_sales` a better variable name than `x`?

<details>
<summary>💡 Click to see answers</summary>

1. Python is **dynamically typed** — it looks at the value you assign and
   figures out the type automatically, so you don't have to declare it.
2. ```python
   value = int("42")
   print(value + 8)   # 50
   ```
3. `2nd_score` is invalid because it starts with a number. Fix: `second_score`.
4. `int(9.9)` returns `9`, not `10` — it **cuts off** the decimal part rather
   than rounding. Use `round(9.9)` if you want proper rounding.
5. `total_sales` explains exactly what the value represents, so anyone
   reading the code (including future you) understands it instantly — `x`
   gives no information at all.

</details>

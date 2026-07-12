# 🐍 Data Types — Foundations

---

## 📌 What Is a Data Type?

A **data type** just tells Python *what kind of value* you're working with — a
number, some text, a yes/no answer, or a list of things.

Python looks at the value you type and figures out the type automatically.
You never have to say "this is a number" — Python just knows.

```python
age = 25          # Python sees this is a whole number
price = 25.50     # Python sees this has a decimal point
name = "Ravi"     # Python sees this is text (it's in quotes)
```

> 💬 **Why this matters:** If you try to do math on text by mistake, Python will
> stop and give you an error. Knowing the types helps you understand *why*.

---

## 📊 Why This Matters for Data Analytics

When you open a spreadsheet or CSV file in Python, every single column is made
of one of these basic types. A "Price" column should be numbers. A "Name"
column should be text. If even one row has the wrong type mixed in (like the
word `"unknown"` inside a number column), your calculations will break.

So before doing anything fancy, you need to be completely comfortable with
these basic building blocks.

---

## 🧱 The Main Data Types

| Type | Name in Python | Example | Used For |
|------|----------------|---------|----------|
| Whole number | `int` | `25` | Counting things (age, quantity) |
| Decimal number | `float` | `25.50` | Prices, percentages, measurements |
| Text | `str` | `"Ravi"` | Names, addresses, any words |
| True/False | `bool` | `True` | Yes/no questions (Is active? Is paid?) |
| Ordered list (changeable) | `list` | `[1, 2, 3]` | A group of related items |
| Ordered list (locked) | `tuple` | `(1, 2, 3)` | A group that should never change |
| Key-value pairs | `dict` | `{"name": "Ravi"}` | Labeled data, like a mini spreadsheet row |
| Unique items only | `set` | `{1, 2, 3}` | A group with no duplicates |
| Nothing / empty | `None` | `None` | "No value yet" or "missing" |

We'll go through each one below.

---

## 1️⃣ Integer (`int`) — Whole Numbers

```python
age = 25
quantity = 10
year = 2026
```

- No decimal point.
- Can be positive or negative.
- Used for counting things.

**Try it:**
```python
apples = 5
oranges = 3
total_fruits = apples + oranges
print(total_fruits)   # 8
```

---

## 2️⃣ Float (`float`) — Decimal Numbers

```python
price = 99.99
temperature = 36.6
discount_rate = 0.15
```

- Has a decimal point — even `10.0` is a float, not an int.
- Used anywhere you need precision, like money or measurements.

**Try it:**
```python
price = 250.0
tax = price * 0.18       # 18% tax
final_price = price + tax
print(final_price)       # 295.0
```

> ⚠️ **Watch out:** `10` and `10.0` look almost the same but are different types
> (`int` vs `float`). This matters later when cleaning data — a column that mixes
> `10` and `10.0` and `"10"` is actually mixing three different types.

### 🔧 Common Methods for Numbers

| Method / Function | What It Does | Example |
|---|---|---|
| `round(x, n)` | Rounds to `n` decimal places | `round(3.14159, 2)` → `3.14` |
| `abs(x)` | Removes the negative sign | `abs(-5)` → `5` |
| `x.is_integer()` | Checks if a float has no decimal part | `(4.0).is_integer()` → `True` |
| `int(x)` | Converts to whole number (cuts off decimals) | `int(9.8)` → `9` |
| `float(x)` | Converts to decimal number | `float(9)` → `9.0` |

```python
price = 299.567
print(round(price, 2))   # 299.57
print(abs(-42))          # 42
```

---

## 3️⃣ String (`str`) — Text

```python
name = "Ravi Kumar"
city = 'Mumbai'          # single or double quotes both work
email = "ravi@email.com"
```

- Always wrapped in quotes.
- You can join (add) strings together, and grab pieces of them.

**Try it:**
```python
first_name = "Ravi"
last_name = "Kumar"
full_name = first_name + " " + last_name
print(full_name)          # Ravi Kumar
print(full_name.upper())  # RAVI KUMAR
print(len(full_name))     # 10 (counts characters, including the space)
```

### 🔧 Common Methods for Strings

| Method | What It Does | Example |
|---|---|---|
| `.upper()` | Converts to CAPITAL letters | `"ravi".upper()` → `"RAVI"` |
| `.lower()` | Converts to small letters | `"RAVI".lower()` → `"ravi"` |
| `.strip()` | Removes extra spaces from both ends | `"  ravi  ".strip()` → `"ravi"` |
| `.replace(old, new)` | Swaps one piece of text for another | `"Ravi".replace("R", "M")` → `"Mavi"` |
| `.split(sep)` | Breaks text into a list, using a separator | `"a,b,c".split(",")` → `['a','b','c']` |
| `.startswith(x)` | Checks if text begins with `x` | `"data.csv".startswith("data")` → `True` |
| `len(text)` | Counts the number of characters | `len("Ravi")` → `4` |

```python
messy_name = "  ravi kumar  "
clean_name = messy_name.strip().title()
print(clean_name)   # "Ravi Kumar"
```
*Explanation:* This exact pattern — `.strip()` then fixing capitalization —
is one of the most common things you'll do when cleaning messy text columns
from a spreadsheet.

---

## 4️⃣ Boolean (`bool`) — True or False

```python
is_active = True
is_paid = False
```

- Only two possible values: `True` or `False`.
- Comes from asking a yes/no question.

**Try it:**
```python
age = 20
is_adult = age >= 18
print(is_adult)     # True
```

> 💡 **Good to know:** Behind the scenes, `True` is treated as `1` and `False`
> as `0`. So `True + True` actually equals `2`. This is used a lot later when
> counting how many rows in a dataset match a condition.

---

## 5️⃣ List (`list`) — A Group of Items You Can Change

```python
fruits = ["apple", "banana", "mango"]
scores = [88, 92, 79, 95]
```

- Written with square brackets `[ ]`.
- Items are in order, and you *can* add, remove, or change items later.

**Try it:**
```python
fruits = ["apple", "banana"]
fruits.append("mango")     # add an item
print(fruits)               # ['apple', 'banana', 'mango']
print(fruits[0])            # 'apple'  → first item (counting starts at 0)
```

### 🔧 Common Methods for Lists

| Method | What It Does | Example |
|---|---|---|
| `.append(x)` | Adds an item to the end | `fruits.append("kiwi")` |
| `.remove(x)` | Removes the first matching item | `fruits.remove("banana")` |
| `.sort()` | Sorts the list in place | `scores.sort()` |
| `.reverse()` | Reverses the order | `fruits.reverse()` |
| `len(list)` | Counts how many items | `len(fruits)` → `3` |
| `sum(list)` | Adds up all numbers in the list | `sum(scores)` |
| `max(list)` / `min(list)` | Largest / smallest value | `max(scores)` |

```python
scores = [88, 92, 79, 95]
scores.sort()
print(scores)          # [79, 88, 92, 95]
print(max(scores))     # 95
print(sum(scores) / len(scores))   # average score → 88.5
```
*Explanation:* `sum()`, `len()`, `max()`, and `min()` are exactly how you'd
calculate a total, count, highest, and lowest by hand — before you learn
Pandas' `.sum()` and `.mean()`, which do the same thing on entire columns.

---

## 6️⃣ Tuple (`tuple`) — A Group of Items That's Locked

```python
coordinates = (28.6, 77.2)
rgb_color = (255, 0, 0)
```

- Written with round brackets `( )`.
- Looks like a list, but **cannot be changed** after it's created.
- Used when the data should never accidentally be edited (like a fixed location).

**Try it:**
```python
point = (10, 20)
print(point[0])   # 10
# point[0] = 99   # ❌ this would give an error — tuples can't be changed
```

### 🔧 Common Methods for Tuples

| Method | What It Does | Example |
|---|---|---|
| `.count(x)` | Counts how many times `x` appears | `(1,2,2,3).count(2)` → `2` |
| `.index(x)` | Finds the position of `x` | `(10,20,30).index(20)` → `1` |
| `len(tuple)` | Counts how many items | `len((1,2,3))` → `3` |

Tuples support far fewer methods than lists — that's the point. Fewer ways to
accidentally change locked data.

---

## 7️⃣ Dictionary (`dict`) — Labeled Data

```python
student = {
    "name": "Ravi",
    "age": 25,
    "city": "Mumbai"
}
```

- Written with curly brackets `{ }`.
- Stores data as **label: value** pairs (like a mini spreadsheet row where
  each column has a name).

**Try it:**
```python
student = {"name": "Ravi", "age": 25}
print(student["name"])     # Ravi
student["age"] = 26        # update a value
print(student)             # {'name': 'Ravi', 'age': 26}
```

### 🔧 Common Methods for Dictionaries

| Method | What It Does | Example |
|---|---|---|
| `.keys()` | Gets all the labels | `student.keys()` → `['name','age']` |
| `.values()` | Gets all the values | `student.values()` → `['Ravi',26]` |
| `.items()` | Gets label-value pairs together | `student.items()` |
| `.get(key)` | Safely fetches a value (no error if missing) | `student.get("city")` → `None` |
| `.update({...})` | Adds/updates multiple values at once | `student.update({"city":"Pune"})` |

```python
student = {"name": "Ravi", "age": 25}
print(student.get("city"))       # None → doesn't crash, unlike student["city"]
for key, value in student.items():
    print(key, "->", value)
```
*Explanation:* `.get()` is the safe way to look up a value that might not
exist — this matters a lot once you're pulling values out of real, messy data.

---

## 8️⃣ Set (`set`) — Only Unique Items

```python
unique_cities = {"Mumbai", "Delhi", "Mumbai", "Pune"}
print(unique_cities)   # {'Mumbai', 'Delhi', 'Pune'}  → duplicate removed automatically
```

- Written with curly brackets `{ }`, but no labels (unlike a dictionary).
- Automatically removes duplicate values.
- Very handy for quickly finding unique values in a dataset.

---

## 9️⃣ None (`NoneType`) — Nothing / Missing

```python
middle_name = None
```

- Means "no value yet" or "this is empty/unknown."
- Different from `0` or `""` (empty text) — those are still values. `None`
  means *there is no value at all.*
- This is exactly what a missing cell in a spreadsheet becomes in Python.

---

## 🔍 How to Check a Value's Type

```python
age = 25
print(type(age))   # <class 'int'>

name = "Ravi"
print(type(name))  # <class 'str'>
```

Use `type()` any time you're unsure what kind of value you're dealing with —
this is one of the most-used commands when exploring a new dataset.

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ What Actually Happens |
|-----------|---------------------------|
| `"5" + 5` | Error — you can't add text and a number directly |
| Forgetting quotes: `name = Ravi` | Error — Python thinks `Ravi` is a variable name, not text |
| Mixing up `=` and `==` | `=` sets a value, `==` checks if two values are equal |
| Thinking `10` and `"10"` are the same | They're different types — one's a number, one's text |
| Trying to change a tuple | Tuples are locked once created — use a list instead if you need to change it |

---

## ✍️ Practice Questions

1. What type is `3.0`? Is it the same as `3`?
2. What will `type("100")` print?
3. Create a list of your 3 favorite foods, then print just the second one.
4. Why would you use a tuple instead of a list?
5. What does `True + True + False` equal, and why?

<details>
<summary>💡 Click to see answers</summary>

1. `3.0` is a `float`. It is *not* the same type as `3` (`int`), even though
   they're mathematically equal.
2. `<class 'str'>` — even though it looks like a number, it's in quotes, so
   it's text.
3. ```python
   foods = ["pizza", "pasta", "biryani"]
   print(foods[1])   # pasta
   ```
4. Use a tuple when the values should never change — like GPS coordinates or
   a fixed date of birth.
5. `2` — because `True` counts as `1` and `False` counts as `0`, so
   `1 + 1 + 0 = 2`.

</details>

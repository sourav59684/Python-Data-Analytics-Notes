# 🐍 Operators — Foundations

---

## 📌 What Is an Operator?

An **operator** is a symbol that tells Python to *do something* with values —
add them, compare them, or combine conditions.

```python
total = 10 + 5   # + is the operator, 10 and 5 are the values (called operands)
```

---

## 📊 Why This Matters for Data Analytics

Operators are how you calculate totals, compare values, and filter data.
Every time you write "show me sales greater than 1000" or "flag rows where
age is missing," you're using operators — this is the backbone of filtering
and calculating in Pandas later.

---

## 🧮 1. Arithmetic Operators — Math

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division (always gives decimal) | `10 / 4` | `2.5` |
| `//` | Floor division (rounds down, no decimal) | `10 // 4` | `2` |
| `%` | Modulus (remainder after division) | `10 % 4` | `2` |
| `**` | Power (exponent) | `2 ** 3` | `8` |

```python
total_items = 47
items_per_box = 10
full_boxes = total_items // items_per_box   # 4 full boxes
leftover = total_items % items_per_box      # 7 items left over
print(full_boxes, leftover)   # 4 7
```
*Explanation:* `//` and `%` together are exactly how you'd split items into
groups by hand — very useful for bucketing data (e.g., grouping ages into
decades).

---

## ⚖️ 2. Comparison Operators — Comparing Values

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `10 > 5` | `True` |
| `<` | Less than | `10 < 5` | `False` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `4 <= 5` | `True` |

> ⚠️ **Watch out:** `=` sets a value. `==` checks if two values are equal.
> Mixing these up is one of the most common beginner errors.

```python
sales = 1200
target = 1000
print(sales >= target)   # True → target achieved
```

---

## 🔗 3. Logical Operators — Combining Conditions

| Operator | Meaning | Example |
|---|---|---|
| `and` | True only if **both** conditions are true | `age > 18 and has_id == True` |
| `or` | True if **at least one** condition is true | `is_vip or total > 5000` |
| `not` | Flips True to False, and False to True | `not is_active` |

```python
age = 25
has_ticket = True

can_enter = age >= 18 and has_ticket
print(can_enter)   # True — both conditions are true
```
*Explanation:* This is exactly the logic you'll later write as filter
conditions in Pandas — e.g., "show customers where age > 18 AND active == True."

---

## 📝 4. Assignment Operators — Shortcuts for Updating a Value

| Operator | Meaning | Same As |
|---|---|---|
| `=` | Assign a value | `x = 5` |
| `+=` | Add and reassign | `x = x + 5` |
| `-=` | Subtract and reassign | `x = x - 5` |
| `*=` | Multiply and reassign | `x = x * 5` |
| `/=` | Divide and reassign | `x = x / 5` |

```python
total_sales = 1000
total_sales += 250   # same as total_sales = total_sales + 250
print(total_sales)   # 1250
```

---

## 🔎 5. Membership & Identity Operators

| Operator | Meaning | Example |
|---|---|---|
| `in` | Checks if a value exists inside a list/string | `"a" in "apple"` → `True` |
| `not in` | Checks if a value does NOT exist | `"z" in "apple"` → `False` |
| `is` | Checks if two variables point to the exact same object | `x is None` |
| `is not` | Opposite of `is` | `x is not None` |

```python
fruits = ["apple", "banana", "mango"]
print("banana" in fruits)       # True
print("grape" not in fruits)    # True

value = None
print(value is None)            # True — this is the correct way to check for "no value"
```
*Explanation:* `in` is extremely common for checking if something exists in
a dataset (like checking if a column name is present). `is None` is always
the correct way to check for missing values — never use `== None`.

---

## 💡 Examples

### 1. Basic — Simple calculator
```python
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a % b)
# 13 7 30 3.3333333333333335 1
```

### 2. Analytics Use Case — Checking if a sale qualifies for a bonus
```python
sales_amount = 15000
is_repeat_customer = True

qualifies_for_bonus = sales_amount > 10000 and is_repeat_customer
print(qualifies_for_bonus)   # True
```

### 3. Combining Comparison + Logical Operators
```python
age = 17
has_guardian = True

can_watch_movie = age >= 18 or (age >= 13 and has_guardian)
print(can_watch_movie)   # True — under 18, but has a guardian
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| `if x = 5:` | Use `==` for comparison, `=` is only for assignment |
| `10 / 3` expecting a whole number | `/` always gives a decimal — use `//` for whole numbers |
| `value == None` | Use `value is None` — it's the correct and faster way |
| Forgetting operator order (`2 + 3 * 4`) | Python follows math rules: multiplication happens before addition — use `()` to be explicit |
| `and`/`or` typed as `&&`/`||` (from other languages) | Python uses the words `and` and `or`, not symbols |

---

## ✍️ Practice Questions

1. What does `17 % 5` give you, and what does it represent?
2. Write a condition that checks if a number is between 10 and 20 (inclusive).
3. What's wrong with this code: `if score = 90:`
4. What does `"cat" in "concatenate"` return?
5. Why should you use `is None` instead of `== None`?

<details>
<summary>💡 Click to see answers</summary>

1. `17 % 5` gives `2` — it's the remainder left over after dividing 17 by 5
   (5 goes into 17 three times = 15, remainder 2).
2. ```python
   number = 15
   print(10 <= number <= 20)   # True
   ```
3. It uses `=` (assignment) instead of `==` (comparison) — this is a syntax
   error in an `if` statement. Should be `if score == 90:`
4. `True` — `"cat"` appears inside the letters of `"concatenate"`.
5. `is None` checks identity directly and is the Python-recommended way to
   check for missing values; `== None` technically works most of the time but
   is considered bad practice and can behave unexpectedly with custom objects.

</details>

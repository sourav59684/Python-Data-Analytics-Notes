# 🐍 Error Handling — try/except

---

## 📌 What Is Error Handling?

Sometimes code fails while running — dividing by zero, converting text that
isn't really a number, opening a file that doesn't exist. Instead of letting
your entire program crash, **error handling** lets you catch the problem and
decide what to do instead.

```python
age = int("twenty-five")   # ❌ this crashes the program
```

```python
try:
    age = int("twenty-five")
except:
    print("That wasn't a valid number!")
    age = None
# program keeps running instead of crashing
```

---

## 📊 Why This Matters for Data Analytics

Real datasets are messy. A "price" column might have a stray `"unknown"`
value. An API might not respond. A file might be missing. Without error
handling, one bad row can crash a script that was processing thousands of
good rows. Handling errors gracefully means your code can skip or flag the
bad data and keep going.

---

## 🏗️ Basic Structure

```
try:
    # code that might fail
except SomeErrorType:
    # what to do if that specific error happens
else:
    # runs only if NO error happened
finally:
    # always runs, error or not
```

| Part | Required? | Purpose |
|---|---|---|
| `try` | ✅ Yes | The code you want to attempt |
| `except` | ✅ Yes (at least one) | What to do if it fails |
| `else` | Optional | Runs only if `try` succeeded |
| `finally` | Optional | Always runs — good for cleanup |

---

## 🚨 Common Error Types

| Error | Happens When | Example |
|---|---|---|
| `ValueError` | A value is the right type but wrong content | `int("hello")` |
| `TypeError` | An operation is used on the wrong type | `"5" + 5` |
| `ZeroDivisionError` | Dividing by zero | `10 / 0` |
| `KeyError` | A dictionary key doesn't exist | `student["email"]` when it's not there |
| `IndexError` | A list index is out of range | `fruits[10]` when there are only 3 items |
| `FileNotFoundError` | Trying to open a file that doesn't exist | `open("missing.csv")` |

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")
```

> 💡 **Catching specific errors is better than catching everything.** A bare
> `except:` catches *every* error, even ones you didn't expect — making bugs
> harder to find. Name the error type when you can.

---

## 💡 Examples

### 1. Basic — Handling a bad conversion
```python
values = ["10", "20", "abc", "40"]

for val in values:
    try:
        number = int(val)
        print("Converted:", number)
    except ValueError:
        print("Skipping invalid value:", val)
```

### 2. Analytics Use Case — Safely processing a messy dataset
```python
raw_prices = ["199.99", "N/A", "250", "", "89.50"]
clean_prices = []

for price in raw_prices:
    try:
        clean_prices.append(float(price))
    except ValueError:
        clean_prices.append(None)   # mark as missing instead of crashing

print(clean_prices)   # [199.99, None, 250.0, None, 89.5]
```
*Explanation:* This exact pattern — try to convert, fall back to `None` on
failure — is what lets you clean an entire messy column without your script
stopping on the first bad value.

### 3. Using else and finally
```python
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("Attempted division of", a, "by", b)

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

### 4. Catching Multiple Error Types
```python
data = {"name": "Ravi", "age": "25"}

try:
    email = data["email"]          # this key doesn't exist
except KeyError:
    print("Email not found in record")
except TypeError:
    print("Data isn't in the expected format")
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Using a bare `except:` for everything | Catch specific error types so you know exactly what went wrong |
| Ignoring errors silently with just `pass` | At least log or print what happened — silent failures are hard to debug |
| Wrapping the entire program in one giant `try` | Wrap only the specific risky lines — makes it clear what could fail |
| Using try/except to hide bugs instead of fixing them | Error handling is for *expected* problems (bad data), not a substitute for fixing broken logic |

---

## ✍️ Practice Questions

1. What's the difference between a `ValueError` and a `TypeError`?
2. Write a try/except that safely converts `"abc"` to an integer without crashing.
3. When does the `finally` block run?
4. Why is `except:` (with nothing specified) considered bad practice?
5. What error would `[1, 2, 3][10]` cause?

<details>
<summary>💡 Click to see answers</summary>

1. A `ValueError` happens when a value has the right type but invalid
   content (like `int("hello")`). A `TypeError` happens when an operation is
   used on an incompatible type (like `"5" + 5`).
2. ```python
   try:
       number = int("abc")
   except ValueError:
       print("Invalid number")
       number = None
   ```
3. `finally` always runs — whether or not an error happened — making it
   useful for cleanup tasks like closing a file.
4. It catches *every* type of error, including ones you didn't anticipate,
   which can hide real bugs and make debugging much harder.
5. `IndexError` — the list only has 3 items (indexes 0, 1, 2), so index `10`
   doesn't exist.

</details>

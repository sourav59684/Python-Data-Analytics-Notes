# 🐍 Functions — Foundations

---

## 📌 What Is a Function?

A **function** is a reusable block of code that performs a task. You write
it once, then "call" (use) it as many times as you want, with different
inputs, without rewriting the logic every time.

```python
def greet(name):
    print("Hello,", name)

greet("Ravi")    # Hello, Ravi
greet("Anu")     # Hello, Anu
```

Think of it like a recipe: you write the steps once, then you can "cook it"
(run it) any time with different ingredients (inputs).

---

## 📊 Why This Matters for Data Analytics

You'll constantly write small functions to clean or transform data — like
"convert this messy date format" or "categorize this age into a group."
Instead of repeating that logic for every row by hand, you write it once as
a function and apply it to the entire dataset in one line.

---

## 🏗️ Anatomy of a Function

```
def function_name(parameter1, parameter2):
    # code that runs when the function is called
    return result
```

| Part | Meaning |
|---|---|
| `def` | Keyword that starts a function definition |
| `function_name` | The name you'll use to call it later |
| `parameters` | Inputs the function expects (optional) |
| `return` | Sends a value back out of the function (optional) |

```python
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print(total)   # 8
```

> ⚠️ **`print()` vs `return`:** `print()` just displays something on screen.
> `return` actually sends the value back so you can store it in a variable
> and use it elsewhere. A function without `return` gives you `None`.

---

## 🎛️ Parameters & Arguments

| Term | Meaning |
|---|---|
| **Parameter** | The placeholder name inside the function definition |
| **Argument** | The actual value you pass in when calling the function |

```python
def multiply(x, y):     # x, y are parameters
    return x * y

print(multiply(4, 5))   # 4, 5 are arguments → 20
```

### Default Arguments

Give a parameter a fallback value, used only if the caller doesn't provide one.

```python
def apply_discount(price, discount=0.10):
    return price - (price * discount)

print(apply_discount(1000))         # 900.0  → uses default 10%
print(apply_discount(1000, 0.25))   # 750.0  → overrides default with 25%
```

### Keyword Arguments

Pass arguments by name instead of position — makes calls clearer, especially
with many parameters.

```python
def create_profile(name, age, city):
    print(f"{name}, {age}, {city}")

create_profile(city="Mumbai", name="Ravi", age=25)
# Ravi, 25, Mumbai  → order doesn't matter when using names
```

---

## 🔧 Common Function-Related Tools

| Tool | What It Does | Example |
|---|---|---|
| `return` | Sends a value back from the function | `return total` |
| `return` (multiple values) | Can return more than one value at once | `return name, age` |
| `*args` | Accepts any number of extra positional arguments | `def total(*nums): return sum(nums)` |
| `**kwargs` | Accepts any number of extra named arguments | `def info(**details): print(details)` |
| `help(func)` | Shows a function's docstring/help text | `help(print)` |

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

lowest, highest, average = get_stats([10, 20, 30, 40])
print(lowest, highest, average)   # 10 40 25.0
```

---

## ⚡ Lambda Functions — Small, One-Line Functions

A **lambda** is a mini function written in a single line, usually for quick,
throwaway logic — you'll see this a LOT when using Pandas' `.apply()` later.

```python
# Regular function
def square(x):
    return x ** 2

# Same thing as a lambda
square = lambda x: x ** 2

print(square(5))   # 25
```

```
lambda parameters: expression
```

```python
# Used inline, without even naming it — very common with data
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)   # [1, 4, 9, 16, 25]
```

> 💡 **Rule of thumb:** Use `lambda` for short, simple one-line logic. Use a
> regular `def` function for anything with multiple steps — lambdas get hard
> to read fast if you cram too much into them.

---

## 💡 Examples

### 1. Basic — A function with no inputs
```python
def show_welcome():
    print("Welcome to the data analytics course!")

show_welcome()
```

### 2. Analytics Use Case — Categorizing a value
```python
def age_group(age):
    if age < 18:
        return "Minor"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

ages = [15, 25, 70, 45]
for a in ages:
    print(a, "->", age_group(a))
```
*Explanation:* This exact function, written once here, is the kind of thing
you'll later pass directly into `df['age'].apply(age_group)` to label an
entire column in one line.

### 3. Using default arguments for flexible reusability
```python
def calculate_total(price, quantity, tax_rate=0.18):
    subtotal = price * quantity
    return subtotal + (subtotal * tax_rate)

print(calculate_total(500, 2))          # uses default 18% tax
print(calculate_total(500, 2, 0.05))    # overrides to 5% tax
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting `return` and expecting a value back | Without `return`, a function gives you `None` |
| Confusing `print()` with `return` | `print()` only displays; `return` actually gives the value back to use |
| Forgetting the colon `:` after `def function_name():` | Every function header needs a colon |
| Writing overly complex lambdas | If it needs more than one line of logic, use a regular `def` function |
| Not giving default values when it makes sense | Reduces how often callers need to pass every single argument |

---

## ✍️ Practice Questions

1. What's the difference between a parameter and an argument?
2. Write a function `is_even(n)` that returns `True` if `n` is even.
3. What does a function return if you never write a `return` statement?
4. Convert this function into a lambda: `def double(x): return x * 2`
5. Why would you use a default argument in a function?

<details>
<summary>💡 Click to see answers</summary>

1. A **parameter** is the placeholder name in the function definition. An
   **argument** is the actual value you pass in when calling the function.
2. ```python
   def is_even(n):
       return n % 2 == 0
   ```
3. It returns `None` — Python doesn't send back any value unless you
   explicitly use `return`.
4. ```python
   double = lambda x: x * 2
   ```
5. So callers don't have to specify every argument every time — the function
   still works with sensible defaults, but can still be customized when needed.

</details>

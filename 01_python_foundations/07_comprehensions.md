# 🐍 Comprehensions — List & Dict

---

## 📌 What Is a Comprehension?

A **comprehension** is a short, one-line way to build a new list (or
dictionary) from an existing one — instead of writing a full `for` loop with
multiple lines.

```python
# The long way (a regular for loop)
squares = []
for n in [1, 2, 3, 4]:
    squares.append(n ** 2)

# The short way (a list comprehension) — does the exact same thing
squares = [n ** 2 for n in [1, 2, 3, 4]]

print(squares)   # [1, 4, 9, 16]
```

> 💬 **Key idea:** A comprehension isn't a new concept — it's just a shorter
> way to write a `for` loop that builds a list.

---

## 📊 Why This Matters for Data Analytics

You'll constantly need to transform a whole column of values in one shot —
"convert all these prices from text to numbers," "make every name lowercase."
Comprehensions are the clean, readable way to do that in plain Python, and
the mental model carries directly into Pandas, where entire columns get
transformed in a single line.

---

## 🏗️ List Comprehension — Structure

```
[expression for item in collection]

[expression for item in collection if condition]
```

| Part | Meaning |
|---|---|
| `expression` | What to do with each item before adding it to the new list |
| `item` | The variable representing each element, one at a time |
| `collection` | The list/range/string you're looping through |
| `if condition` (optional) | Only include items that pass this check |

---

## 💡 Examples — List Comprehension

### 1. Basic — Doubling every number
```python
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]
print(doubled)   # [2, 4, 6, 8, 10]
```

### 2. With a Condition — Keep only even numbers
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = [n for n in numbers if n % 2 == 0]
print(evens)   # [2, 4, 6, 8]
```
*Explanation:* Adding `if condition` at the end filters items — only ones
that pass the check make it into the new list.

### 3. Analytics Use Case — Cleaning a list of names
```python
raw_names = [" ravi ", "ANU", "Simran  "]
clean_names = [name.strip().title() for name in raw_names]
print(clean_names)   # ['Ravi', 'Anu', 'Simran']
```
*Explanation:* This single line replaces a 4-line `for` loop, and it's
exactly the kind of cleanup you'll do on real text columns.

### 4. Combining a Function with a Comprehension
```python
def is_valid_price(price):
    return price > 0

prices = [100, -50, 200, -10, 300]
valid_prices = [p for p in prices if is_valid_price(p)]
print(valid_prices)   # [100, 200, 300]
```

---

## 📖 Dictionary Comprehension

Same idea, but builds a dictionary (label: value pairs) instead of a list.

```
{key_expression: value_expression for item in collection}
```

### 🔧 Examples

```python
# Basic — build a dictionary of number: square
squares_dict = {n: n ** 2 for n in range(1, 6)}
print(squares_dict)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
# Analytics use case — turn two lists into a dictionary
names = ["Ravi", "Anu", "Simran"]
scores = [85, 92, 78]

name_scores = {name: score for name, score in zip(names, scores)}
print(name_scores)   # {'Ravi': 85, 'Anu': 92, 'Simran': 78}
```
*Explanation:* `zip()` pairs up two lists item by item — very handy when you
have separate lists of labels and values that belong together.

```python
# With a condition — keep only passing scores
name_scores = {"Ravi": 85, "Anu": 45, "Simran": 78}
passed = {name: score for name, score in name_scores.items() if score >= 60}
print(passed)   # {'Ravi': 85, 'Simran': 78}
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Cramming too much logic into one comprehension | If it's hard to read in one line, just use a regular `for` loop instead |
| Forgetting the brackets `[ ]` for list, `{ }` for dict | `[x for x in ...]` vs `{k: v for ... }` — easy to mix up |
| Using `if/else` incorrectly in a comprehension | For if/else (not filtering), put it before the `for`: `[x if x>0 else 0 for x in nums]` |
| Overusing comprehensions where a named function is clearer | Comprehensions are for simple transforms — complex logic deserves a proper function |

---

## ✍️ Practice Questions

1. Convert this loop into a list comprehension:
   ```python
   result = []
   for x in range(1, 6):
       result.append(x * 10)
   ```
2. Write a list comprehension that keeps only words longer than 3 letters
   from `["cat", "elephant", "dog", "giraffe"]`.
3. What's the difference between a list comprehension and a dict comprehension?
4. Build a dictionary comprehension that maps each number 1-5 to whether it's even (`True`/`False`).
5. When should you NOT use a comprehension?

<details>
<summary>💡 Click to see answers</summary>

1. ```python
   result = [x * 10 for x in range(1, 6)]
   ```
2. ```python
   words = ["cat", "elephant", "dog", "giraffe"]
   long_words = [w for w in words if len(w) > 3]
   print(long_words)   # ['elephant', 'giraffe']
   ```
3. A list comprehension builds a `list` using `[ ]`. A dict comprehension
   builds a `dict` using `{ }` and needs both a key and a value expression.
4. ```python
   even_check = {n: n % 2 == 0 for n in range(1, 6)}
   print(even_check)   # {1: False, 2: True, 3: False, 4: True, 5: False}
   ```
5. When the logic is complex or spans multiple steps — cramming it into one
   line hurts readability. A regular `for` loop or a named function is
   clearer in that case.

</details>

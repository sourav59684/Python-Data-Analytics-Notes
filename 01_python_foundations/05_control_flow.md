# 🐍 Control Flow — if/else & Loops

---

## 📌 What Is Control Flow?

**Control flow** is how you tell Python to make decisions and repeat actions
— instead of running every line exactly once, top to bottom.

Two main tools:
- **if/else** → "Do this ONLY IF a condition is true"
- **loops** → "Do this AGAIN AND AGAIN, for every item"

---

## 📊 Why This Matters for Data Analytics

Control flow is how you filter data ("only show rows where sales > 1000")
and process data row by row ("check every customer's status"). Pandas will
later do most of this for you automatically and much faster — but you need
to understand the logic first, because it's exactly what's happening under
the hood.

---

## 🔀 1. if / elif / else — Making Decisions

```python
age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

```
if condition:
    → runs if condition is True
elif another_condition:
    → runs if the first was False, but this one is True
else:
    → runs if none of the above were True
```

> ⚠️ **Indentation matters in Python.** The code inside `if` must be indented
> (usually 4 spaces). Python uses indentation instead of `{ }` to know what
> belongs inside the block.

### Multiple Conditions with `elif`

```python
score = 75

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(grade)   # B
```
*Explanation:* Python checks conditions top to bottom and stops at the first
`True` one — order matters.

---

## 🔁 2. for Loops — Repeat for Each Item

A `for` loop goes through a collection (list, string, range of numbers) one
item at a time.

```python
fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)
# apple
# banana
# mango
```

### Looping Over a Range of Numbers

```python
for i in range(1, 6):    # 1, 2, 3, 4, 5 (stops before 6)
    print(i)
```

| `range()` version | Produces |
|---|---|
| `range(5)` | `0, 1, 2, 3, 4` |
| `range(1, 5)` | `1, 2, 3, 4` |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` (step of 2) |

---

## 🔂 3. while Loops — Repeat Until a Condition Becomes False

```python
count = 1

while count <= 5:
    print(count)
    count += 1     # very important! without this, the loop never ends
```

> ⚠️ **Watch out:** Forgetting to update the variable inside a `while` loop
> creates an **infinite loop** — your code will run forever and freeze.

**When to use `for` vs `while`:**

| Use `for` when... | Use `while` when... |
|---|---|
| You know how many items you're looping through (a list, a range) | You don't know exactly how many times — you loop "until something happens" |

---

## ⏭️ 4. break, continue, pass

| Keyword | What It Does |
|---|---|
| `break` | Stops the loop completely, right now |
| `continue` | Skips the rest of this round, moves to the next item |
| `pass` | Does nothing — a placeholder so empty code doesn't error |

```python
# break example — stop as soon as we find it
numbers = [4, 8, 15, 16, 23, 42]
for num in numbers:
    if num == 15:
        print("Found 15!")
        break

# continue example — skip negative numbers, keep going
values = [10, -5, 20, -8, 30]
for val in values:
    if val < 0:
        continue
    print(val)   # 10, 20, 30 (negatives skipped)

# pass example — placeholder while you build the logic later
for num in numbers:
    if num > 100:
        pass   # TODO: handle this case later
```

---

## 💡 Examples

### 1. Basic — Grading students
```python
scores = [95, 67, 45, 82]

for score in scores:
    if score >= 90:
        print(score, "-> A")
    elif score >= 60:
        print(score, "-> B")
    else:
        print(score, "-> Fail")
```

### 2. Analytics Use Case — Counting how many sales exceed a target
```python
sales = [1200, 800, 1500, 300, 2000]
target = 1000
count_above_target = 0

for sale in sales:
    if sale > target:
        count_above_target += 1

print(count_above_target)   # 3
```
*Explanation:* This manual counting pattern is exactly what Pandas replaces
with a single line later: `(df['sales'] > 1000).sum()`.

### 3. Combining a while loop with break
```python
attempts = 0
correct_password = "data123"

while True:
    entered = "data123"   # imagine this comes from user input
    attempts += 1
    if entered == correct_password:
        print("Access granted after", attempts, "attempt(s)")
        break
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting the colon `:` after `if`/`for`/`while` | Every block header needs a colon: `if age > 18:` |
| Wrong or missing indentation | Python requires consistent indentation to know what's inside a block |
| Forgetting to update the loop variable in `while` | Always change the condition variable inside the loop, or it runs forever |
| Using `=` instead of `==` in a condition | `=` assigns, `==` compares |
| Confusing `break` and `continue` | `break` exits the whole loop, `continue` just skips to the next round |

---

## ✍️ Practice Questions

1. Write an if/else that prints "Even" or "Odd" for a given number.
2. What does `range(2, 10, 3)` produce?
3. What's the danger of writing a `while` loop without updating the condition variable?
4. What's the difference between `break` and `continue`?
5. Loop through `[5, 12, 8, 20, 3]` and print only numbers greater than 10.

<details>
<summary>💡 Click to see answers</summary>

1. ```python
   number = 7
   if number % 2 == 0:
       print("Even")
   else:
       print("Odd")
   ```
2. `2, 5, 8` — starts at 2, adds 3 each time, stops before 10.
3. It creates an **infinite loop** — the condition never becomes False, so
   the program runs forever and freezes.
4. `break` stops the loop entirely and exits it. `continue` only skips the
   current round and moves on to the next item in the loop.
5. ```python
   numbers = [5, 12, 8, 20, 3]
   for num in numbers:
       if num > 10:
           print(num)
   # 12, 20
   ```

</details>

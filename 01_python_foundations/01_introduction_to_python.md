# 🐍 Introduction to Python

---

## 📌 What Is Python?

Python is a **programming language** — a way of giving instructions to a
computer using text, instead of clicking buttons.

You write instructions (called **code**), the computer reads them line by
line, and it does exactly what you told it to do.

```python
print("Hello, I am learning Python!")
```

Run this one line, and the computer prints that sentence on screen. That's it
— that's a working Python program.

> 💬 **Key idea:** A computer doesn't "understand" English. Python is a
> simplified, strict language that both humans and computers can read —
> it's the middle ground between the two.

---

## 📊 Why Python for Data Analytics?

Python is one of the most popular languages for working with data, and for a
few practical reasons:

| Reason | Why It Matters |
|---|---|
| **Easy to read** | Code looks close to plain English, so beginners pick it up fast |
| **Huge data libraries** | Tools like **Pandas** and **NumPy** are built specifically for working with data tables and numbers |
| **Free and open-source** | No license cost, runs on Windows/Mac/Linux |
| **Connects everything** | Can pull data from Excel, CSV files, databases, websites, and APIs |
| **Widely used in industry** | Data analysts, data scientists, and analytics teams use it daily |

In this repo, you'll learn plain Python first (this section), then two
libraries built on top of it:
- **NumPy** — for fast number calculations
- **Pandas** — for working with data tables (like Excel, but through code)

---

## 🏗️ How Python Code Actually Runs

```
You write code (a .py file or a notebook cell)
        │
        ▼
Python reads it line by line, top to bottom
        │
        ▼
Each line is turned into instructions the computer understands
        │
        ▼
The result (output) is shown to you
```

Python runs your code **one line at a time, in order** — unless you tell it
to skip, repeat, or jump (which you'll learn in the Control Flow file later).

---

## 💻 Ways to Write and Run Python

| Method | What It Is | Best For |
|---|---|---|
| **Python Shell / Terminal** | Type one line, see the result immediately | Quick tests |
| **.py file** | A text file full of code, run all at once | Full programs, projects |
| **Jupyter Notebook** | Code split into "cells" you run one at a time, with output shown right below each cell | Data analysis — this is what most data analysts use daily |

> 💡 **For this repo:** Most data analytics work (and most examples going
> forward) will assume a Jupyter Notebook, because you can run a small piece
> of code, see the result immediately, and keep building step by step.

---

## 💡 Examples

### 1. Your First Line of Code
```python
print("Hello, World!")
```
*Explanation:* `print()` is a built-in command that displays whatever you put
inside the brackets. This is usually the very first thing anyone types in any
programming language.

---

### 2. Python as a Calculator
```python
print(10 + 5)
print(20 / 4)
print(3 * 7)
```
*Explanation:* Before working with data, it helps to know Python can do basic
math directly — this becomes useful for quick calculations while analyzing numbers.

---

### 3. A Tiny Taste of "Data Analytics" Already
```python
sales = [200, 450, 300, 150]
total_sales = sum(sales)
print("Total Sales:", total_sales)
```
*Explanation:* This is a preview of what's coming — storing numbers together
and calculating something useful from them. You'll do this constantly with
Pandas later, just on a much bigger scale (thousands of rows instead of 4).

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting brackets: `print "Hello"` | Always use brackets: `print("Hello")` |
| Mixing up capital and small letters: `Print()` | Python is case-sensitive — it must be lowercase `print()` |
| Forgetting quotes around text: `print(Hello)` | Text always needs quotes: `print("Hello")` |
| Expecting code to run out of order | Python runs top to bottom, one line after another |

---

## ✍️ Practice Questions

1. What is the difference between a programming language and English?
2. Write one line of code that prints your name.
3. What are the three ways to run Python code mentioned above?
4. Why is Python popular specifically for data analytics work?

<details>
<summary>💡 Click to see answers</summary>

1. English is flexible and full of ambiguity — the same sentence can mean
   different things. A programming language like Python has strict, fixed
   rules, so the computer always understands exactly what to do.
2. ```python
   print("Ravi Kumar")
   ```
3. Python Shell/Terminal, a `.py` file, and Jupyter Notebook.
4. Because it's easy to read for beginners, and it has powerful free
   libraries (NumPy and Pandas) built specifically for working with numbers
   and data tables.

</details>

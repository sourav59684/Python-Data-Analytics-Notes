# 🐍 File Handling — Reading & Writing Files

---

## 📌 What Is File Handling?

**File handling** means using Python to open, read, write, or update files
saved on your computer — text files, CSVs, logs, and more.

```python
file = open("notes.txt", "r")   # open in "read" mode
content = file.read()
file.close()                    # always close it when done
```

> 💬 **Why this matters:** Before you ever load a spreadsheet with Pandas,
> you're really just opening a file. Understanding the basics helps you
> understand what Pandas is doing behind the scenes.

---

## 📊 Why This Matters for Data Analytics

Every dataset you'll ever analyze starts as a file — a CSV export, an Excel
sheet, a text log. Data analysts need to know how files work: how to open
them safely, read their contents, and write results back out (like saving a
cleaned dataset or a summary report).

---

## 🏗️ File Modes

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) — file must already exist |
| `"w"` | Write — creates a new file, or **erases** an existing one |
| `"a"` | Append — adds to the end of an existing file, without erasing it |
| `"r+"` | Read and write |

```python
open("data.txt", "r")   # read only
open("data.txt", "w")   # write (overwrites!)
open("data.txt", "a")   # append (adds to the end)
```

> ⚠️ **Watch out:** Opening a file in `"w"` mode **erases everything** in it
> first, even if you haven't written anything new yet. Use `"a"` if you want
> to keep existing content.

---

## ✅ The Safe Way: `with open(...)`

Always prefer `with open(...)` over manually calling `open()` and `close()`.
It automatically closes the file for you, even if an error happens partway through.

```python
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
# file is automatically closed here — no need to call file.close()
```

---

## 🔧 Common File Methods

| Method | What It Does |
|---|---|
| `.read()` | Reads the entire file as one string |
| `.readline()` | Reads just one line |
| `.readlines()` | Reads all lines into a list of strings |
| `.write(text)` | Writes text to the file |
| `.writelines(list)` | Writes a list of strings to the file |
| `.close()` | Closes the file (not needed if you used `with`) |

```python
with open("notes.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())   # .strip() removes the extra newline character
```

---

## 💡 Examples

### 1. Basic — Reading a text file
```python
with open("notes.txt", "r") as file:
    content = file.read()
print(content)
```

### 2. Writing to a new file
```python
with open("summary.txt", "w") as file:
    file.write("Total Sales: 15000\n")
    file.write("Total Customers: 320\n")
```
*Explanation:* This is how you'd save a quick summary report after
processing some data — very similar to how you'll later use
`df.to_csv("summary.csv")` in Pandas.

### 3. Analytics Use Case — Reading raw sales data line by line
```python
with open("sales.txt", "r") as file:
    total = 0
    for line in file:
        try:
            total += float(line.strip())
        except ValueError:
            continue   # skip any line that isn't a valid number

print("Total Sales:", total)
```
*Explanation:* Combines file reading with error handling (from the previous
file) — a very realistic pattern for processing raw text data before you
have Pandas to do it for you.

### 4. Appending new records without erasing old ones
```python
with open("log.txt", "a") as file:
    file.write("New customer added: Ravi Kumar\n")
```

---

## 🚨 Common Beginner Mistakes

| ❌ Mistake | ✅ Correct Approach |
|---|---|
| Forgetting to close a file (`file.close()`) | Use `with open(...) as file:` — it closes automatically |
| Using `"w"` mode when you meant to keep existing data | Use `"a"` (append) to add without erasing |
| Forgetting `.strip()` and getting extra blank lines/spaces | Always `.strip()` text read from a file before using it |
| Assuming a file exists | Wrap file operations in `try/except FileNotFoundError` for safety |
| Reading a huge file all at once with `.read()` | For very large files, read line by line instead of loading everything into memory |

---

## ✍️ Practice Questions

1. What's the difference between `"w"` mode and `"a"` mode?
2. Why is `with open(...) as file:` preferred over manually calling `open()` and `close()`?
3. Write code that safely opens a file that might not exist, without crashing.
4. What does `.readlines()` return?
5. What does `.strip()` remove from a line of text, and why is it usually needed?

<details>
<summary>💡 Click to see answers</summary>

1. `"w"` mode creates a new file or **erases** an existing one before
   writing. `"a"` mode adds new content to the **end** of an existing file
   without deleting what's already there.
2. `with` automatically closes the file when you're done, even if an error
   happens inside the block — preventing files from being left open by accident.
3. ```python
   try:
       with open("missing.txt", "r") as file:
           content = file.read()
   except FileNotFoundError:
       print("File not found!")
   ```
4. It returns a **list of strings**, where each item is one line from the
   file (including the newline character at the end of each line).
5. `.strip()` removes extra whitespace and the newline character (`\n`) from
   the start and end of a line — needed because every line read from a file
   includes that trailing newline by default.

</details>

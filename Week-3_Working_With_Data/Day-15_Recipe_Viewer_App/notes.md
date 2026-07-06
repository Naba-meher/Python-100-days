# Day 15 Notes

## Learned
- Use `open()` to read files.
- The `with` statement automatically closes files.
- Read files using `read()`, `readline()`, or `readlines()`.
- Handle missing files with `try-except`.
- Store parsed file data in dictionaries for easy access.

## File Modes

| Mode | Purpose |
|------|---------|
| `r` | Read a text file |
| `rb` | Read a binary file |
| `r+` | Read and write a file |

## Reading a File

```python
with open("sample.txt", "r") as file:
    content = file.read()
```

## Reading Line by Line

```python
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## Reading All Lines

```python
with open("sample.txt", "r") as file:
    lines = file.readlines()
```

## Handling Errors

```python
try:
    with open("sample.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")
```

## Common File Methods

| Method | Purpose |
|---------|---------|
| `read()` | Read the entire file |
| `readline()` | Read one line |
| `readlines()` | Read all lines |
| `close()` | Close the file (not needed with `with`) |

## Takeaway
File reading enables applications to load stored data. Using `with` and `try-except` ensures files are handled safely and errors are managed gracefully.
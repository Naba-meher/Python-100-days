# Day 16 Notes

## Learned
- `w` mode creates or overwrites a file.
- `a` mode adds new content without deleting existing data.
- Use `with open()` to safely work with files.
- Handle file errors using `try-except`.

## File Modes

| Mode | Purpose |
|------|---------|
| `w` | Write (overwrite) |
| `a` | Append |
| `r` | Read |
| `r+` | Read & Write |

## Writing to a File

```python
with open("journal.txt", "w") as file:
    file.write("Hello World!")
```

## Appending to a File

```python
with open("journal.txt", "a") as file:
    file.write("\nNew Entry")
```

## Handling Errors

```python
try:
    with open("journal.txt", "w") as file:
        file.write("Entry")
except PermissionError:
    print("Permission denied.")
```

## Common File Methods

| Method | Purpose |
|---------|---------|
| `write()` | Write text to a file |
| `read()` | Read entire file |
| `readlines()` | Read all lines |
| `close()` | Close the file (automatic with `with`) |

## Takeaway
Writing and appending to files allows applications to save user data permanently, making programs useful beyond a single execution.
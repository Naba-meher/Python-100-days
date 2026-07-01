# Day 10 Notes

## Learned
- File handling allows data to be stored permanently.
- Use `with open()` to safely work with files.
- Files can be opened in different modes (`r`, `w`, `a`).
- The `with` statement automatically closes the file.

## File Modes

| Mode | Purpose |
|------|---------|
| `r` | Read a file |
| `w` | Write (overwrite) a file |
| `a` | Append to a file |
| `x` | Create a new file |

## Read a File

```python
with open("notes.txt", "r") as file:
    print(file.read())
```

## Write to a File

```python
with open("notes.txt", "w") as file:
    file.write("Hello, World!")
```

## Append to a File

```python
with open("notes.txt", "a") as file:
    file.write("\nNew Note")
```

## Useful File Methods

| Method | Purpose |
|---------|---------|
| `read()` | Read the entire file |
| `readline()` | Read one line |
| `readlines()` | Read all lines as a list |
| `write()` | Write text to a file |
| `writelines()` | Write multiple lines |

## Takeaway
File handling allows programs to save, read, and update data, making applications useful even after they are closed.
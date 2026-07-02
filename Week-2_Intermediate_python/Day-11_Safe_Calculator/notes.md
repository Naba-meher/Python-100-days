# Day 11 Notes

## Learned
- Exceptions prevent programs from crashing unexpectedly.
- `try` contains code that may raise an error.
- `except` handles specific exceptions.
- `else` executes if no exception occurs.
- `finally` always executes.
- `raise` is used to create custom exceptions.

## Exception Handling

```python
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
```

## try-except-else-finally

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print(result)
finally:
    print("Program finished.")
```

## Multiple Exceptions

```python
try:
    num = int(input())
    result = 10 / num
except ValueError:
    print("Enter a valid number.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
```

## Custom Exception

```python
age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")
```

## Common Exceptions

| Exception | Cause |
|-----------|-------|
| `ValueError` | Invalid value |
| `TypeError` | Wrong data type |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | File does not exist |
| `IndexError` | Invalid list index |
| `KeyError` | Dictionary key not found |

## Takeaway
Exception handling makes programs robust by preventing crashes and allowing errors to be handled gracefully.
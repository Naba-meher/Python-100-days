# Day 12 Notes

## Learned
- Functions can return values using `return`.
- Return values can be stored, printed, or reused.
- Breaking a program into small functions improves readability.
- A function should perform one specific task.

## Function with Return

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
```

## Returning Multiple Values

```python
def calculate(a, b):
    return a + b, a - b

sum, difference = calculate(10, 5)
```

## Function Call

```python
temperature = float(input("Enter Celsius: "))
print(celsius_to_fahrenheit(temperature))
```

## Best Practices

- Keep functions short.
- Use descriptive function names.
- Avoid repeating code.
- Return values instead of printing inside functions.

## Takeaway
Functions with return values make programs modular, reusable, and easier to maintain. They allow calculations to be performed once and used wherever needed.
# Day 4 Notes

## Learned
- `if`, `elif`, and `else` control program flow.
- Comparison operators compare values.
- Logical operators combine multiple conditions.
- Nested `if` statements check conditions inside another `if`.

## Comparison Operators

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

## Logical Operators

| Operator | Meaning |
|----------|---------|
| `and` | Both conditions must be True |
| `or` | At least one condition must be True |
| `not` | Reverses the condition |

## Key Syntax

```python
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

## Takeaway
Use `if-elif-else` to make decisions based on conditions. Combine conditions using logical operators when needed.
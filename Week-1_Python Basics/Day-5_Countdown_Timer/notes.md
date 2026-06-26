# Day 5 Notes

## Learned
- `for` loops iterate over a sequence or range.
- `while` loops run until a condition becomes False.
- `range()` generates a sequence of numbers.
- `time.sleep()` pauses program execution.

## Loop Syntax

### For Loop

```python
for i in range(5):
    print(i)
```

### While Loop

```python
count = 5
while count > 0:
    print(count)
    count -= 1
```

### Delay

```python
import time

time.sleep(1)
```

## Takeaway
Use `for` and `while` loops to repeat tasks. `time.sleep()` is useful for creating delays, such as in a countdown timer.
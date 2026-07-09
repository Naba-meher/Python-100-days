# Day 20 Notes

## Learned
- The `datetime` module is used to work with dates and times.
- `datetime.now()` returns the current date and time.
- `strftime()` formats dates into readable strings.
- `strptime()` converts a string into a `datetime` object.
- Date subtraction returns a `timedelta` object.

## Current Date & Time

```python
from datetime import datetime

current = datetime.now()
print(current)
```

## Formatting Date & Time

```python
formatted = current.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)
```

## Convert String to Date

```python
date = datetime.strptime(
    "2026-12-31 23:59:59",
    "%Y-%m-%d %H:%M:%S"
)
```

## Calculate Time Difference

```python
time_left = event_date - datetime.now()

print(time_left.days)
```

## Common Format Codes

| Code | Meaning |
|------|---------|
| `%Y` | Year |
| `%m` | Month |
| `%d` | Day |
| `%H` | Hour (24-hour) |
| `%M` | Minute |
| `%S` | Second |

## Takeaway
The `datetime` module makes it easy to work with dates, format time, and calculate time differences for applications like countdown timers and schedulers.
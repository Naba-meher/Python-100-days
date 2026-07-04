# Day 13 Notes

## Learned
- List comprehensions create lists in a single line.
- Conditional expressions can be used inside list comprehensions.
- Filters help select items based on a condition.
- `enumerate()` provides both index and value.
- `zip()` combines multiple iterables.

## Basic List Comprehension

```python
numbers = [1, 2, 3, 4]

squares = [num ** 2 for num in numbers]
```

## Filtering

```python
even_numbers = [num for num in numbers if num % 2 == 0]
```

## Conditional Expression

```python
grades = [
    "Pass" if score >= 60 else "Fail"
    for score in scores
]
```

## enumerate()

```python
for index, score in enumerate(scores, start=1):
    print(index, score)
```

## zip()

```python
for score, grade in zip(scores, grades):
    print(score, grade)
```

## Takeaway
List comprehensions make code shorter and more readable. Combining them with conditions, `enumerate()`, and `zip()` simplifies data processing.
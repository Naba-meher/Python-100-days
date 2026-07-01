# Day 9 Notes

## Learned
- Tuples are ordered and immutable collections.
- Tuple unpacking assigns values to multiple variables.
- Sets store unique values.
- Set operations help compare collections efficiently.

## Tuple Example

```python
coordinates = (10, 20, 30)
x, y, z = coordinates
```

## Set Example

```python
fruits = {"apple", "banana", "mango"}

fruits.add("orange")
fruits.remove("banana")
```

## Set Operations

| Operator | Purpose |
|----------|---------|
| `|` | Union |
| `&` | Intersection |
| `-` | Difference |

## Example

```python
set_a = {"flour", "sugar", "butter"}
set_b = {"sugar", "eggs"}

print(set_a | set_b)
print(set_a & set_b)
print(set_a - set_b)
```

## Common Set Methods

| Method | Purpose |
|---------|---------|
| `add()` | Add an item |
| `remove()` | Remove an item |
| `discard()` | Remove safely |
| `clear()` | Remove all items |
| `union()` | Combine sets |
| `intersection()` | Common items |
| `difference()` | Unique items |

## Takeaway
Sets are useful for comparing collections, removing duplicates, and finding missing or common elements.
# Day 7 Notes

## Learned
- Lists store multiple values in a single variable.
- Items are accessed using indexes (starting from 0).
- List methods help modify lists.
- Loops can iterate through list items.
- `enumerate()` provides both index and value while looping.

## Common List Operations

```python
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")
fruits.remove("Banana")
print(fruits[0])
```

## Loop Through a List

```python
for item in fruits:
    print(item)
```

## Using `enumerate()`

```python
for index, item in enumerate(fruits):
    print(index, item)
```

Output:

```
0 Apple
1 Banana
2 Mango
```

## Common List Methods

| Method | Purpose |
|---------|---------|
| `append()` | Add an item |
| `insert()` | Insert at a position |
| `remove()` | Remove an item |
| `pop()` | Remove by index |
| `sort()` | Sort the list |
| `reverse()` | Reverse the list |
| `clear()` | Remove all items |
| `len()` | Get the number of items |
| `enumerate()` | Get index and value while looping |

## Takeaway
Lists make it easy to store and manage collections of data. Use `enumerate()` when you need both the index and the item, and `clear()` to remove all elements from a list.
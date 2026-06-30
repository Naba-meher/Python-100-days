# Day 8 Notes

## Learned
- Dictionaries store data as **key-value pairs**.
- JSON files allow data to persist after the program closes.
- Functions make code modular and reusable.
- CRUD operations help manage data efficiently.
- Input validation improves program reliability.

## Dictionary Example

```python
contacts = {
    "Naba": {
        "phone": "9876543210",
        "email": "naba@example.com"
    }
}
```

## JSON File Handling

```python
import json

# Read
with open("contacts.json", "r") as file:
    contacts = json.load(file)

# Write
with open("contacts.json", "w") as file:
    json.dump(contacts, file, indent=4)
```

## Dictionary Methods

| Method | Purpose |
|---------|---------|
| `get()` | Get a value safely |
| `keys()` | Return all keys |
| `values()` | Return all values |
| `items()` | Return key-value pairs |
| `pop()` | Remove a key |
| `update()` | Update a dictionary |
| `clear()` | Remove all entries |

## File Handling

| Function | Purpose |
|----------|---------|
| `open()` | Open a file |
| `json.load()` | Read JSON data |
| `json.dump()` | Write JSON data |

## Concepts Used
- Dictionaries
- Functions
- JSON File Handling
- CRUD Operations
- Input Validation
- Loops & Conditionals

## Takeaway
Using dictionaries with JSON file handling makes it easy to build applications that can save, retrieve, update, and manage data permanently.
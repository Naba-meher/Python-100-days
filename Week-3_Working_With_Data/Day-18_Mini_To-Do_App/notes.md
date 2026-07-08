# Day 18 Notes

## Learned
- JSON stores structured data using key-value pairs.
- `json.load()` reads JSON data into Python objects.
- `json.dump()` writes Python objects to JSON files.
- JSON is commonly used for configuration files and data storage.
- Dictionaries and lists can be easily converted to JSON.

## JSON Example

```python
tasks = [
    {
        "task": "Learn Python",
        "status": "Incomplete"
    }
]
```

## Reading JSON

```python
import json

with open("tasks.json", "r") as file:
    tasks = json.load(file)
```

## Writing JSON

```python
with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=2)
```

## Common JSON Functions

| Function | Purpose |
|----------|---------|
| `json.load()` | Read JSON from a file |
| `json.dump()` | Write JSON to a file |
| `json.loads()` | Convert JSON string to Python object |
| `json.dumps()` | Convert Python object to JSON string |

## Takeaway
JSON provides a simple and readable way to store structured data, making it ideal for applications such as to-do lists, configuration files, and APIs.
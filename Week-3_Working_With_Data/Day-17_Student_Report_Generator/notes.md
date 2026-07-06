# Day 17 Notes

## Learned
- CSV (Comma-Separated Values) files store tabular data.
- The `csv` module makes reading and writing CSV files easy.
- `DictReader()` reads rows as dictionaries.
- `DictWriter()` writes dictionaries to CSV files.
- Exception handling prevents file-related errors.

## Reading a CSV

```python
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
```

## Writing a CSV

```python
import csv

with open("report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Average"])
```

## Using DictWriter

```python
writer = csv.DictWriter(file, fieldnames=["Name", "Average"])
writer.writeheader()
writer.writerow({"Name": "John", "Average": 85})
```

## Common CSV Classes

| Class | Purpose |
|--------|---------|
| `csv.reader()` | Read rows as lists |
| `csv.DictReader()` | Read rows as dictionaries |
| `csv.writer()` | Write rows as lists |
| `csv.DictWriter()` | Write rows as dictionaries |

## Takeaway
The `csv` module makes it easy to read, process, and generate reports from structured data files.
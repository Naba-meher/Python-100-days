# Day 14 Notes

## Learned
- Modules help organize reusable code.
- Libraries provide additional functionality.
- Use `import` to access modules.
- Python includes many built-in modules.
- Custom modules can be imported like built-in modules.

## Import Syntax

```python
import random
import string

from random import randint
import random as r
```

## Common Built-in Modules

| Module | Purpose |
|---------|---------|
| `random` | Random numbers and selections |
| `string` | Character constants |
| `math` | Mathematical functions |
| `datetime` | Date & time |
| `os` | Operating system utilities |

## Useful Functions

```python
random.randint(1, 10)
random.choice(items)
random.choices(items, k=5)
random.shuffle(list)

string.ascii_uppercase
string.ascii_lowercase
string.digits
```

## Custom Module

```python
import greetings

print(greetings.say_hello("John"))
```

## Takeaway
Modules and libraries make development faster by providing reusable code. The `random` and `string` modules are especially useful for generating secure passwords.
# Day 21 Notes

## Learned
- Web scraping extracts data from websites.
- `requests` fetches HTML pages.
- BeautifulSoup parses HTML content.
- HTML elements can be searched using tags.
- Extracted data can be cleaned and displayed.

## Basic HTML

```html
<h1>Title</h1>
<p>Paragraph</p>
<a href="https://example.com">Link</a>
```

## Fetch a Web Page

```python
import requests

response = requests.get(url)

if response.status_code == 200:
    print(response.text)
```

## Parse HTML

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
```

## Find Elements

```python
title = soup.find("h1").text

paragraphs = soup.find_all("p")
```

## Extract Links

```python
for link in soup.find_all("a", href=True):
    print(link["href"])
```

## Common BeautifulSoup Methods

| Method | Purpose |
|---------|---------|
| `find()` | Find the first matching element |
| `find_all()` | Find all matching elements |
| `.text` | Get element text |
| `.get()` | Get an attribute |
| `.strip()` | Remove extra spaces |

## Takeaway
Web scraping allows Python programs to collect information from websites. Combining `requests` and BeautifulSoup makes it easy to fetch, parse, and extract useful data from HTML pages.
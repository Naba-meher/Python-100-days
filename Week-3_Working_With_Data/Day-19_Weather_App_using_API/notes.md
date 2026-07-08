# Day 19 Notes

## Learned
- APIs allow applications to communicate and exchange data.
- `requests` is used to send HTTP requests.
- API keys authenticate requests.
- JSON is the standard format for API responses.
- API responses can be converted into Python dictionaries.

## What is an API?

An **API (Application Programming Interface)** allows one application to request data or services from another.

Example:

```
Python Program
      │
      ▼
OpenWeather API
      │
      ▼
JSON Response
      │
      ▼
Display Weather
```

## Sending a GET Request

```python
import requests

response = requests.get(url)
```

## Check Response Status

```python
if response.status_code == 200:
    data = response.json()
```

## Reading JSON Response

```python
city = data["name"]
temperature = data["main"]["temp"]
weather = data["weather"][0]["description"]
```

## Common HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | Success |
| 400 | Bad Request |
| 401 | Unauthorized (Invalid API Key) |
| 404 | Resource Not Found |
| 500 | Server Error |

## Takeaway
APIs allow Python programs to fetch live data from external services. The `requests` library simplifies sending HTTP requests and processing JSON responses.
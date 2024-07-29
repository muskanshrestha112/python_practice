import requests
import json


url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"
response = requests.get(url)
data = response.json()
print(data)
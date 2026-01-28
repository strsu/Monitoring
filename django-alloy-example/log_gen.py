import requests
import time

MEMO_BASE_URL = "http://192.168.71.74:8000"
BOOK_BASE_URL = "http://192.168.71.74:8001"

for i in range(10):
    requests.post(f"{MEMO_BASE_URL}/api/memo/", json={"title": f"test {i}", "content": f"test {i}"})
    requests.post(f"{BOOK_BASE_URL}/api/book/", json={"name": f"test {i}", "author": f"test {i}", "published_date": f"2026-01-01"})
    time.sleep(1)

count = 0
while True:
    requests.get("http://localhost:8000/api/memo/")
    time.sleep(0.3)
    requests.get("http://localhost:8001/api/book/")
    time.sleep(0.3)
    count += 1
    if count % 10 == 0:
        print(f"count: {count}")
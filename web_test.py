import requests
import concurrent.futures
import socket

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 80))

    for i in range(0, 2):
        futures.append(executor.submit(lambda: requests.get('http://localhost')))

    for completed in concurrent.futures.as_completed(futures):
        print(completed.result())

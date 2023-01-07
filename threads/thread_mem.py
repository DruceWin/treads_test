import time

import requests
import threading
import json

count_data = 1
array_url = [f"https://jsonplaceholder.typicode.com/posts/{count_data}",
             f"https://jsonplaceholder.typicode.com/comments/{count_data}",
             f"https://jsonplaceholder.typicode.com/albums/{count_data}",
             f"https://jsonplaceholder.typicode.com/photos/{count_data}",
             f"https://jsonplaceholder.typicode.com/todos/{count_data}",
             f"https://jsonplaceholder.typicode.com/users/{count_data}",
             ]


def time_decorator(func):
    start = time.time()

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print(time.time()-start)
    return wrapper


@time_decorator
def sunc_requests_to_json_placeholder(urls):
    """Синхронные запросы на ресурс"""
    with open("result_data_json.json", "w") as file:
        data_json = []
        for url in urls:
            data_json.append(requests.get(url).json())
        json.dump(data_json, file)


@time_decorator
def request_to_json_placeholder_from_threading(urls):
    data_json = []

    def request_to_json_pl(url):
        data_json.append(requests.get(url).json())

    for i in urls:
        thred = threading.Thread(target=request_to_json_pl, args=(i, ))
        thred.start()
        thred.join()

    with open("result_data_json.json", "w") as file:
        json.dump(data_json, file)


sunc_requests_to_json_placeholder(array_url)
request_to_json_placeholder_from_threading(array_url)

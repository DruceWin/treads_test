import random
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
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time()
        print(finish-start)
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
        sleep_time = random.randrange(1, 4)
        # time.sleep(sleep_time)
        # print(sleep_time)
        data_json.append(requests.get(url).json())

    # for i in urls:
    #     thred = threading.Thread(target=request_to_json_pl, args=(i, ))
    #     thred.start()
    #     thred.join()

    # for i, j in enumerate(urls):
    #     print(i, j)

    threds = [threading.Thread(target=request_to_json_pl, args=(i, )) for i in urls]
    [i.start() for i in threds]
    [i.join() for i in threds]

    # thred1 = threading.Thread(target=request_to_json_pl, args=(urls[0], ))
    # thred1.start()
    # thred2 = threading.Thread(target=request_to_json_pl, args=(urls[1], ))
    # thred2.start()
    # thred3 = threading.Thread(target=request_to_json_pl, args=(urls[2], ))
    # thred3.start()
    # thred4 = threading.Thread(target=request_to_json_pl, args=(urls[3], ))
    # thred4.start()
    # thred5 = threading.Thread(target=request_to_json_pl, args=(urls[4], ))
    # thred5.start()
    # thred6 = threading.Thread(target=request_to_json_pl, args=(urls[5], ))
    # thred6.start()
    # thred1.join()
    # thred2.join()
    # thred3.join()
    # thred4.join()
    # thred5.join()
    # thred6.join()

    with open("result_data_json.json", "w") as file:
        json.dump(data_json, file)


sunc_requests_to_json_placeholder(array_url)
request_to_json_placeholder_from_threading(array_url)

import asyncio
import multiprocessing
import threading
import time

import requests


url = 'https://jsonplaceholder.typicode.com/posts/1'


def django_request():
    response = requests.get(url).json()
    print(response)


async def get_one():
    t1 = threading.Thread(target=django_request)
    t2 = threading.Thread(target=django_request)
    t3 = threading.Thread(target=django_request)
    t1.start()
    t2.start()
    t3.start()
    # t1.join()
    # t2.join()
    # t3.join()


async def get_two():
    t1 = threading.Thread(target=django_request)
    t2 = threading.Thread(target=django_request)
    t3 = threading.Thread(target=django_request)
    t1.start()
    t2.start()
    t3.start()
    # t1.join()
    # t2.join()
    # t3.join()


def hello_from_proccess(n):
    print(t := time.time())
    res = []
    for i in range(n):
        res.append(i**2)
    print(res)
    with open('new_txt.txt', 'w') as file:
        for i in res:
            file.writelines(f"{str(i)}\n")
    print(time.time() - t)


async def heavy():
    proc1 = multiprocessing.Process(target=hello_from_proccess, args=(1000, ))
    proc1.start()
    # proc1.join()


async def main():
    # task1 = asyncio.create_task(get_one())
    # task2 = asyncio.create_task(get_two())
    task3 = asyncio.create_task(heavy())
    # await task1
    # await task2
    await task3

print(t := time.time(), 'main')
asyncio.run(main())
print(time.time()-t, 'main')

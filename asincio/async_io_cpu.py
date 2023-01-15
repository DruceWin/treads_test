""" Синхронный код с IO-bound и CPU-bound"""

# import requests
#
#
#
# '''Веб-запрос ограничен производительностью ввода-вывода'''
# response = requests.get('https://www.itec.by')
#
# '''Обработка ответа связанная с быстродействием процессора'''
# items = response.headers.items()
# headers = [f'{key}: {header}' for key, header in items]
# formatted_headers = '\n'.join(headers)#конкатенация строк
#
# '''Запись на жесткий диск  в файл ограничена производительностью ввода-вывода'''
# with open('headers.txt', 'w') as file:
#     file.write(formatted_headers)
import time

"""==========Процессы Потоки========="""

# import os
# import threading
# print(f'Исполняется Python-процесс с идентификатором: {os.getpid()}')
# total_threads = threading.active_count()
# thread_name = threading.current_thread().name
# print(f'В данный момент Python исполняет {total_threads} поток(ов)')
# print(f'Имя текущего потока {thread_name}')
#

'''
Процессы могут порождать дополнительные потоки, разделяющие
память со своим процессом-родителем. Они могут конкурентно вы-
полнять другую работу, это называется многопоточностью.
'''

# import threading
# import requests
# import time
# url_django ='http://127.0.0.1:8080'
# url_fastapi ='http://127.0.0.1:8000'
#
# def hello_from_thread(url):
#     start = time.time()
#     resp = requests.get(url)
#     print(resp.json())
#     print(f'Привет от потока {threading.current_thread()}!')
#     print(f"Время запроса {threading.current_thread()}==={time.time()-start}")
# def fn(delay):
#
#     for i in range(1000):
#          # time.sleep(delay)
#          if i%2 ==0:
#              print(str(i),"fn")
#     print(f"fn {delay}")
#
#
# def fn1(delay):
#     for i in range(1000):
#         # time.sleep(delay)
#         if i % 2 != 0:
#             print(str(i),"fn1")
#     print(f"fn {delay}")
#
#
# django_thread = threading.Thread(target=hello_from_thread,args=(url_django,),name="query_to_django")
# fastapi_thread = threading.Thread(target=hello_from_thread,args=(url_fastapi,), name="query_to_fastapi")
# fn_thread = threading.Thread(target=fn,args=(1,), name="query_to_fastapi")
# fn1_thread = threading.Thread(target=fn1,args=(1,), name="query_to_fastapi")
# # fn_thread.start()
# # fn1_thread.start()
# django_thread.start()
# fastapi_thread.start()
#
# fastapi_thread.join()
# django_thread.join()
# # fn_thread.join()
# total_threads = threading.active_count()
# thread_name = threading.current_thread().name
# print(f'В данный момент Python выполняет {total_threads} поток(ов)')
# print(f'Имя текущего потока {thread_name}')


'''==================Многопроцессность================'''

# import multiprocessing
# import os
#
# a = 100
# def hello_from_process():
#     global a
#     a=a+1
#     print(f'Привет от дочернего процесса {os.getpid()}!,{a}')
#
#
#
# if __name__ == '__main__':
#     hello_process = multiprocessing.Process(target=hello_from_process)
#     hello_process.start()
#     # hello_from_process()
#     print(f'Привет от родительского процесса {os.getpid()}')
#     hello_process.join()
#     print(a)

"""=============ASINCIO=============="""


'''
Сопрограмму можно рассматривать как обычную функцию Python,
наделенную сверхспособностью: приостанавливаться, встретив опе-
рацию, для выполнения которой нужно заметное время. По заверше-
нии такой длительной операции сопрограмму можно «пробудить»,
после чего она продолжит выполнение. Пока приостановленная со-
программа ждет завершения операции, мы можем выполнять другой
код. Такое выполнение другого кода во время ожидания и обеспечи-
вает конкурентность внутри приложения. Можно также одновремен-
но выполнять несколько длительных операций, что еще больше по-
вышает производительность приложения.
Для создания и приостановки сопрограммы нам придется исполь-
зовать ключевые слова Python async и await. Слово async определяет
сопрограмму, а слово await приостанавливает ее на время выполне-
ния длительной операции.


сопрограммы не выполняются, если их вы-
звать напрямую. Вместо этого возвращается объект сопрограммы,
который будет выполнен позже. Чтобы выполнить сопрограмму, мы
должны явно передать ее циклу событий. И как же создать цикл со-
бытий и выполнить в нем нашу сопрограмму?
В версиях Python, предшествующих 3.7, цикл событий нужно было
создавать вручную, если его еще не было. Но затем в asyncio было до-
бавлено несколько функций, абстрагирующих управление циклом со-
бытий. Одна из них – вспомогательная функция asyncio.run, которую
можно использовать для запуска нашей сопрограммы.
'''

# import asyncio
#
# '''Слова async/await?'''
#
#
# async def async_fn(number: int) -> int:
#     await asyncio.sleep(number)
#     return number
#
#
# print(async_fn)
# res = async_fn(2)
# print(res)
#
#
# async def main() -> None:
#     c = await async_fn(2)
#     print(c)
#
#
# asyncio.run(main())
'''asyncio.run делает несколько важных вещей. Во-
первых, она создает новое событие. Потом она выполняет код пере-
данной нами сопрограммы до конца и возвращает результат. Эта
функция также подчищает все то, что могло остаться после заверше-
ния сопрограммы. И в конце она останавливает и закрывает цикл со-
бытий.

!!!!самое главное в asyncio.run – то, что она задумана
как главная точка входа в созданное нами приложение asyncio. Она
выполняет только одну сопрограмму, и эта сопрограмма должна по-
заботиться обо всех остальных аспектах приложения. Сопро-
грамма, которую выполняет asyncio.run, должна создать и запустить
все прочие сопрограммы, это позволит нам обратить себе на пользу
конкурентную природу asyncio!!!.
'''

# import asyncio
#
# #Создаем три сопрограммы
#
# async def func_0() -> int:
#     print("start func_0")
#     await asyncio.sleep(0)
#     print("stop func_0")
#     return 0
#
# async def func_1() -> int:
#     print("start func_1")
#     await asyncio.sleep(1)
#     print("stop func_1")
#     return 1
#
# async def func_2() -> int:
#     print("start func_2")
#     await asyncio.sleep(2)
#     print("stop func_2")
#     return 2
# async def main():
#     start= time.time()
#     f0 = await func_0()
#     f1 = await func_1()
#     f2 = await func_2()
#
#     print(f0)
#     print(f1)
#     print(f2)
#     print(f"время работы {time.time()-start}")
# asyncio.run(main())
'''
Асинхронный ввод-вывод позволяет приостановить выполнение
метода, встретив операцию ввода-вывода; ожидая завершения этой
операции, работающей в фоновом режиме, мы можем выполнять ка-
кой-нибудь другой код. Это позволяет выполнять одновременно мно-
го операций ввода-вывода и тем самым ускорить работу приложения.
'''

''' Конкурентное выполнение с помощью задач

Цикл событий – сердце любого приложения asyncio. Этот паттерн про-
ектирования встречается во многих системах и был придуман уже
довольно давно. Используя в браузере JavaScript для отправки асин-
хронного запроса, вы создаете задачу, управляемую циклом событий.
В GUI-приложениях Windows за кулисами используются так называе-
мые циклы обработки сообщений; это основной механизм обработки
таких событий, как нажатие клавиш, он позволяет одновременно от-
рисовывать интерфейс и реагировать на действия пользователя.
По сути своей цикл событий очень прост. Мы создаем очередь, в ко-
торой хранится список событий или сообщений, а затем входим в бес-
конечный цикл, где обрабатываем сообщения по мере их поступле-
ния

В asyncio цикл событий управляет очередью задач, а не сообщений.
Задача – это обертка вокруг сопрограммы. Сопрограмма может при-
остановить выполнение, встретив операцию ввода-вывода, и дать ци-
клу событий возможность выполнить другие задачи, которые не ждут
завершения ввода-вывода.
Создавая цикл событий, мы создаем пустую очередь задач. Затем
добавляем в эту очередь задачи для выполнения. На каждой ите-
рации цикла проверяется, есть ли в очереди готовая задача, и если
да, то она выполняется, пока не встретит операцию ввода-вывода.
В этот момент задача приостанавливается, и мы просим операцион-
ную систему наблюдать за ее сокетами. А сами тем временем пере-
ходим к следующей готовой задаче. На каждой итерации проверяет-
ся, завершилась ли какая-нибудь операция ввода-вывода; если да, то
ожидавшие ее завершения задачи пробуждаются и им предоставля-
ется возможность продолжить работу.
'''

# import asyncio
#
# #Создаем три сопрограммы
#
# async def func_0() -> int:
#     print("start func_0")
#     await asyncio.sleep(0)
#     print("stop func_0")
#     return 0
#
# async def func_1() -> int:
#     print("start func_1")
#     await asyncio.sleep(1)
#     print("stop func_1")
#     return 1
#
# async def func_2() -> int:
#     print("start func_2")
#     await asyncio.sleep(2)
#     print("stop func_2")
#     return 2
# async def main():
#     start = time.time()
#     print(f"Начало {start}")
#     f0 = asyncio.create_task(func_0())
#     f1 = asyncio.create_task(func_1())
#     f2 = asyncio.create_task(func_2())
#     await f0
#     await f1
#     await f2
#     print(f0)
#     print(f1)
#     print(f2)
#     print(f"Конец {time.time()}",f"время работы {time.time()-start}")
#
# asyncio.run(main())


'''=========FUTURE and AWAITABLE========='''

'''
Объект future в Python содержит одно значение, которое мы ожидаем
получить в будущем, но пока еще, возможно, не получили. Обычно
в момент создания future не обертывает никакого значения, потому
что его еще не существует. Объект в таком состоянии называется не-
полным, неразрешенным или просто неготовым. И только получив
результат, мы можем установить значение объекта future, в резуль-
тате чего он становится полным и из него можно извлечь результат.

'''
'''-----FUTURE----exemple'''
# from asyncio import Future
# future = Future()
# print(future)
# print(dir(future))
# print(f'my_future разрешен? {future.done()}')
# future.set_result(42)
# print(future)
# print(f'my_future разрешен(получил значение)? {future.done()}')
# print(future)
# print(f'Какой результат обернут футурой my_future? {future.result()}')


'''future query to fastapi'''


# import asyncio
# import aiohttp
# from aiohttp import ClientSession
# from asyncio import Future
#
# def create_future() -> Future:
#     future = Future()
#     asyncio.create_task(fetch_typa_js(future))
#     return future
#
#
# async def fetch_typa_js(any_future):
#     async with aiohttp.ClientSession() as session:
#         url = 'http://127.0.0.1:8000/'
#         print(f'Запрос по адресу {url}')
#         async with session.get(url) as result:
#             any_future.set_result(await result.text())
#             print(f'Статус ответа по запросу {url} === {result.status}')
#             print(f"Тело ответа {dir(result)}====\n{await result.text()}")
#             return result.status
#
#
# async def main():
#     future = create_future()
#     await future
#     print(future.result())
#
# asyncio.run(main())


'''========================================================='''
import asyncio
import aiohttp
from aiohttp import ClientSession

async def fetch_status(session: ClientSession, url: str) -> int:
     async with session.get(url) as result:
         return result.status


async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        urls = ['http://127.0.0.1:8000/' for _ in range(1000)]
        requests = [fetch_status(session, url) for url in urls]
        status_codes = await asyncio.gather(*requests)
        print(status_codes)
    print(time.time()-start,"Время работы 1000 запросов")
asyncio.run(main())
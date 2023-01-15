import asyncio
import time


async def one():
    print('one')


async def two():
    print('two')


async def three():
    await asyncio.sleep(1)
    with open('new_test_txt.txt', 'w') as file:
        file.writelines('zapisal')
    print('three')


async def main():
    task1 = asyncio.create_task(one())
    task2 = asyncio.create_task(two())
    task3 = asyncio.create_task(three())
    await task1
    await task2
    await task3


print(t := time.time(), 'main')
asyncio.run(main())
print(time.time()-t, 'main')

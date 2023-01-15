def fn():
    print('start')
    n = yield 1
    print(n, 'yield 1')
    n = yield 2
    print(n, 'yield 2')
    n = yield 3
    print(n, 'yield 3')


fng = fn()
x, y = 333, 555
print('next1', next(fng))
print('next2', fng.send(x))

x = 777
fng_2 = fn()
print(fng)
print(fng_2)
print('next1', next(fng_2))
print('next2', fng_2.send(x))


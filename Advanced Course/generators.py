import time

def fibo_gen(max: int) -> int:
    a, b, c, aux = 0, 1, 0, 0
    while aux <= max:
        if c == 0:
            c += 1
            yield a
        elif c == 1:
            c += 1
            yield b
        else:
            aux = a + b
            a, b = b, aux
            c += 1
            yield aux

if __name__ == '__main__':
    fibo = fibo_gen(1000)
    for element in fibo:
        print(element)
        time.sleep(0.5)
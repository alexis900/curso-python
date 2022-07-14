def continuar():
    for contador in range(1000):
        if contador % 2 != 0:
            continue
        print(contador)


def parar():
    for i in range(10000):
        print(i)
        if i == 4678:
            break

def run():
    #continuar()
    parar()

if __name__ == '__main__':
    run()
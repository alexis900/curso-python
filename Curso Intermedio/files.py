def read():
    numbers = []
    with open('./files/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
        print(numbers)
    f.close()

def write():
    names = ["Facundo", "Miguel", "Alejandro", "Alex"]
    with open('./files/names.txt', 'w', encoding='utf-8') as f:
        for name in names:
            f.write(f'{name}\n')
    f.close()


def run():
    write()


if __name__ == '__main__':
    run()
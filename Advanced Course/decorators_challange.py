def with_ceasar(num):
    def ceasar(func):
        def wrapper(msg):
            func(msg)
            rotated = ''
            for letter in msg:
                l = ord(letter)
                rotated += ''.join(chr(l + num))
            print(f'{msg} coded is {rotated}')
        return wrapper
    return ceasar

@with_ceasar(8)
def imprime(msg):
    return msg
    

def run():
    print(imprime('Hola'))

if __name__ == '__main__':
    run()
def while_bucle():
    LIMITE = 1000000
    contador = 0
    potencia = 2**contador
    while potencia <= LIMITE:
        print(f'2^{contador}={potencia}')
        contador = contador+1
        potencia = 2**contador

def run():
    while_bucle()
    

if __name__ == '__main__':
    run()
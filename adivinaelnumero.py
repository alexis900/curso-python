import random

def run():
    randomNum = random.randint(1, 100)
    numero = False
    while numero != randomNum:
        numero = int(input('¿Sabes cual es el número aleatorio? '))
        if numero > randomNum:
            print(f'El número es más pequeño que {numero}')
        elif numero < randomNum:
            print(f'El número es más grande que {numero}')
        elif numero == randomNum:
            print(f'El número aleatorio es {numero}')
            

if __name__ == '__main__':
    run()
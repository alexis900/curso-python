# def is_prime(number):
#     counter = 0
#     for i in range(1, number + 1):
#         if i == 1 or i == number:
#             continue
#         if number % i == 0:
#             counter += 1
#             break
#     if counter == 0 and number != 1:
#         return True

from itertools import count


def is_primeGood(number):
    cont = 1
    for i in range(2, number+1):
        if number % i == 0:
            cont += 1
        
    if cont >= 3 or number == 1:
        return False
    else:
        return True

def run():
    list = [1, 2, 3, 4, 5, 6, 17, 18, 55]
    for i in list:
        if is_primeGood(i):
            print(f'{i} is prime')
        else:
            print(f'{i} is not prime')

if __name__ == '__main__':
    run()
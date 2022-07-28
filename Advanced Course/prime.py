def is_prime(number: int) -> bool:
    result = [i for i in range(1, number+1) if number%i==0]
    return len(result)==2
            

def run():
    print(is_prime(1))


if __name__ == '__main__':
    run()
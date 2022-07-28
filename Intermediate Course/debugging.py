def divisors(num):
    return [i for i in range(1, num+1) if num % i == 0]
    

def run():
    while True:
        num = input("Enter the number: ")
        try:
            if len(num) == 0:
                raise ValueError('The input cannot be empty')
        except ValueError as checkLenght:
            print(checkLenght)
        try:
            num = int(num)
        except ValueError:
            print('The input must be a number')
        else:
            try:
                if num <= 0:
                    raise ValueError("You must enter a positive number")
            except ValueError as positiveCheck:
                print(positiveCheck)
            else:
                print(divisors(num))
                print("Program ended")
                break
            


if __name__ == '__main__':
    run()
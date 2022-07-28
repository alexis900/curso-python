def divisors(num):
    return [i for i in range(1, num+1) if num % i == 0]
    

def run():
    num = input("Enter the number: ")
    assert num.isnumeric(), "Debes ingresar un número"
    assert int(num) < 0, "You must enter a positive number"
    print(divisors(int(num)))
    print("Program ended")



if __name__ == '__main__':
    run()
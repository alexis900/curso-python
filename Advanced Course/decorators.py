def uppercase(func):
    def wrapping(text: str) -> str:
        return func(text).upper()
    return wrapping

@uppercase
def message(name: str) -> str:
    return f'{name}, are you revided a message'



def run():
    print(message('Alejandro'))

if __name__ == '__main__':
    run()
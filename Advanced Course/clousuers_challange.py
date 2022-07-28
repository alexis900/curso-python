from typing import Callable


def make_division_by(n: int) -> Callable[[int], float]:
    assert type(n) == int, 'Solo puedes usar números enteros'
    assert type(n) != 0, 'No puedes dividir entre 0'

    """
    This clousure returns a function that reutrns the division of an x number by n
    """
    def division(x: int) -> float:
        return x / n
    return division

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18)) # Expected output is 6
    division_by_5 = make_division_by(5)
    print(division_by_5(100)) # Expected output is 20
    division_by_18 = make_division_by(18)
    print(division_by_18(54)) # Expected output is 3

if __name__ == '__main__':
    run()
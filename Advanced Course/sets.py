SET_1 = {'🍓', '🍰', '🍭', '🧁'}
SET_2 = {'🍐', '🍋', '🍓', '🫐'}

def run() -> None:
    print(f'Union: {SET_1.union(SET_2)}') # {'🍐', '🍋', '🫐', '🧁', '🍓', '🍭', '🍰'}
    print(f'Intersection: {SET_1.intersection(SET_2)}') # {'🍓'}
    print(f'Difference SET_1 to SET_2: {SET_1.difference(SET_2)}') # {'🧁', '🍭', '🍰'}
    print(f'Difference SET_2 to SET_1: {SET_2.difference(SET_1)}') # {'🍐', '🫐', '🍋'}
    print(f'Symetric Difference: {SET_1.symmetric_difference(SET_2)}') # {'🍐', '🧁', '🍰', '🍋', '🍭', '🫐'}


if __name__ == '__main__':
    run()
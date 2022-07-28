def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {"firstname": "Alejandro", "lastname": "Martin"}

    super_list = [
        {"firstname": "Alejandro", "lastname": "Martin"},
        {"firstname": "Alex", "lastname": "Rodriguez"},
        {"firstname": "Billy", "lastname": "García"},
        {"firstname": "Sussana", "lastname": "Rodelo"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.4, 4.6, 2.6, 7.2, 5.3]
    }

    for key, value in super_dict.items():
        print(f'{key} - {value}')

    for key in super_list:
        print(key['firstname'], key['lastname'])

    

if __name__ == '__main__':
    run()
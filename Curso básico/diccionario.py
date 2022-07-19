def run():
    diccionario = {
        # Estructura de datos de llaves y valores
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }

    poblacion_paises = {
        'España': 46500984,
        'Blasil': 210147125,
        'Colombia': 50372424
    }

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #      print(pais)
    
    for pais, poblacion in poblacion_paises.items():
         print(f'{pais} tiene {poblacion} habitantes')

    # print(poblacion_paises['España'])

    # print(diccionario['llave1'])
    # print(diccionario['llave2'])
    # print(diccionario['llave3'])


if __name__ == '__main__':
    run()
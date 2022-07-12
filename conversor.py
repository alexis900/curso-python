val_dolar = 137.21
val_yen = 0.00731


def Menu():
    print("""
    1. Dolar a yen
    2. Yen a dolar
    3. Salir
    """)

    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        dolar = float(input("Introduce los dolares que tienes: "))
        yen = str(round(dolar * val_dolar, 2))
        print("Tienes " + yen + " yens")
        Menu()
    elif opcion == 2:
        yen = float(input("Introduce los yens que tienes: "))
        dolar = str(round(yen / val_dolar, 2))
        print("Tienes " + dolar + " dolares")
        Menu()
    elif opcion == 3:
        print("Hasta luego")
    else:
        print("Opcion no valida")
        Menu()


Menu()
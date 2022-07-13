from xmlrpc.client import boolean


val_dolar = 137.21
tipo_moneda = "Yen"
def conversor(tipo_moneda, valor_dolar, to_moneda=False):
    if (to_moneda == True):
        moneda = float(input("¿Cuántos dólares tienes? "))
        dolares = str(round(moneda * valor_dolar))
        print("Tienes " + dolares + " " + tipo_moneda)
    else:
        moneda = float(input("¿Cuántos " + tipo_moneda + " tienes? "))
        dolares = str(round(moneda / valor_dolar))
        print("Tienes $ " + dolares + " dólares")
    

def Menu(tipo_moneda):
    print("1. Dolar a " + tipo_moneda + "\n2. " + tipo_moneda + " a dolar\n3. Salir")

    opcion = int(input("Introduce una opcion: "))
    if opcion == 1:
        conversor(tipo_moneda, val_dolar, True)
        Menu(tipo_moneda)
    elif opcion == 2:
        conversor(tipo_moneda, val_dolar)
        Menu(tipo_moneda)
    elif opcion == 3:
        print("Hasta luego")
    else:
        print("Opcion no valida")
        Menu(tipo_moneda)


Menu(tipo_moneda)
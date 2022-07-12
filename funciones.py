# def imprimir_msg():
#     print("Mensaje especial: ")
#     print("Estoy aprendiendo a usar funciones")

# imprimir_msg()
# imprimir_msg()

def conversacion(opcion):
    print("Hola")
    print("Como estás")
    print("Elegiste la opción " + str(opcion))
    print("Adiós")

opcion = int(input("Elige la opción 1, 2 o 3"))
if opcion == 1:
    conversacion(opcion)
elif opcion == 2:
    conversacion(opcion)
elif opcion == 3:
    conversacion(opcion)
else:
    print("Opción no valida")
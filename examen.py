# Examen práctico - Sistema de pedidos del kiosco
# Nombre y apellido:
# Curso:
#
# IMPORTANTE:
# Resolver el programa siguiendo las etapas indicadas en el README.md.
# Realizar los commits y push cuando se indique.



# =========================
# ETAPA 1 - INICIO
# =========================
nombre = input("¿cual es su nombre?")
saldo = int(input("¿Cual es su saldo actual?"))
productos = ["agua", "alfajor", "tostado"]
precios = ["$700", "$900","$2200"]

print("Bienvenid: ",nombre, "saldo: ",saldo)



# =========================
# ETAPA 2 - COMPRAS
# =========================

print("1. Agua       - $700")
print("2. Alfajor    - $900")
print("3. Tostado    - $2200")
print("4. Consultar pedido")
print("5. Finalizar compra")
opcion = int(input("Elija la opcion"))

if opcion == 1:
    print("Producto: ", productos [0])
    print("Precio: ", precios [0])
    if saldo < 700:
        print("No le alcanza")
    saldo = saldo - 700
    cant_aguas += 1
if opcion == 2:
    print("Producto: ", productos [1])
    print("Precio: ", precios [1])
    if saldo < 900:
     print("No le alcanza")
    saldo = saldo - 900
    cant_alfajores += 1
if opcion == 3:
    print("Producto: ", productos [-1])
    print("Precio: ", precios [-1])
    if saldo < 2200:
     print ("No le alcanza")
    saldo = saldo - 2200
# =========================
# ETAPA 3 - CICLO PRINCIPAL
# =========================

# Modificar el programa para que continúe funcionando
# hasta que el usuario decida finalizar la compra.


# =========================
# ETAPA 4 - PEDIDO Y RESUMEN
# =========================

# Mostrar el estado actual del pedido.
# Recorrer las listas con un for para mostrar productos y precios.

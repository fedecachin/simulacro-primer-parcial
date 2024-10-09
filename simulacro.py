import os

def agregar_producto(lista: list, tipo: str, precio: float, cantidad: int):
    lista.append([tipo, precio, cantidad])

def cargar_productos(lista: list):
    respuesta = "si"
    while respuesta == "si":
        tipo = input("producto: ")
        precio = input("precio: ")
        cantidad = input("cantidad: ")
        respuesta = input("desea cargar otro producto: ")

        agregar_producto(lista, tipo, precio, cantidad)

def buscar_producto(lista: list, nombre: str):
    for producto in lista:
        if producto[0] == nombre:
            return producto
        
def buscar_producto_mas_caro_barato(lista: list) -> str:
    bandera_caro = 0
    bandera_barato = 0
    for producto in lista:
        if bandera_caro == 0 or producto[1] > mas_caro[1]:
            mas_caro = producto
            bandera_caro = 1
        if bandera_barato == 0 or producto[1] < mas_barato[1]:
            mas_barato = producto
            bandera_barato = 1
    return f"el producto mas barato es: {mas_barato}\nel producto mas caro es: {mas_caro}"

inventario = [
    ["Laptop", 1500.00, 10],
    ["Silla", 200.00, 50],
    ["Libro", 15.00, 100],
    ["Monitor", 300.00,30]
]
while True:
    os.system("cls")
    
    opcion = input("""
    1. Cargar producto/s 
    2. Buscar producto 
    3. Ordenar inventario
    4. Mostrar producto más caro y más barato
    5. Mostrar productos con precio mayor a 15000
    6. Salir
    
    elija una opcion: """)

    os.system("cls")

    match opcion:
        case "1":
            cargar_productos(inventario)
        case "2":
            nombre = input("ingrese el nombre del producto a mostrar: ")
            producto = buscar_producto(inventario, nombre)
            print(producto)
            input("")
        case "3":
            break
        case "4":
            print(buscar_producto_mas_caro_barato(inventario))
            input("")
        case "5":
            break
        case "6":
            break
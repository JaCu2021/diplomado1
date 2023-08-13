# Definir una lista de productos con sus nombres, precios y cantidades disponibles
productos = [
    {"nombre": "Camiseta básica unisex", "precio": 40000, "cantidad_disponible": 50},
    {"nombre": "Camisa manga larga hombre", "precio": 85000, "cantidad_disponible": 30},
    {"nombre": "Blusa de encaje", "precio": 115000, "cantidad_disponible": 25},
    {"nombre": "Chaqueta de cuero", "precio": 180000, "cantidad_disponible": 20},
    {"nombre": "Pantalones de lino hombre", "precio": 90000, "cantidad_disponible": 40},
    {"nombre": "Jeans mujer ajustados", "precio": 120000, "cantidad_disponible": 60},
    {"nombre": "Jeans hombre ajustados", "precio": 100000, "cantidad_disponible": 15},
    {"nombre": "Vestido de cóctel", "precio": 250000, "cantidad_disponible": 12},
    {"nombre": "Cinturón de cuero", "precio": 70000, "cantidad_disponible": 35},
    {"nombre": "Zapatos de tacón", "precio": 155000, "cantidad_disponible": 18}
]

# Mostrar la lista de productos al usuario
print("Lista de productos disponibles:")
for i, producto in enumerate(productos, start=1):
    print(f"{i}. {producto['nombre']}: ${producto['precio']} (Disponibles: {producto['cantidad_disponible']})")

# Solicitar al usuario que elija productos y cantidades
carrito = []
while True:
    seleccion = input("Seleccione el número de producto que desea comprar (o 'q' para finalizar): ")

    if seleccion == 'q':
        break

    try:
        seleccion_num = int(seleccion)
        if 1 <= seleccion_num <= len(productos):
            producto_elegido = productos[seleccion_num - 1]
            cantidad = int(input(f"Ingrese la cantidad de '{producto_elegido['nombre']}' que desea comprar: "))
            if cantidad <= producto_elegido['cantidad_disponible']:
                carrito.append({"producto": producto_elegido, "cantidad": cantidad})
                producto_elegido['cantidad_disponible'] -= cantidad
                print("Producto agregado al carrito.")
            else:
                print("No hay suficiente cantidad disponible.")
        else:
            print("Seleccione un número válido.")
    except ValueError:
        print("Ingrese un número válido o 'q' para finalizar.")

# Mostrar los productos en el carrito y el total a pagar
print("\nProductos en el carrito:")
total_a_pagar = 0
for item in carrito:
    subtotal = item['producto']['precio'] * item['cantidad']
    total_a_pagar += subtotal
    print(f"{item['producto']['nombre']} - Cantidad: {item['cantidad']} - Subtotal: ${subtotal:.2f}")

print(f"Total a pagar: ${total_a_pagar:.2f}")

# Solicitar la aprobación del pedido al usuario
aprobacion = input("¿Desea aprobar el pedido? (s/n): ")

# Mostrar mensajes según la aprobación
if aprobacion.lower() == 's':
    print("\nResumen de la compra:")
    for item in carrito:
        print(
            f"{item['producto']['nombre']} - Cantidad: {item['cantidad']} - Subtotal: ${item['producto']['precio'] * item['cantidad']:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")
    print("Compra aprobada. ¡Gracias por su compra!")
else:
    print("Pedido cancelado. ¡Esperamos atenderle en otro momento!")

# Fin del programa
from inventario import Inventario
from ventas import GestorVentas
from reportes import Reportes
from utilidades import leer_entero, leer_decimal, pausar


def mostrar_menu():
    print("\n" + "=" * 58)
    print(" SISTEMA DE GESTIÓN DE INVENTARIO Y VENTAS ")
    print("=" * 58)
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Reabastecer producto")
    print("4. Registrar venta")
    print("5. Ver ingresos y utilidad")
    print("6. Ver productos más vendidos")
    print("7. Ver productos con stock bajo")
    print("8. Generar gráfica de ventas")
    print("9. Salir")


def agregar_producto(inventario):
    print("\n--- Agregar producto ---")
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría (Escolar/Juguete/Otro): ").strip()
    precio_compra = leer_decimal("Precio de compra: $", minimo=0)
    precio_venta = leer_decimal("Precio de venta: $", minimo=0)
    stock = leer_entero("Stock inicial: ", minimo=0)

    try:
        producto = inventario.agregar_producto(
            nombre, categoria, precio_compra, precio_venta, stock
        )
        print(f"Producto registrado con ID {producto.id_producto}.")
    except ValueError as error:
        print(f"No fue posible registrar el producto: {error}")


def reabastecer(inventario):
    inventario.mostrar_inventario()
    id_producto = leer_entero("ID del producto: ", minimo=1)
    cantidad = leer_entero("Cantidad que se agregará: ", minimo=1)
    try:
        inventario.reabastecer(id_producto, cantidad)
        print("Existencias actualizadas correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def registrar_venta(inventario, gestor_ventas):
    inventario.mostrar_inventario()
    id_producto = leer_entero("ID del producto vendido: ", minimo=1)
    cantidad = leer_entero("Cantidad vendida: ", minimo=1)
    try:
        venta = gestor_ventas.registrar_venta(id_producto, cantidad)
        print("\nVenta registrada correctamente.")
        print(f"Folio: {venta.id_venta}")
        print(f"Producto: {venta.nombre_producto}")
        print(f"Cantidad: {venta.cantidad}")
        print(f"Total: ${venta.total_venta:.2f}")
    except ValueError as error:
        print(f"No fue posible registrar la venta: {error}")


def ejecutar():
    inventario = Inventario("productos.csv")
    gestor_ventas = GestorVentas(inventario, "ventas.csv")
    reportes = Reportes("productos.csv", "ventas.csv")

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            agregar_producto(inventario)
        elif opcion == "2":
            inventario.mostrar_inventario()
        elif opcion == "3":
            reabastecer(inventario)
        elif opcion == "4":
            registrar_venta(inventario, gestor_ventas)
        elif opcion == "5":
            reportes.mostrar_resumen_financiero()
        elif opcion == "6":
            reportes.mostrar_productos_mas_vendidos()
        elif opcion == "7":
            limite = leer_entero("Mostrar productos con stock igual o menor a: ", minimo=0)
            reportes.mostrar_stock_bajo(limite)
        elif opcion == "8":
            reportes.generar_grafica()
        elif opcion == "9":
            print("Datos guardados. Fin del programa.")
            break
        else:
            print("Opción no válida. Elige un número del 1 al 9.")

        pausar()


if __name__ == "__main__":
    ejecutar()

import csv
from pathlib import Path
from producto import Producto


class Inventario:
    CAMPOS = [
        "id_producto", "nombre", "categoria", "precio_compra",
        "precio_venta", "stock"
    ]

    def __init__(self, ruta_csv):
        self.ruta_csv = Path(ruta_csv)
        self.productos = []
        self._crear_archivo_si_no_existe()
        self.cargar()

    def _crear_archivo_si_no_existe(self):
        if not self.ruta_csv.exists():
            with self.ruta_csv.open("w", newline="", encoding="utf-8-sig") as archivo:
                writer = csv.DictWriter(archivo, fieldnames=self.CAMPOS)
                writer.writeheader()

    def cargar(self):
        self.productos = []
        with self.ruta_csv.open("r", newline="", encoding="utf-8-sig") as archivo:
            for fila in csv.DictReader(archivo):
                if not fila.get("id_producto"):
                    continue
                self.productos.append(Producto(
                    int(fila["id_producto"]), fila["nombre"], fila["categoria"],
                    float(fila["precio_compra"]), float(fila["precio_venta"]),
                    int(fila["stock"])
                ))

    def guardar(self):
        with self.ruta_csv.open("w", newline="", encoding="utf-8-sig") as archivo:
            writer = csv.DictWriter(archivo, fieldnames=self.CAMPOS)
            writer.writeheader()
            writer.writerows(producto.a_fila_csv() for producto in self.productos)

    def siguiente_id(self):
        return max((p.id_producto for p in self.productos), default=0) + 1

    def agregar_producto(self, nombre, categoria, precio_compra, precio_venta, stock):
        if any(p.nombre.lower() == nombre.strip().lower() for p in self.productos):
            raise ValueError("Ya existe un producto con ese nombre.")
        if precio_venta < precio_compra:
            raise ValueError("El precio de venta no puede ser menor al precio de compra.")
        producto = Producto(
            self.siguiente_id(), nombre.strip(), categoria.strip() or "Otro",
            precio_compra, precio_venta, stock
        )
        self.productos.append(producto)
        self.guardar()
        return producto

    def buscar_por_id(self, id_producto):
        return next((p for p in self.productos if p.id_producto == id_producto), None)

    def reabastecer(self, id_producto, cantidad):
        producto = self.buscar_por_id(id_producto)
        if not producto:
            raise ValueError("Producto no encontrado.")
        producto.agregar_stock(cantidad)
        self.guardar()

    def mostrar_inventario(self):
        print("\n--- Inventario actual ---")
        if not self.productos:
            print("No hay productos registrados.")
            return
        encabezado = f"{'ID':<5}{'Producto':<22}{'Categoría':<14}{'Compra':>10}{'Venta':>10}{'Stock':>8}"
        print(encabezado)
        print("-" * len(encabezado))
        for p in self.productos:
            print(f"{p.id_producto:<5}{p.nombre:<22.22}{p.categoria:<14.14}"
                  f"${p.precio_compra:>9.2f}${p.precio_venta:>9.2f}{p.stock:>8}")

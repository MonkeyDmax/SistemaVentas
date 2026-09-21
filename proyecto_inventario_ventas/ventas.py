import csv
from datetime import datetime
from pathlib import Path
from venta import Venta


class GestorVentas:
    CAMPOS = [
        "id_venta", "fecha", "id_producto", "nombre_producto", "cantidad",
        "precio_compra_unitario", "precio_unitario", "total_venta", "utilidad"
    ]

    def __init__(self, inventario, ruta_csv):
        self.inventario = inventario
        self.ruta_csv = Path(ruta_csv)
        self._crear_archivo_si_no_existe()

    def _crear_archivo_si_no_existe(self):
        if not self.ruta_csv.exists():
            with self.ruta_csv.open("w", newline="", encoding="utf-8-sig") as archivo:
                writer = csv.DictWriter(archivo, fieldnames=self.CAMPOS)
                writer.writeheader()

    def siguiente_id(self):
        mayor = 0
        with self.ruta_csv.open("r", newline="", encoding="utf-8-sig") as archivo:
            for fila in csv.DictReader(archivo):
                if fila.get("id_venta"):
                    mayor = max(mayor, int(fila["id_venta"]))
        return mayor + 1

    def registrar_venta(self, id_producto, cantidad):
        producto = self.inventario.buscar_por_id(id_producto)
        if not producto:
            raise ValueError("Producto no encontrado.")
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        producto.reducir_stock(cantidad)

        total = round(cantidad * producto.precio_venta, 2)
        utilidad = round(cantidad * (producto.precio_venta - producto.precio_compra), 2)
        venta = Venta(
            self.siguiente_id(), datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            producto.id_producto, producto.nombre, cantidad,
            producto.precio_compra, producto.precio_venta, total, utilidad
        )

        # Primero se registra la venta y después se actualiza el inventario.
        # Ante un error de escritura, el stock se restaura en memoria.
        try:
            with self.ruta_csv.open("a", newline="", encoding="utf-8-sig") as archivo:
                writer = csv.DictWriter(archivo, fieldnames=self.CAMPOS)
                writer.writerow(venta.a_fila_csv())
            self.inventario.guardar()
        except OSError:
            producto.agregar_stock(cantidad)
            raise ValueError("No fue posible guardar la venta.")
        return venta

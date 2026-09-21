import csv
from collections import defaultdict
from pathlib import Path


class Reportes:
    def __init__(self, productos_csv, ventas_csv):
        self.productos_csv = Path(productos_csv)
        self.ventas_csv = Path(ventas_csv)

    def _leer_ventas(self):
        if not self.ventas_csv.exists():
            return []
        with self.ventas_csv.open("r", newline="", encoding="utf-8-sig") as archivo:
            return list(csv.DictReader(archivo))

    def _leer_productos(self):
        if not self.productos_csv.exists():
            return []
        with self.productos_csv.open("r", newline="", encoding="utf-8-sig") as archivo:
            return list(csv.DictReader(archivo))

    def mostrar_resumen_financiero(self):
        ventas = self._leer_ventas()
        ingresos = sum(float(v["total_venta"]) for v in ventas)
        utilidad = sum(float(v["utilidad"]) for v in ventas)
        unidades = sum(int(v["cantidad"]) for v in ventas)
        print("\n--- Resumen financiero ---")
        print(f"Operaciones registradas: {len(ventas)}")
        print(f"Unidades vendidas: {unidades}")
        print(f"Ingresos totales: ${ingresos:.2f}")
        print(f"Utilidad estimada: ${utilidad:.2f}")
        print("Nota: la utilidad no contempla gastos como transporte o renta.")

    def mostrar_productos_mas_vendidos(self):
        acumulado = defaultdict(lambda: {"cantidad": 0, "ingresos": 0.0})
        for venta in self._leer_ventas():
            nombre = venta["nombre_producto"]
            acumulado[nombre]["cantidad"] += int(venta["cantidad"])
            acumulado[nombre]["ingresos"] += float(venta["total_venta"])

        print("\n--- Productos más vendidos ---")
        if not acumulado:
            print("Todavía no hay ventas registradas.")
            return
        ordenados = sorted(acumulado.items(), key=lambda x: x[1]["cantidad"], reverse=True)
        print(f"{'Producto':<24}{'Unidades':>10}{'Ingresos':>14}")
        print("-" * 48)
        for nombre, datos in ordenados:
            print(f"{nombre:<24.24}{datos['cantidad']:>10}${datos['ingresos']:>13.2f}")

    def mostrar_stock_bajo(self, limite=5):
        productos = [p for p in self._leer_productos() if int(p["stock"]) <= limite]
        print(f"\n--- Productos con stock igual o menor a {limite} ---")
        if not productos:
            print("No hay productos con stock bajo.")
            return
        for p in sorted(productos, key=lambda x: int(x["stock"])):
            print(f"ID {p['id_producto']}: {p['nombre']} - {p['stock']} unidades")

    def generar_grafica(self):
        acumulado = defaultdict(int)
        for venta in self._leer_ventas():
            acumulado[venta["nombre_producto"]] += int(venta["cantidad"])
        if not acumulado:
            print("No hay ventas para graficar.")
            return
        try:
            import matplotlib.pyplot as plt
        except ImportError:
            print("No está instalada la librería matplotlib.")
            print("Instálala con: pip install matplotlib")
            return

        ordenados = sorted(acumulado.items(), key=lambda x: x[1], reverse=True)
        nombres = [x[0] for x in ordenados]
        cantidades = [x[1] for x in ordenados]
        plt.figure(figsize=(9, 5))
        plt.bar(nombres, cantidades)
        plt.title("Unidades vendidas por producto")
        plt.xlabel("Producto")
        plt.ylabel("Unidades vendidas")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        salida = "grafica_ventas.png"
        plt.savefig(salida, dpi=150)
        plt.close()
        print(f"Gráfica guardada como {salida}.")

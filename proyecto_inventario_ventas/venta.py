from dataclasses import dataclass


@dataclass
class Venta:
    id_venta: int
    fecha: str
    id_producto: int
    nombre_producto: str
    cantidad: int
    precio_compra_unitario: float
    precio_unitario: float
    total_venta: float
    utilidad: float

    def a_fila_csv(self):
        return {
            "id_venta": self.id_venta,
            "fecha": self.fecha,
            "id_producto": self.id_producto,
            "nombre_producto": self.nombre_producto,
            "cantidad": self.cantidad,
            "precio_compra_unitario": f"{self.precio_compra_unitario:.2f}",
            "precio_unitario": f"{self.precio_unitario:.2f}",
            "total_venta": f"{self.total_venta:.2f}",
            "utilidad": f"{self.utilidad:.2f}",
        }

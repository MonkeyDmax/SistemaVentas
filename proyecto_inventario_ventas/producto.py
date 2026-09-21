from dataclasses import dataclass


@dataclass
class Producto:
    id_producto: int
    nombre: str
    categoria: str
    precio_compra: float
    precio_venta: float
    stock: int

    def __post_init__(self):
        if self.id_producto <= 0:
            raise ValueError("El ID debe ser mayor que cero.")
        if not self.nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if self.precio_compra < 0 or self.precio_venta < 0:
            raise ValueError("Los precios no pueden ser negativos.")
        if self.stock < 0:
            raise ValueError("El stock no puede ser negativo.")

    def agregar_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.stock += cantidad

    def reducir_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if cantidad > self.stock:
            raise ValueError(f"Stock insuficiente. Solo hay {self.stock} unidades.")
        self.stock -= cantidad

    def a_fila_csv(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio_compra": f"{self.precio_compra:.2f}",
            "precio_venta": f"{self.precio_venta:.2f}",
            "stock": self.stock,
        }

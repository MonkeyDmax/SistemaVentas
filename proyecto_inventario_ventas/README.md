# Sistema de Gestión de Inventario y Ventas

Proyecto universitario en Python para un pequeño negocio familiar que vende artículos escolares y juguetes.

## Funcionalidades

- Alta de productos.
- Consulta y reabastecimiento del inventario.
- Registro de ventas con validación de stock.
- Actualización automática de existencias.
- Cálculo de ingresos y utilidad estimada.
- Reporte de productos más vendidos.
- Alerta de stock bajo.
- Gráfica de unidades vendidas por producto.

## Requisitos

- Python 3.10 o posterior.
- `matplotlib` solo para la opción de gráfica.

## Ejecución

1. Descomprime el proyecto.
2. Abre una terminal dentro de la carpeta.
3. Ejecuta:

```bash
python main.py
```

Para habilitar la gráfica:

```bash
pip install matplotlib
```

## Archivos

- `main.py`: menú e interacción con el usuario.
- `producto.py`: clase Producto.
- `venta.py`: clase Venta.
- `inventario.py`: lectura, escritura y operaciones de inventario.
- `ventas.py`: registro de ventas.
- `reportes.py`: reportes y gráfica.
- `utilidades.py`: validación de entradas.
- `productos.csv`: catálogo e inventario.
- `ventas.csv`: historial de ventas.

## Fórmulas

- Total de venta = cantidad × precio de venta.
- Utilidad estimada = cantidad × (precio de venta - precio de compra).

La utilidad es una estimación y no contempla transporte, renta del puesto u otros gastos.

from producto import Producto
from inventario import Inventario

inventario = Inventario()

producto_uno = Producto(1, "Iphone 16 Pro Max", 31000, "Iphone", "rojo")
producto_dos = Producto(2, "Iphone 15 Pro Max", 25000, "Iphone", "negro")
producto_tres = Producto(3, "Iphone 14 Pro Max", 20000, "Iphone", "blanco")

inventario.agregar_producto(producto_uno)
inventario.agregar_producto(producto_dos)
inventario.agregar_producto(producto_tres)

inventario.mostrar_productos()

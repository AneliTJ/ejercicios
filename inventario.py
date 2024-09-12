class Inventario:
    productos = []

    # Agregar productos
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Eliminar productos
    def eliminar_producto(self):
        pass

    def mostrar_productos(self):
        print("\n----- Productos en el Sistema -----")
        for producto in self.productos:
            print("\n")
            print("Id: ", producto.id)
            print("Nombre: ", producto.nombre)
            print("Precio", producto.precio)
            print("Categoria: ", producto.categoria)
            print("Color: ", producto.color)

#solo es un comentario
class Producto:
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int ):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def get_id_producto(self):
        return self.__id_producto
    
    def set_id_producto(self, id_producto):
        self.__id_producto = id_producto

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
    
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.__precio = precio
    
    def get_stock(self):
        return self.__stock
    
    def set_stock(self,stock):
        self.__stock = stock

    def __str__(self):
        return f' ID: {self.get_id_producto()} Producto: {self.get_nombre()} Precio: {self.get_precio()} Stock: {self.get_stock()}'


    def actualizar_stock(self,cantidad: int):
        self.set_stock(cantidad)


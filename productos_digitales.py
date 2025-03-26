from productos import Producto

class ProductoDigital(Producto):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, formato: str, tamano: float):
        super().__init__(id_producto, nombre, precio, stock)
        self.__formato = formato
        self.__tamano = tamano

    def get_formato(self):
        return self.__formato
    
    def set_formato(self,formato):
        self.__formato =formato

    def get_tamano(self):
        return self.__tamano
    
    def set_tamano(self,tamano):
        self.__tamano = tamano

    def __str__(self):
        return  f'ID : {self.get_id_producto()} Producto: {self.get_nombre()} Precio {self.get_precio()} Stock: {self.get_stock()} Formato {self.get_formato()} Tamano: {self.get_tamano()}'
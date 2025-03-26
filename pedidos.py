from clientes import Cliente
from productos import Producto

class Pedido:
    def __init__(self, id_pedido: str, cliente: Cliente, fecha: str):
        self.__id_pedido = id_pedido
        self.__cliente = cliente
        self.__productos = []
        self.__fecha = fecha

    def get_id_pedido(self):
        return self.__id_pedido
    
    def set_id_pedido(self,id_pedido):
        self.__id_pedido = id_pedido

    def get_cliente(self):
        return self.__cliente
    
    def set_cliente(self,cliente):
        self.__cliente = cliente

    def get_productos(self):
        return self.__productos
    
    def set_productos(self,productos):
        self.__productos = productos

    def get_fecha(self):
        return self.__fecha
    
    def set_fecha(self,fecha):
        self.__fecha = fecha

    def agregar_producto(self, producto: Producto):
        self.__productos.append(producto)

    def calcular_total(self):
        total = 0
        for i in self.__productos:
            total += self.__productos.get_precio()

    def __str__(self):
        return f' ID: {self.get_id_pedido()} Cliente: {self.get_cliente()} Productos: {self.get_productos()} Fecha: {self.get_fecha()}'
    


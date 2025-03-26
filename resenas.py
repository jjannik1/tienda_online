from productos import Producto
from clientes import Cliente

class Resena(Producto,Cliente):
    def __init__(self,id_resena: str, producto: Producto, cliente: Cliente, comentario: str, puntuacion: int):
        Producto.__init__(self,producto.get_id_producto(),producto.get_nombre(),producto.get_precio(),producto.get_stock())
        Cliente.__init__(self,cliente.get_id_cliente(),cliente.get_nombre(),cliente.get_email(),cliente.get_direccion())
        self.__id_resena = id_resena
        self.__comentario = comentario
        self.__puntuacion = puntuacion


    def get_id_resena(self):
        return self.__id_resena
    
    def get_comentario(self):
        return self.__comentario
    
    def get_puntuacion(self):
        return self.__puntuacion
    
    def set_id_resena(self,id_resena):
        self.__id_resena = id_resena

    def set_comentario(self,comentario):
        self.__comentario = comentario

    def set_puntuacion(self,puntuacion):
        self.__puntuacion = puntuacion

    def __str__(self):
        return f'ID: {self.get_id_resena()} Producto: {self.get_id_producto()} Cliente: {self.get_id_cliente()} Comentario: {self.get_comentario()} Puntuacion: {self.get_puntuacion()}'
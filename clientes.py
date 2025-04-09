class Cliente:
    def __init__(self,id_cliente: str, nombre: str, email: str, direccion: str):
        """_summary_

        :param id_cliente: _description_
        :type id_cliente: str
        :param nombre: _description_
        :type nombre: str
        :param email: _description_
        :type email: str
        :param direccion: _description_
        :type direccion: str
        """
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion

    def get_id_cliente(self):
        return self.__id_cliente
    
    def set_id_cliente(self,id_cliente):
        self.__id_cliente = id_cliente

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_email(self):
        return self.__email
    
    def set_email(self,email):
        self.__email = email

    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self,direccion):
        self.__direccion = direccion

    def __str__(self):
        return f' ID: {self.get_id_cliente()} Nombre: {self.get_nombre()} Email: {self.get_email()} Direccion: {self.get_direccion()}'
    


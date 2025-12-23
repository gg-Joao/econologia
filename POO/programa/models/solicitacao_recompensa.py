class SolicitacaoRecompensa:
    def __init__(self, id = None, data = None, confirmado = False, item = None):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(confirmado)
        self.set_item(item)

    def __str__(self):
        return f'ID: {self.get_id()} - DATA: {self.get_data()} - CONFIRMADA: {self.get_confirmado()} - ITEM: {self.get_item()}'

    def set_id(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id

    def set_data(self, data):
        self.__data = data
    
    def get_data(self):
        return self.__data
    
    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado
    
    def get_confirmado(self):
        return self.__confirmado
    
    def set_item(self, item):
        self.__item = item

    def get_item(self):
        return self.__item
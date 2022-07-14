
class Saludo:
    def __init__(self, name) -> None:
        self.name = name
        
    def saludar(self):
        return f'Hola {self.name} este paquete te envia un saludo'
    
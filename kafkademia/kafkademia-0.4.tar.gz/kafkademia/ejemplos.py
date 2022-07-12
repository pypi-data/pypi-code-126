from datetime import datetime
import random
from uuid import uuid4

class ATM(object):
    def __init__(self, atm_id_min=1, atm_id_max=100, mov_min:int=-5000, mov_max:int=-100):
        self.atm_id_min = atm_id_min
        self.atm_id_max = atm_id_max
        self.id_sucursal_min = atm_id_min # igual que el min para id atm
        self.id_sucursal_max = atm_id_max # igual que el max para id atm
        self.user_id = str()
        self.mov_min = mov_min
        self.mov_max = mov_max
    
    def generar_mensaje(self):
        id_atm = random.randint(self.atm_id_min, self.atm_id_max)
        id_sucursal = random.randint(self.id_sucursal_min, self.id_sucursal_max)
        movimiento = random.randint(self.mov_min, self.mov_max)
        hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.user_id = str(uuid4())
        
        mensaje_atm = {
            "id_atm" : id_atm,
            "id_usuario" : self.user_id,
            "id_sucursal": id_sucursal,
            "hora" : hora,
            "movimiento" : movimiento
        }
        return mensaje_atm

class Venta(object):
    def __init__(self, min_venta:float=100.0, max_venta:float=3490.0, id_vendedor_min:int=1, id_vendedor_max:int=100):
        self.min_venta = min_venta
        self.max_venta = max_venta
        self.id_vendedor_min = id_vendedor_min
        self.id_vendedor_max = id_vendedor_max
        self.id_sucursal_min = id_vendedor_min # igual que el min para id vendedor
        self.id_sucursal_max = id_vendedor_max # igual que el max para id vendedor

    def generar_mensaje(self):
        total_venta = random.randint(self.min_venta, self.max_venta)
        dinero_recibido = random.randint(total_venta, total_venta+50)
        id_vendedor = random.randint(self.id_vendedor_min, self.id_vendedor_max)
        id_sucursal = random.randint(self.id_sucursal_min, self.id_sucursal_max)
        mensaje_venta = {
            "total" : total_venta,
            "dinero_recibido" : dinero_recibido,
            "vuelto" : dinero_recibido-total_venta,
            "vendedor": id_vendedor,
            "sucursal": id_sucursal
        }
        return mensaje_venta
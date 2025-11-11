import threading
import time
import random

class Cocinero(threading.Thread):
    def __init__(self, id_cocinero, cocina):
        super().__init__()
        self.id_cocinero = id_cocinero
        self.cocina = cocina

    def run(self):
        while True:
            pedido = self.cocina.tomar_pedido()
            if pedido is None:
                break
            self.preparar_pedido(pedido)

    def preparar_pedido(self, pedido):
        print(f"Cocinero {self.id_cocinero} está preparando el pedido {pedido.id}: {pedido.nombre_plato}")
        time.sleep(random.uniform(1, 3))  # Simula tiempo de preparación
        self.cocina.registrar_pedido(pedido, self.id_cocinero)

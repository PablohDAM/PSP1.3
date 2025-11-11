import threading
from pedido import Pedido

class Cocina:
    def __init__(self):
        self.lista_pedidos = [
            Pedido(1, "Paella"),
            Pedido(2, "Tortilla"),
            Pedido(3, "Gazpacho"),
            Pedido(4, "Croquetas"),
            Pedido(5, "Ensalada"),
            Pedido(6, "Fabada")
        ]
        self.lock = threading.Lock()
        self.log_file_path = "log_pedidos.txt"
        with open(self.log_file_path, "w") as f:
            f.write("")

    def tomar_pedido(self):
        with self.lock:
            if not self.lista_pedidos:
                return None
            return self.lista_pedidos.pop(0)

    def registrar_pedido(self, pedido, id_cocinero):
        with self.lock:
            with open(self.log_file_path, "a") as f:
                log = f"Pedido {pedido.id} ({pedido.nombre_plato}) preparado por cocinero {id_cocinero}\n"
                f.write(log)

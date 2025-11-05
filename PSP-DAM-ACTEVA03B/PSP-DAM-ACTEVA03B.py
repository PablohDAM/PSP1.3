import threading
import time
import random

class Pedido:
    def __init__(self, id, nombre_plato):
        self.id = id
        self.nombre_plato = nombre_plato

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
        self.log_file_path = "PSP-DAM-ACTEVA03B/log_pedidos.txt"
        # Limpiar archivo log al comenzar
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

def main():
    cocina = Cocina()
    cocineros = [Cocinero(1, cocina), Cocinero(2, cocina), Cocinero(3, cocina)]

    for c in cocineros:
        c.start()

    for c in cocineros:
        c.join()

    print("Todos los pedidos han sido procesados.")

if __name__ == "__main__":
    main()

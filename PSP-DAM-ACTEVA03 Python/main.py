from cocina import Cocina
from cocinero import Cocinero

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

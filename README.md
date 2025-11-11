# PSP1.3


## Descripción

Simulación concurrente en una cocina donde varios cocineros (hilos) procesan pedidos de una lista compartida y registran la operación en un archivo `log_pedidos.txt`. El objetivo principal es practicar la sincronización de hilos, garantizando el acceso exclusivo tanto a la lista como al registro de pedidos, usando herramientas específicas de Java (`synchronized`) y Python (`threading.Lock`).



- **PSP-DAM-ACTEVA03B.py:** Contienen la lógica principal de la cocina, gestión de pedidos y sincronización.
- **Cocinero.java / clase Cocinero (Python):** Implementan el comportamiento del hilo cocinero: tomar, preparar y registrar pedidos.
- **Pedido.java / clase Pedido (Python):** Modelan el pedido con identificador y nombre del plato.
- **GestionCocina.java:** Lanzador para la versión Java.
- **log_pedidos.txt:** Archivo de registro de operaciones concurrentes.

## Funcionamiento

1. Al iniciar el programa, se crean al menos seis pedidos en la cocina.
2. Tres cocineros (Java: threads; Python: Thread) procesan los pedidos extraídos de la lista compartida.
3. Cada cocinero simula la preparación mediante una pausa aleatoria, y registra la operación en el archivo log con acceso sincronizado.
4. El proceso termina cuando todos los pedidos han sido procesados y registrados.

## Sincronización

- **Java:** Se usan métodos `synchronized` en la clase `Cocina` para tomar y registrar pedidos, asegurando que sólo un hilo acceda a la lista y al archivo simultáneamente.
- **Python:** Se emplea `threading.Lock()` para proteger las operaciones de acceso/registro, evitando condiciones de carrera.


## Salida de ejecución

A medida que se van gestionando las operaciones se va sacando la información por la consola

Las operaciones realizadas por cada cocinero quedan reflejadas en `log_pedidos.txt` de forma ordenada y segura.

## Requisitos

- **Java:** JDK 8 o superior.
- **Python:** Python 3.7+.



## Créditos y contexto académico

Proyecto para la unidad de Programación de Servicios y Procesos (PSP) del ciclo DAM. Ejercicio orientado a la práctica de concurrencia y sincronización en aplicaciones reales.

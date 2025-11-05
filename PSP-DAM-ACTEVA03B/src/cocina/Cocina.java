package cocina;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


public class Cocina {
    private List<Pedido> listaPedidos = new ArrayList<>();
    private FileWriter logFile;

    public Cocina() {
        try {
            logFile = new FileWriter("log_pedidos.txt", true); // Archivo en modo append
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Añadir al menos 6 pedidos
        listaPedidos.add(new Pedido(1, "Paella"));
        listaPedidos.add(new Pedido(2, "Tortilla"));
        listaPedidos.add(new Pedido(3, "Gazpacho"));
        listaPedidos.add(new Pedido(4, "Croquetas"));
        listaPedidos.add(new Pedido(5, "Ensalada"));
        listaPedidos.add(new Pedido(6, "Fabada"));
    }

    // Método sincronizado para acceder a pedidos
    public synchronized Pedido tomarPedido() {
        if (listaPedidos.isEmpty()) {
            return null;
        }
        return listaPedidos.remove(0);
    }

    // Método sincronizado para registrar en log
    public synchronized void registrarPedido(Pedido pedido, int idCocinero) {
        try {
            String log = "Pedido " + pedido.getId() + " (" + pedido.getNombrePlato() + ") preparado por cocinero " + idCocinero + "\n";
            logFile.write(log);
            logFile.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void iniciarCocina() {
        // Crear 3 cocineros
        Cocinero c1 = new Cocinero(1, this);
        Cocinero c2 = new Cocinero(2, this);
        Cocinero c3 = new Cocinero(3, this);

        c1.start();
        c2.start();
        c3.start();

        try {
            c1.join();
            c2.join();
            c3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        try {
            logFile.close();
        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Todos los pedidos han sido procesados.");
    }

    public static void main(String[] args) {
        Cocina cocina = new Cocina();
        cocina.iniciarCocina();
    }
}

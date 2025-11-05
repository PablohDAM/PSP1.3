package cocina;

class Cocinero extends Thread {
    private int idCocinero;
    private Cocina cocina;

    public Cocinero(int idCocinero, Cocina cocina) {
        this.idCocinero = idCocinero;
        this.cocina = cocina;
    }

    @Override
    public void run() {
        while (true) {
            Pedido pedido = cocina.tomarPedido();
            if (pedido == null) { // No quedan pedidos
                break;
            }
            prepararPedido(pedido);
        }
    }

    private void prepararPedido(Pedido pedido) {
        System.out.println("Cocinero " + idCocinero + " está preparando el pedido " + pedido.getId() + ": " + pedido.getNombrePlato());
        try {
            Thread.sleep((long) (Math.random() * 2000) + 1000); // Simula el tiempo de preparación
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        cocina.registrarPedido(pedido, idCocinero);
    }
}
package fase5.estruturas_de_controle;

public class LacoRepeticaoDoWhile {
    public static void main(String[] args) {
        int contador = 1;

        do {
            System.out.println("Contador: " + contador);
            contador++;
        } while (contador <= 10);
    }
}

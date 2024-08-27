package fase5.estruturas_de_controle;

public class LacoRepeticaoFor {
    public static void main(String[] args) {
        System.out.println("Contagem de 0 a 10");
        for (int contador = 0; contador <= 10; contador++) {
            System.out.println("Contador = " + contador);
        }

        System.out.println("Contagem de 10 a 0");
        for (int iterador = 10; iterador >= 0; iterador--) {
            System.out.println("Contador = " + iterador);
        }
    }

}
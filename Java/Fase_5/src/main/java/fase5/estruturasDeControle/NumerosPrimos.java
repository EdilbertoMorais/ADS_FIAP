package fase5.estruturasDeControle;

import java.util.Scanner;

public class NumerosPrimos {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite um número maior que 1: ");
        int numero = scanner.nextInt();

        if (numero <= 1) {
            System.out.println("Número inválido.");
        }else {
            boolean ehPrimo = true;

            for (int i = 2; i < numero; i++) {
                if (numero % i == 0) {
                    ehPrimo = false;
                    break;
                }
            }

            if (ehPrimo) {
                System.out.println("O número " + numero + " é primo.");
            }else {
                System.out.println("O número " + numero + " não é primo.");
            }
        }
    }
}
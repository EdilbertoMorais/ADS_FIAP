package fase5.estruturasDeControle;

import java.util.Scanner;

public class MostraNumerosPrimos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite o número máximo para mostrar os números primos: ");
        int numero = sc.nextInt();

        for (int i = 2; i <= numero; i++) {
            boolean ehPrimo = true; // Assume que o número é primo

            // Verifica se o número é divisível por qualquer número entre 2 e a raiz quadrada de i
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    ehPrimo = false; // Não é primo
                    break;
                }
            }

            if (ehPrimo) {
                System.out.println(i);
            }
        }
        sc.close();
    }
}
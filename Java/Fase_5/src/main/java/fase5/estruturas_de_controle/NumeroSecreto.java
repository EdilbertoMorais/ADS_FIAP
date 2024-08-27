package fase5.estruturas_de_controle;

import java.util.Random;
import java.util.Scanner;

public class NumeroSecreto {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numeroSecreto = new Random().nextInt(10) + 1;
        System.out.println("""
                Vamos brincar de adivinhar o número secreto?
                Informe um número de 1 a 10:
                """);

        int tentativas = 1;
        boolean acertou = false;

        while (!acertou) {
            int chute = entrada.nextInt();
            if (chute == numeroSecreto) {
                acertou = true;
                System.out.println("Parabéns! Você acertou o número secreto com " + tentativas + " tentativas.");
            } else if (chute < numeroSecreto) {
                System.out.println("Número errado. Tente um número maior.");
                tentativas++;
            } else {
                System.out.println("Número errado. Tente um número menor.");
                tentativas++;
            }
        }
        entrada.close();
    }
}

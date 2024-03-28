package com.fiap.introducao.desvio_encadeado;
/**
 * # Dado três números, informar o de maior valor
 */

import java.util.Scanner;

public class MaiorDeTres {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe o primeiro número:");
        int numero1 = scanner.nextInt();
        System.out.println("Informe o segundo número:");
        int numero2 = scanner.nextInt();
        System.out.println("Informe o terceiro número:");
        int numero3 = scanner.nextInt();

        if (numero1 > numero2 && numero1 > numero3) {
            System.out.println("O primeiro número é o maior de todos");
        } else if (numero2 > numero1 && numero2 > numero3) {
            System.out.println("O segundo número é o maior de todos");
        } else {
            System.out.println("O terceiro número é o maior de todos");
        }

    }
}

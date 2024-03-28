package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

/**
 * Dados 10 números pelo usuário, some-os e mostre o total.
 */
public class SomaDosNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite 10 números:");
        System.out.println("Digite o 1º número");
        int somaTotal = scanner.nextInt();

        for (int i = 2; i <= 10; i++){
            System.out.println("Digite o " + i + "º número:");
            int numero = scanner.nextInt();
            somaTotal = somaTotal + numero;
        }
        System.out.println("Soma total= " + somaTotal);
    }
}

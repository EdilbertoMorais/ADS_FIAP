package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

/**
 * Dados 2 números, exibir o intervalo entre eles.
 */
public class IntervalorDoisNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Informe 2 números: ");
        int numero1 = scanner.nextInt();
        int numero2 = scanner.nextInt();
        System.out.println("Números dentro do intervalo entre " + numero1 + " e " + numero2 + ":");

        for (int cont = numero1 + 1; cont < numero2; cont++){
            System.out.println(cont);
        }
    }
}

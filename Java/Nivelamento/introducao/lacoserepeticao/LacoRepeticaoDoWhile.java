package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

/**
 * Somar números digitados pelo usuário até que ele digite um número negativo.
 * (O número negativo não deve ser somado)
 * Entrada: 5 4 1 10 12 -4
 * Saída: 32
 */
public class LacoRepeticaoDoWhile {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero, soma = 0;

        do {
            System.out.println("Digite um número");
            numero = scanner.nextInt();
            if (numero > 0) {
                soma += numero;
            }
        } while (numero >= 0);

        System.out.print("Soma = " + soma);
    }
}

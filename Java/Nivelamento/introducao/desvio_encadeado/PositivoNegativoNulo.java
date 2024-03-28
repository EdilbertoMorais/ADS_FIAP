package com.fiap.introducao.desvio_encadeado;

import java.util.Scanner;

/**
 * Dado um número pelo usuário, informar se ele é positivo, negativo ou nulo.
 */
public class PositivoNegativoNulo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("informe um número:");
        int numero = scanner.nextInt();

        if (numero > 0) {
            System.out.println("Número Positivo.");
        } else if (numero < 0) {
            System.out.println("Número Negativo.");
        }else {
            System.out.println("Número Nulo.");
        }
    }
}

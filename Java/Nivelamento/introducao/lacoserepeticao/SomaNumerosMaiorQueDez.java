package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

public class SomaNumerosMaiorQueDez {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numero, soma = 0;

        do {
            System.out.println("Digite um número");
            numero = scanner.nextInt();
            if (numero > 10) {
                soma += numero;
            }
        } while (numero >= 0);
        System.out.print("Soma = " + soma);
    }
}

package com.fiap.introducao.lacoserepeticao;

import java.util.Scanner;

/**
 * Dados 5 números pelo usuário, exibir o de maior.
 * Entrada: digite 5 números: 5 9 80 -2 5
 * saída: Maior valor: 80
 */
public class MaiorEntreCincoNumeros {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numeroMaior = 0;

        System.out.println("Digite 5 números:");

        for (int i = 1; i <= 5; i++){
            System.out.println("Digite o " + i + "º número:");
            int numero = scanner.nextInt();
            if (numero > numeroMaior){
                numeroMaior = numero;
            }
        }
        System.out.println("Maior valor = " + numeroMaior);

    }
}
